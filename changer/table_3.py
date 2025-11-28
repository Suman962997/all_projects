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





def llama_parse_function(pdf_path:str,section_key:int):
    start_time = time.time()  # ⏱ Start time 
    
    
    questions_1= [
    "Percentage coverage by training and awareness programmes on any of the Principles during the financial year:",
    "Monetary",
    "Non-Monetary",
    "Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed.",
    "Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement agency for the charges of bribery/ corruption",
    "Details of complaints with regard to conflict of interest",
    "Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services procured) in the following format:",
    "Provide details of concentration of purchases and sales with trading houses, dealers, and related parties along-with loans and advances & investments, with related parties, in the following format:",
    "Awareness programmes conducted for value chain partners on any of the Principles during the financial year:",
    ]
    
    questions_2=[
        "Percentage of R&D and capital expenditure (capex) investments in specific technologies to improve the environmental and social impacts of product and processes to total R&D and capex investments made by the entity, respectively.",
        "Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing industry) or for its services (for service industry)? If yes, provide details in the following format?",
        "If there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the Life Cycle Perspective / Assessments (LCA) or through any other means, briefly describe the same along-with action taken to mitigate the same.",
        "Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)",
        "Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:",
        "Reclaimed products and their packaging materials (as percentage of products sold) for each product category.",

    ]

    questions_3=[
        "Details of measures for the well-being of employees:",
        "Details of measures for the well-being of workers:",
        "Details of retirement benefits, for Current and Previous FY",
        "Return to work and Retention rates of permanent employees and workers that took parental leave.",
        "Is there a mechanism available to receive and redress grievances for the following categories of employees and worker? If yes, give details of the mechanism in brief",
        "Membership of employees and worker in association(s) or Unions recognised by the listed entity:",
        "Details of training given to employees and workers:",
        "Details of performance and career development reviews of employees and workers:",
        "Details of safety related incidents, in the following format:",
        "Number of Complaints on the following made by employees and workers:",
        "Assessments for the year:",
        "Provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in Q11 of Essential Indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:",
        "Details on assessment of value chain partners:"
        
    ]

    questions_4=[
     "List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group.",
     ""           
    ]

    questions_5=[
        "Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:",
        "Details of minimum wages paid to employees and workers, in the following format:",
        "Details of remuneration/salary/wages",
        "Number of Complaints on the following made by employees and workers:",
        "Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format:",
        "Assessments for the year:",
        "Details on assessment of value chain partners:",        
    ]

    questions_6=[
        "Details of total energy consumption (in Joules or multiples) and energy intensity, in the following format:",
        "Provide details of the following disclosures related to water, in the following format:",
        "Provide the following details related to water discharged:",
        "Please provide details of air emissions (other than GHG emissions) by the entity, in the following format:",
        "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:",
        "Provide details related to waste management by the entity, in the following format:",
        "If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:",
        "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:",
        "Is the entity compliant with the applicable environmental law/ regulations/ guidelines in India; such as the Water (Prevention and Control of Pollution) Act, Air (Prevention and Control of Pollution) Act, Environment protection act and rules thereunder (Y/N). If not, provide details of all such non-compliances, in the following format:",
        "Water withdrawal, consumption and discharge in areas of water stress (in kilolitres):",
        "Please provide details of total Scope 3 emissions & its intensity, in the following format",
        "If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:"
        
    ]

    questions_7=[
        "List the top 10 trade and industry chambers/ associations (determined based on the total members of such body) the entity is a member of/ affiliated to, in the following format",
        "Provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities.",
        "Details of public policy positions advocated by the entity:",
    ]

    questions_8=[
        "Details of Social Impact Assessments (SIA) of projects undertaken by the entity based on applicable laws, in the current financial year.",
        "Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following format",
        "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
        "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost",
        "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments (Reference: Question 1 of Essential Indicators above):",
        "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts as identified by government bodies",
        "Details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:",
        "Details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved.",
        "Details of beneficiaries of CSR Projects:",

    ]

    questions_9=[
        "Turnover of products and/ services as a percentage of turnover from all products/service that carry information about:",
        "Number of consumer complaints in respect of the following:",
        "Details of instances of product recalls on account of safety issues:",        
    ]

    def section_key_fun(section):
        question_dict={
            1:questions_1,
            2:questions_2,
            3:questions_3,
            4:questions_4,
            5:questions_5,
            6:questions_6,
            7:questions_7,
            8:questions_8,
            9:questions_9,
        }
        
        return question_dict[section]


    question=section_key_fun(section_key)
    text = extract_text_from_pdf(pdf_path)
    tables = extract_tables_with_questions(text)
    results = match_questions_to_tables(tables, question)


    end_time = time.time()  # End time
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    print(f"\n⏱ Execution Time: {minutes} minutes, {seconds} seconds")        # if os.path.exists(temp_path):

    return results



    
        
        


