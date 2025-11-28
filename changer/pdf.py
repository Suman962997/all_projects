from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import json
import random
from typing import Any
from models import create_pdf_model
from sqlalchemy.orm import declarative_base, relationship,Session
from fastapi import Depends
from database import engine, SessionLocal
from sqlalchemy import Column, Integer, String, ForeignKey, Text,text,inspect,desc
from models import Base,create_pdf_model,TableRegistry  # Import if not already done
from database import engine, SessionLocal


session = SessionLocal()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




def find_percentage(part, whole):
    return round((part / whole) * 100)




def random_number():
    list1 = [32, 20, 38, 47, 59, 96]
    return random.choice(list1)




def get_table_data(table_name: str):
    # Dynamically create model
    PDFTable = create_pdf_model(table_name)

    # Create session
    session = SessionLocal()

    try:
        # Query all rows from that table
        results = session.query(PDFTable).all()
        return [
            {
                "id": r.id,
                "section": r.section,
                "title": r.title,
                "categoryNo": r.categoryNo,
                "subtitle": r.subtitle,
                "question_no": r.question_no,
                "question": r.question,
                "answer": r.answer,
                "created_at": r.created_at,
            }
            for r in results
        ]
    finally:
        session.close()


def get_principle(principle:str):
    dicts={
        'principle_1':'one',
        'principle_2':'two',
        'principle_3':'three',
        'principle_4':'four',
        'principle_5':'five',
        'principle_6':'six',
        'principle_7':'seven',
        'principle_8':'eight',
        'principle_9':'nine',

    }
    return dicts[principle]




def answer_progress(table_name: str, table_section: Any, section_principle: Any):
    if not table_name:
        return {"error": "Table name is required"}

    # Step 1: Registry validation
    filters = {"section": table_section, "table_name": table_name}
    if section_principle:
        filters["principle"] = section_principle

    registry_entry = session.query(TableRegistry).filter_by(**filters).first()
    if not registry_entry:
        return {"error": f"Table '{table_name}' not found in registry"}

    # Step 2: Check if table exists in DB
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        return {"error": f"Table '{table_name}' does not exist in the database"}

    # Step 3: Load model dynamically & fetch rows
    PDFModel = create_pdf_model(table_name)
    results = session.query(PDFModel).all()

    # Convert rows to dicts
    data = [
        {
            "section": row.section,
            "categoryNo": row.categoryNo,
            "question": row.question,
            "answer": row.answer,
        }
        for row in results
    ]

    # Section mapping
    if section_principle:
        section_filter = "SECTION C"
        category_filter = get_principle(section_principle)
    else:
        section_filter = "SECTION A" if table_section == "section_a" else "SECTION B"
        category_filter = None

    # Collect questions and valid answers
    questions = []
    pure_answers = []

    for d in data:
        if d["section"] == section_filter and (not category_filter or d["categoryNo"] == category_filter):
            questions.append(d["question"])
            if d["answer"] not in ("Not Applicable", "[]", None):
                pure_answers.append(d["answer"])

    return find_percentage(len(pure_answers), len(questions)) if questions else 0




# def create_pdf(json_data: list, pdf_name: str):
#     print("Generating PDF from JSON data...")

#     # Styles Setup
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='Question', fontSize=11, spaceAfter=6, leading=14))
#     styles.add(ParagraphStyle(name='Answer', fontSize=11, textColor=colors.darkblue, leftIndent=10, leading=14))
#     styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))

#     output_path = f"{pdf_name}.pdf"
#     doc = SimpleDocTemplate(
#         output_path,
#         pagesize=letter,
#         rightMargin=40,
#         leftMargin=40,
#         topMargin=60,
#         bottomMargin=40
#     )

#     elements = []

#     # Title Page
#     elements.append(Paragraph("Aeiforo", styles['Heading2']))
#     elements.append(Paragraph("BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT", styles['Title']))
#     elements.append(Spacer(1, 20))

