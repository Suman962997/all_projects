import os
import re
from typing import List, Dict
from dotenv import load_dotenv
from llama_parse import LlamaParse
from difflib import SequenceMatcher
import time
import pdf_changes


load_dotenv()

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def extract_text_from_pdf(pdf_path: str) -> str:
    parser = LlamaParse(api_key=os.getenv("KLAMA"), result_type="markdown")
    with open(pdf_path, "rb") as f:
        docs = parser.load_data(f, extra_info={"file_name": os.path.basename(pdf_path)})
    return "\n".join([doc.text for doc in docs])


def extract_tables_with_questions(text: str) -> List[Dict[str, str]]:
    tables_with_questions = []
    lines = text.splitlines()

    current_question = None
    current_table = []

    for line in lines:
        if re.match(r"^\s*\|.*\|\s*$", line):  # Detect markdown table rows
            current_table.append(line)
        else:
            if current_table:
                if len(current_table) >= 2:  # Minimum: header + 1 row
                    tables_with_questions.append({
                        "question": current_question or "Unknown Question",
                        "answer": "\n".join(current_table)
                    })
                current_table = []

            if line.strip() and not line.strip().startswith("|"):
                current_question = line.strip()
    # Catch any table at EOF
    if current_table and len(current_table) >= 2:
        
        tables_with_questions.append({
            "question": current_question or "Unknown Question",
            "answer": "\n".join(current_table)
        })

    return tables_with_questions


def markdown_table_to_json(table: str) -> List[Dict[str, str]]:
    lines = table.strip().splitlines()
    if len(lines) < 2:
        return []

    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    data_rows = lines[2:] if re.match(r'^\s*\|?\s*-+', lines[1]) else lines[1:]

    json_data = []
    for row in data_rows:
        if not row.strip().startswith("|"):
            continue
        values = [cell.strip() for cell in row.strip("|").split("|")]
        if len(values) < len(headers):
            values += [""] * (len(headers) - len(values))
        json_data.append(dict(zip(headers, values)))
    return json_data

def match_questions_to_tables(tables: List[Dict[str, str]], questions: List[str]) -> Dict[str, List[Dict[str, str]]]:
    matched = {}
    for user_question in questions:
        best_match = None
        best_score = 0.0

        for item in tables:
            extracted_question = item["question"]
            score = similarity(user_question, extracted_question)

            if score > best_score:
                best_score = score
                best_match = item

        # Optional threshold to avoid bad matches
        if best_match and best_score > 0.6:
            matched[user_question] = markdown_table_to_json(best_match["answer"])
        else:
            matched[user_question] = [{"error": "No good match found for this question."}]

    return matched






##################################QUESTIONS#############################################


def normalize(text: str) -> str:
    """Lowercase, remove punctuation, extra whitespace."""
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', text.lower())).strip()

def fuzzy_match(target: str, candidates: List[str], threshold: float = 0.85) -> str:
    """Return best fuzzy match from candidates based on similarity threshold."""
    target_norm = normalize(target)
    best_match = ""
    best_score = 0.0
    for candidate in candidates:
        score = SequenceMatcher(None, target_norm, normalize(candidate)).ratio()
        if score > best_score and score >= threshold:
            best_match = candidate
            best_score = score
    return best_match if best_match else None

def table(result: Dict[str, List[Dict[str, str]]], qdict: Dict) -> List[Dict[str, str]]:
    question = qdict.get("question", "")
    column = qdict.get("columns", {})
    # Normalize all keys in result to match against normalized question
    normalized_result = {normalize(k): v for k, v in result.items()}
    matched_question_key = fuzzy_match(question, list(result.keys()))

    if not matched_question_key:
        print("❌ No matching question found.")
        return []

    table_json = result[matched_question_key]
    if not table_json or (len(table_json) == 1 and 'error' in table_json[0]):
        print("⚠️ Table not found or contains error.")
        return []

    filtered_table = []
    for row in table_json:
        filtered_row = {}
        row_keys = list(row.keys())
        for canonical_col, aliases in column.items():
            matched_key = None
            for alias in aliases:
                matched_key = fuzzy_match(alias, row_keys)
                if matched_key:
                    break
            filtered_row[canonical_col] = row.get(matched_key, "") if matched_key else ""
        filtered_table.append(filtered_row)

    return filtered_table



def llama_parse_function(pdf_path:str):
    start_time = time.time()  # ⏱ Start time 
    
    questions = [
        "Details of business activities (accounting for 90% of the turnover)",
        "Products / Services sold by the entity (accounting for 90% of the entity’s Turnover)",
        "Number of locations where plants and/or operations/offices of the entity are situated",
        "Number of locations",
        "Employees and workers (including differently abled):",
        "Differently abled Employees and workers:",
        "Participation/Inclusion/Representation of women",
        "Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
        "Names of holding / subsidiary / associate companies / joint ventures",
        "Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
        "Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format."
    ]


    text = extract_text_from_pdf(pdf_path)
    tables = extract_tables_with_questions(text)
    results = match_questions_to_tables(tables, questions)


    end_time = time.time()  # End time
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    print(f"\n⏱ Execution Time: {minutes} minutes, {seconds} seconds")        # if os.path.exists(temp_path):

    return results



    
        
        


