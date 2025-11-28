import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
import os


def rotate_pdf(rotated_pages: list, pdf_path: str, output_name: str = None):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    print("PDF SHOULD ROTATE !")

    for i, page in enumerate(reader.pages, start=1):  # Pages are 1-indexed
        if i in rotated_pages:
            page.rotate(90)
            print(f"Rotated page {i}")
        writer.add_page(page)

    # Auto-generate output filename if not given
    if output_name is None:
        base, ext = os.path.splitext(pdf_path)
        output_name = f"{base}_rotated{ext}"

    with open(output_name, "wb") as f:
        writer.write(f)

    abs_path = os.path.abspath(output_name)
    print(f"PDF saved at: {abs_path}")
    return abs_path

def find_sideway(pdf_path:str):
    pages=[]
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            # Extract character info (with orientation)
            chars = page.chars  
            if not chars:
                continue
            
            # Collect text angles
            angles = [round(c["upright"], 2) for c in chars]  
            # "upright" = 1 if normal, 0 if rotated, -1 if upside-down

            if sum(angles)/len(angles) < 0.8:  # threshold for rotated text
                # print(f"Page {i} likely rotated (sideways text).")
                pages.append(i)
                continue
        if pages==[]:
            return pdf_path
        elif pages:
            print(pages)
            return rotate_pdf(pages,pdf_path)
        else:
            print("NO ONE THIS PDF ")
            return None    