#     # Process Data in Order
#     current_section = current_title = current_subtitle = None

#     for item in json_data:
#         section = item.get("section", "").strip()
#         title = item.get("title", "").strip()
#         subtitle = item.get("subtitle", "").strip()
#         question_no = item.get("question_no", "").strip()
#         question_text = item.get("question", "").strip()
#         answer = item.get("answer", "")

#         # Section Heading
#         if section != current_section:
#             current_section = section
#             elements.append(Spacer(1, 16))
#             elements.append(Paragraph(section, styles['Heading2']))

#         # Title Heading
#         if title != current_title:
#             current_title = title
#             elements.append(Spacer(1, 12))
#             elements.append(Paragraph(title, styles['Heading3']))

#         # Subtitle Heading
#         if subtitle != current_subtitle:
#             current_subtitle = subtitle
#             elements.append(Spacer(1, 8))
#             elements.append(Paragraph(subtitle, styles['Heading4']))

#         # Question
#         elements.append(Paragraph(f"<b>{question_no}. {question_text}</b>", styles['Question']))

#         # Parse the Answer
#         parsed_answer = answer
#         if isinstance(answer, str) and answer.strip().startswith("["):
#             try:
#                 parsed_answer = json.loads(answer)
#             except json.JSONDecodeError:
#                 pass  # Leave as string if invalid JSON

#         # Render Table if list of dicts
#         if isinstance(parsed_answer, list) and all(isinstance(row, dict) for row in parsed_answer):
#             if len(parsed_answer) > 0:
#                 headers = list(parsed_answer[0].keys())
#                 table_data = [[Paragraph(h, styles['TableCell']) for h in headers]]
#                 for row in parsed_answer:
#                     table_data.append([Paragraph(str(row.get(col, "")), styles['TableCell']) for col in headers])

#                 col_width = 480 / len(headers)
#                 t = Table(table_data, colWidths=[col_width]*len(headers), repeatRows=1)
#                 t.setStyle(TableStyle([
#                     ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                     ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
#                     ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#                     ('VALIGN', (0, 0), (-1, -1), 'TOP'),
#                     ('FONTSIZE', (0, 0), (-1, -1), 9),
#                     ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
#                     ('TOPPADDING', (0, 0), (-1, -1), 4),
#                 ]))
#                 elements.append(t)
#             else:
#                 # Empty Table Case
#                 elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))
#         elif isinstance(parsed_answer, list):
#             # List of strings or invalid dict structure
#             for line in parsed_answer:
#                 elements.append(Paragraph(str(line), styles['Answer']))
#         elif isinstance(parsed_answer, str):
#             elements.append(Paragraph(parsed_answer.strip() or "N/A", styles['Answer']))
#         else:
#             elements.append(Paragraph(str(parsed_answer), styles['Answer']))

#         elements.append(Spacer(1, 8))

#     # Build PDF
#     doc.build(elements)
#     print(f"✅ PDF created successfully: {output_path}")
#     return output_path


# def create_pdf(json_data: list, pdf_name: str):
#     print("Generating PDF from JSON data...")

#     # Styles Setup
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='Question', fontSize=11, spaceAfter=6, leading=14))
#     styles.add(ParagraphStyle(name='Answer', fontSize=11, textColor=colors.darkblue, leftIndent=10, leading=14))
#     styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))

#     output_path = f"{pdf_name}.pdf"
#     doc = SimpleDocTemplate(
#         output_path,
#         pagesize=letter,
#         rightMargin=40,
#         leftMargin=40,
#         topMargin=60,
#         bottomMargin=40
#     )

#     elements = []

#     # Title Page
#     elements.append(Paragraph("Aeiforo", styles['Heading2']))
#     elements.append(Paragraph("BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT", styles['Title']))
#     elements.append(Spacer(1, 20))

#     # Process Data in Order
#     current_section = current_title = current_subtitle = None

