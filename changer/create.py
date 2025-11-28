import os
import io
from PyPDF2 import PdfReader, PdfWriter
from llama_parse import LlamaParse
import time
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import re
import string
from difflib import SequenceMatcher
import pdfplumber
from httpx import HTTPStatusError  # LlamaParse uses httpx internally
import pdf_changes
import h


app=FastAPI()
load_dotenv()


def normalize(text: str) -> str:
    # Lowercase, remove punctuations, and normalize spaces
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.split())
    return text

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()



def extract_text_from_pdf(pdf_path: str) -> str:
    
    parser = LlamaParse(api_key=os.getenv("LLAMABRSR"), result_type="markdown")
    max_retries = 6
    delay = 5  # start with 5 seconds

    for attempt in range(max_retries):
        try:
            with open(pdf_path, "rb") as f:
                docs = parser.load_data(f, extra_info={"file_name": os.path.basename(pdf_path)})
            return "\n".join([doc.text for doc in docs])

        except HTTPStatusError as e:
            if e.response.status_code == 429:
                print(f"[{attempt+1}/{max_retries}] ⚠️ Rate limit hit. Waiting {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # exponential backoff
            else:
                raise e  # re-raise other HTTP errors

        except Exception as e:
            if "429" in str(e):
                print(f"[{attempt+1}/{max_retries}] ⚠️ Rate limit hit (string match). Waiting {delay} seconds...")
                time.sleep(delay)
                delay *= 2
            else:
                raise e

    raise Exception("❌ Failed after maximum retries due to rate limiting.")


def extract_answers(text: str, questions: list) -> dict:
    result = {}
    table_pattern = r"^\|\s*(.*?)\s*\|(.+?)\|$"
    lines = text.split("\n")
    table_rows = []
    
    for line in lines:
        match = re.match(table_pattern, line)
        if match:
            q = match.group(1).strip()
            ans_cells = [cell.strip() for cell in match.group(2).split("|")]
            table_rows.append((q, ans_cells))

    for q in questions:
        q_norm = normalize(q)
        best_match = None
        best_score = 0.0

        for row_q, ans_cells in table_rows:
            row_q_norm = normalize(row_q)
            score = similarity(q_norm, row_q_norm)

            if score > best_score and score >= 0.80:  # 80% match threshold
                best_match = ans_cells
                best_score = score

        result[q] = best_match if best_match else None

    return result





@app.get("/frfr/")
def llama_parse_function():
    start_time = time.time()  # ⏱ Start time 
    
    
    questions= [
    "Whether your entity’s policy/policies cover each principle and its core elements of the NGRBCs",
    "Has the policy been approved by the Board?",
    "Whether the entity has translated the policy into procedures",
    "Do the enlisted policies extend to your value chain partners?",
    "Name of the national and international codes/certifications/labels/standards adopted by your entity and mapped to each principle",
    "Specific commitments, goals and targets set by the entity with defined timelines, if any",
    "Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues?",
    "Indicate whether review was undertaken by Director / Committee of the Board/ Any other Committee",
    "Frequency(Annually/ Half yearly/ Quarterly/ Any other – please specify)",
    "Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency",
    "If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below"
]
    pdf_path = r"C:\Users\coda\Documents\DABUR INDIA LIMITED.pdf"
    text = extract_text_from_pdf(pdf_changes.find_sideway(pdf_path))

    extracted_data = extract_answers(text, questions)

    # tables = extract_tables_with_questions(text)
    # results = match_questions_to_tables(tables, questions)


    end_time = time.time()  # End time
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    print(f"\n⏱ Execution Time: {minutes} minutes, {seconds} seconds")        # if os.path.exists(temp_path):
    return {'texts':text,'datas':extracted_data}


if __name__=='__main__':
    uvicorn.run('create:app',reload=False,host='0.0.0.0',port=2000,log_level='debug')