#     for item in json_data:
#         section = item.get("section", "").strip()
#         title = item.get("title", "").strip()
#         subtitle = item.get("subtitle", "").strip()
#         question_no = item.get("question_no", "").strip()
#         question_text = item.get("question", "").strip()
#         answer = item.get("answer", "")

#         # Section Heading
#         if section != current_section:
#             current_section = section
#             elements.append(Spacer(1, 16))
#             elements.append(Paragraph(section, styles['Heading2']))

#         # Title Heading
#         if title != current_title:
#             current_title = title
#             elements.append(Spacer(1, 12))
#             elements.append(Paragraph(title, styles['Heading3']))

#         # Subtitle Heading
#         if subtitle != current_subtitle:
#             current_subtitle = subtitle
#             elements.append(Spacer(1, 8))
#             elements.append(Paragraph(subtitle, styles['Heading4']))

#         # Question
#         elements.append(Paragraph(f"<b>{question_no}. {question_text}</b>", styles['Question']))

#         # Parse the Answer
#         parsed_answer = answer
#         if isinstance(answer, str) and answer.strip().startswith("["):
#             try:
#                 parsed_answer = json.loads(answer)
#             except json.JSONDecodeError:
#                 pass  # Leave as string if invalid JSON

#         # CASE 1: List of dicts → Table with headers
#         if isinstance(parsed_answer, list) and all(isinstance(row, dict) for row in parsed_answer):
#             if len(parsed_answer) > 0:
#                 headers = list(parsed_answer[0].keys())
#                 table_data = [[Paragraph(h, styles['TableCell']) for h in headers]]
#                 for row in parsed_answer:
#                     table_data.append([Paragraph(str(row.get(col, "")), styles['TableCell']) for col in headers])

#                 col_width = 480 / len(headers)
#                 t = Table(table_data, colWidths=[col_width]*len(headers), repeatRows=1)
#                 t.setStyle(TableStyle([
#                     ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                     ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#                     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
#                     ('FONTSIZE', (0, 0), (-1, -1), 9),
#                     ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
#                     ('TOPPADDING', (0, 0), (-1, -1), 4),
#                 ]))
#                 elements.append(t)
#             else:
#                 elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))

#         # CASE 2: List of strings/numbers → Horizontal table (P1..Pn)
#         elif isinstance(parsed_answer, list):
#             if len(parsed_answer) > 0:
#                 # Generate headers P1, P2, ..., Pn
#                 headers = [f"P{i+1}" for i in range(len(parsed_answer))]
#                 values = [str(val) for val in parsed_answer]

#                 table_data = [
#                     [Paragraph(h, styles['TableCell']) for h in headers],  # header row
#                     [Paragraph(v, styles['TableCell']) for v in values]    # values row
#                 ]

#                 col_width = 480 / len(headers)
#                 t = Table(table_data, colWidths=[col_width]*len(headers), repeatRows=1)
#                 t.setStyle(TableStyle([
#                     ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                     ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#                     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
#                     ('FONTSIZE', (0, 0), (-1, -1), 9),
#                     ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
#                     ('TOPPADDING', (0, 0), (-1, -1), 4),
#                 ]))
#                 elements.append(t)
#             else:
#                 elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))

#         # CASE 3: String or Other → Just Paragraph
#         elif isinstance(parsed_answer, str):
#             elements.append(Paragraph(parsed_answer.strip() or "N/A", styles['Answer']))
#         else:
#             elements.append(Paragraph(str(parsed_answer), styles['Answer']))

#         elements.append(Spacer(1, 8))

#     # Build PDF
#     doc.build(elements)
#     print(f"✅ PDF created successfully: {output_path}")
#     return output_path



# def create_pdf(json_data: list, pdf_name: str):
#     print("Generating PDF from JSON data...")

#     # Styles Setup
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='Question', fontSize=11, spaceAfter=6, leading=14))
#     styles.add(ParagraphStyle(name='Answer', fontSize=11, textColor=colors.darkblue, leftIndent=10, leading=14))
#     styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))

#     output_path = f"{pdf_name}.pdf"
#     doc = SimpleDocTemplate(
#         output_path,
#         pagesize=letter,
#         rightMargin=40,
#         leftMargin=40,
#         topMargin=60,
#         bottomMargin=40
#     )

#     elements = []

#     # Title Page
#     elements.append(Paragraph("Aeiforo", styles['Heading2']))
#     elements.append(Paragraph("BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT", styles['Title']))
#     elements.append(Spacer(1, 20))

#     # Track headings
#     current_section = None
#     current_title = None
#     current_subtitle = None

#     for item in json_data:
#         section = item.get("section", "").strip()
#         title = item.get("title", "").strip()
#         subtitle = item.get("subtitle", "").strip()
#         question_no = item.get("question_no", "").strip()
#         question_text = item.get("question", "").strip()
#         answer = item.get("answer", "")

#         # Section Heading (only once until it changes)
#         if section and section != current_section:
#             current_section = section
#             current_title = None        # reset when section changes
#             current_subtitle = None
#             elements.append(Spacer(1, 16))
#             elements.append(Paragraph(section, styles['Heading2']))

#         # Title Heading (only once until it changes)
#         if title and title != current_title:
#             current_title = title
#             current_subtitle = None     # reset when title changes
#             elements.append(Spacer(1, 12))
#             elements.append(Paragraph(title, styles['Heading3']))

#         # Subtitle Heading (only once until it changes)
#         if subtitle and subtitle != current_subtitle:
#             current_subtitle = subtitle
#             elements.append(Spacer(1, 8))
#             elements.append(Paragraph(subtitle, styles['Heading4']))

#         # Question
#         elements.append(Paragraph(f"<b>{question_no}. {question_text}</b>", styles['Question']))

#         # Parse the Answer
#         parsed_answer = answer
#         if isinstance(answer, str) and answer.strip().startswith("["):
#             try:
#                 parsed_answer = json.loads(answer)
#             except json.JSONDecodeError:
#                 pass  # Leave as string if invalid JSON

#         # CASE 1: Table from list of dicts
#         if isinstance(parsed_answer, list) and all(isinstance(row, dict) for row in parsed_answer):
#             if parsed_answer:
#                 headers = list(parsed_answer[0].keys())
#                 table_data = [[Paragraph(h, styles['TableCell']) for h in headers]]
#                 for row in parsed_answer:
#                     table_data.append([Paragraph(str(row.get(col, "")), styles['TableCell']) for col in headers])

#                 col_width = 480 / len(headers)
#                 t = Table(table_data, colWidths=[col_width] * len(headers), repeatRows=1)
#                 t.setStyle(TableStyle([
#                     ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                     ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
#                     ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#                     ('VALIGN', (0, 0), (-1, -1), 'TOP'),
#                     ('FONTSIZE', (0, 0), (-1, -1), 9),
#                     ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
#                     ('TOPPADDING', (0, 0), (-1, -1), 4),
#                 ]))
#                 elements.append(t)
#             else:
#                 elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))

#         # CASE 2: List of strings → Paragraphs
#         elif isinstance(parsed_answer, list):
#             for line in parsed_answer:
#                 elements.append(Paragraph(str(line), styles['Answer']))

#         # CASE 3: String or Other
#         elif isinstance(parsed_answer, str):
#             elements.append(Paragraph(parsed_answer.strip() or "N/A", styles['Answer']))
#         else:
#             elements.append(Paragraph(str(parsed_answer), styles['Answer']))

#         elements.append(Spacer(1, 8))

#     # Build PDF
#     doc.build(elements)
#     print(f"✅ PDF created successfully: {output_path}")
#     return output_path



def create_pdf(json_data: list, pdf_name: str):
    print("Generating PDF from JSON data...")

    # Styles Setup
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Question', fontSize=11, spaceAfter=6, leading=14))
    styles.add(ParagraphStyle(name='Answer', fontSize=11, textColor=colors.darkblue, leftIndent=10, leading=14))
    styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))

    output_path = f"{pdf_name}.pdf"
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=60,
        bottomMargin=40
    )

    elements = []

    # Title Page
    elements.append(Paragraph("Aeiforo", styles['Heading2']))
    elements.append(Paragraph("BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT", styles['Title']))
    elements.append(Spacer(1, 20))

    # Track headings
    current_section = current_title = current_partRoman = current_subtitle = None

    for item in json_data:
        section = item.get("section", "").strip()
        title = item.get("title", "").strip()
        subtitle = item.get("subtitle", "").strip()
        partRoman = item.get("partRoman", "").strip()
        question_no = item.get("question_no", "").strip()
        question_text = item.get("question", "").strip()
        answer = item.get("answer", "")

        # Section Heading
        if section and section != current_section:
            current_section = section
            current_title = None
            current_subtitle = None
            elements.append(Spacer(1, 16))
            elements.append(Paragraph(section, styles['Heading2']))

        # Title Heading
        if title != current_title:
            current_title = title
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(title, styles['Heading3']))

        # Subtitle Heading
        # if subtitle != current_subtitle:
        #     current_subtitle = subtitle
        #     elements.append(Spacer(1, 8))
        #     elements.append(Paragraph(subtitle, styles['Heading4']))

        # PartRoman + Subtitle combined
        if partRoman and subtitle:
            combined_heading = f"{partRoman}.{subtitle}"
            if combined_heading != current_subtitle:
                current_subtitle = combined_heading
                elements.append(Spacer(1, 10))
                elements.append(Paragraph(combined_heading, styles['Heading4']))



        # Question
        elements.append(Paragraph(f"<b>{question_no}. {question_text}</b>", styles['Question']))

        # Parse the Answer (try JSON)
        parsed_answer = answer
        if isinstance(answer, str) and answer.strip().startswith("["):
            try:
                parsed_answer = json.loads(answer)
            except json.JSONDecodeError:
                pass  # Keep as string if invalid JSON

        # CASE 1: List of dicts → Table with headers
        if isinstance(parsed_answer, list) and all(isinstance(row, dict) for row in parsed_answer):
            if parsed_answer:
                headers = list(parsed_answer[0].keys())
                table_data = [[Paragraph(h, styles['TableCell']) for h in headers]]
                for row in parsed_answer:
                    table_data.append([Paragraph(str(row.get(col, "")), styles['TableCell']) for col in headers])

                col_width = 480 / len(headers)
                t = Table(table_data, colWidths=[col_width]*len(headers), repeatRows=1)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                ]))
                elements.append(t)
            else:
                elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))

        # CASE 2: List of strings/numbers → Horizontal table (P1..Pn)
        elif isinstance(parsed_answer, list):
            if parsed_answer:
                headers = [f"P{i+1}" for i in range(len(parsed_answer))]
                values = [str(val) for val in parsed_answer]

                table_data = [
                    [Paragraph(h, styles['TableCell']) for h in headers],
                    [Paragraph(v, styles['TableCell']) for v in values]
                ]

                col_width = 480 / len(headers)
                t = Table(table_data, colWidths=[col_width]*len(headers), repeatRows=1)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                ]))
                elements.append(t)
            else:
                elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))

        # CASE 3: String or Other → Just Paragraph
        elif isinstance(parsed_answer, str):
            elements.append(Paragraph(parsed_answer.strip() or "N/A", styles['Answer']))
        else:
            elements.append(Paragraph(str(parsed_answer), styles['Answer']))

        elements.append(Spacer(1, 8))

    # Build PDF
    doc.build(elements)
    print(f"✅ PDF created successfully: {output_path}")
    return output_path