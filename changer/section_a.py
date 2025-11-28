import pdfplumber
import pytesseract
from PIL import Image
import io
import re
import pandas as pd

                                        ######## PART II #########

def  Details_of_business(pdf_file):
    print("PART II")

    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of business activities (accounting for 90% of the turnover)",
        "Details of business activities",
        "accounting for 90% of the turnover"

    ]
    q_ends = [
        "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
        "Products/Services sold by the",
        "accounting for 90% of the entity’s Turnover"
        
    ]
    keys = [
        "Description of Main Activity",
        "Description of Business Activity",
        "% of Turnover of the entity",
    ]

    keys_3 = [
        "S.No",
        "Description of Main Activity",
        "Description of Business Activity",
        "% of Turnover of the entity",
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_3 = []
    final_4 = []
    for f in output_rows:
        if len(f) == 3:
            final_3.append(f)
        elif len(f) == 4:
            final_4.append(f)


    
    myout = []

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_4) > len(final_3):
        for row in final_4:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Details_of_business("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

def  Products_Services(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    # lines_between = ["PART II COMPLETED SUCESSFULLY !"]
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
        "Products/Services sold by the",
        "accounting for 90% of the entity’s Turnover"
    ]
    q_ends = [
        "Number of locations where plants and/or operations/",
        "Number of locations where plants",
        "offices of the entity are situated",
    ]

    keys = [
        "Product/Service",
        "NIC Code",
        "% of total Turnover contributed"
    ]

    keys_3 = [
        "S.No",
        "Product/Service",
        "NIC Code",
        "% of total Turnover contributed"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_3 = []
    final_4 = []
    for f in output_rows:
        if len(f) == 3:
            final_3.append(f)
        elif len(f) == 4:
            final_4.append(f)

    
    myout = []
    # myout = ["PART II COMPLETED SUCESSFULLY !"]

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_4) > len(final_3):
        for row in final_4:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Products_Services("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

                                        ######## PART III #########
def  Number_of_locations_where(pdf_file):
    print("PART III")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Number of locations where plants and/or operations/",
        "Number of locations where plants",
        "offices of the entity are situated",
    ]
    q_ends = [
        "Markets served by the entity",
        "Markets served ",
        "by the entity"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_4 = []
    final_5 = []
    for f in output_rows:
        if len(f) == 4:
            final_4.append(f)
        elif len(f) == 5:
            final_5.append(f)

    keys = [
        "Location",
        "No. of plants",
        "No. of offices",
        "Total"
    ]

    keys_3 = [
        "S.No",
        "Location",
        "No. of plants",
        "No. of offices",
        "Total"
    ]
    
    myout = []

    if len(final_4) > len(final_5):
        for row in final_4:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_5) > len(final_4):
        for row in final_5:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Number_of_locations_where("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")


def  Number_of_locations(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Markets served by the entity",
        "Markets served ",
        "by the entity"
    ]
    q_ends = [
        "What is the contribution of exports",
        "percentage of the total turnover",
        "total turnover of the entity"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_2 = []
    final_3 = []
    for f in output_rows:
        if len(f) == 2:
            final_2.append(f)
        elif len(f) == 3:
            final_3.append(f)

    keys = [
        "Location",
        "Number"
    ]

    keys_3 = [
        "S.No",
        "Location",
        "Number"
    ]
    
    myout = []

    if len(final_2) > len(final_3):
        for row in final_2:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_3) > len(final_2):
        for row in final_3:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Number_of_locations("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")


def  What_is_the_contribution(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "What is the contribution of exports",
        "percentage of the total turnover",
        "total turnover of the entity"
    ]
    q_ends = [
        "A brief on types of customers",
        "A brief on types of customers",
        "types of customers"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"


#@ print(What_is_the_contribution("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")


def  A_brief_on_types(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "A brief on types of customers",
        "A brief on types of customers",
        "types of customers"
    ]
    q_ends = [
        "Details as at the end of Financial Year",
        "end of Financial Year",
        "Details as at the end"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"


#@ print(A_brief_on_types("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

                                        ######## PART IV #########


def  Employees_and_workers(pdf_file):
    print("PART IV")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Employees and workers (including differently abled)",
        "Employees and workers",
        "including differently abled"

    ]
    q_ends = [
        "Differently abled Employees and workers",
        "Differently abled Employees",
        "Employees and workers"
    ]
    
    keys = [
        "Particulars",
        "Total (A)",
        "Male No. (B)",
        "Male % (B / A)",
        "Female No. (C)",
        "Female % (C / A)"
    ]

    keys_3 = [
        "S.no",
        "Particulars",
        "Total (A)",
        "Male No. (B)",
        "Male % (B / A)",
        "Female No. (C)",
        "Female % (C / A)"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_6 = []
    final_7 = []
    for f in output_rows:
        if len(f) == 6:
            final_6.append(f)
        elif len(f) == 7:
            final_7.append(f)
    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_6) > len(final_7):
        for row in final_6:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_7) > len(final_6):
        for row in final_7:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Employees_and_workers("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

def  Differently_abled_employees(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Differently abled Employees and workers",
        "Differently abled Employees",
        "Employees and workers"

    ]
    q_ends = [
        "Participation/Inclusion/Representation of women",
        "Participation/Inclusion/",
        "Representation of women"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_6 = []
    final_7 = []
    for f in output_rows:
        if len(f) == 6:
            final_6.append(f)
        elif len(f) == 7:
            final_7.append(f)

    keys = [
        "Particulars",
        "Total (A)",
        "Male No. (B)",
        "Male % (B / A)",
        "Female No. (C)",
        "Female % (C / A)"
    ]

    keys_3 = [
        "S.no",
        "Particulars",
        "Total (A)",
        "Male No. (B)",
        "Male % (B / A)",
        "Female No. (C)",
        "Female % (C / A)"
    ]
    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_6) > len(final_7):
        for row in final_6:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_7) > len(final_6):
        for row in final_7:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Differently_abled_employees("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")


def  Participation_Inclusion(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Participation/Inclusion/Representation of women",
        "Participation/Inclusion/",
        "Representation of women"

    ]
    q_ends = [
        "Turnover rate for permanent employees and workers",
        "Turnover rate for permanent",
        "employees and workers"

    ]
    keys = [
        "Category",
        "Total (A)",
        "No. and percentage of Females No. (B)",
        "No. and percentage of Females % (B / A)"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "Total (A)",
        "No. and percentage of Females No. (B)",
        "No. and percentage of Females % (B / A)"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_4 = []
    final_5 = []
    for f in output_rows:
        if len(f) == 4:
            final_4.append(f)
        elif len(f) == 5:
            final_5.append(f)


    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_4) > len(final_5):
        for row in final_4:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_5) > len(final_4):
        for row in final_5:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Participation_Inclusion("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

def  Turnover_rate(pdf_file):
    print("PART V")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Turnover rate for permanent employees and workers",
        "Turnover rate for permanent",
        "employees and workers"

    ]
    q_ends = [
        "Holding, Subsidiary and Associate Companies (including joint ventures)",
        "Holding, Subsidiary and Associate Companies",
        "including joint ventures"

    ]

    keys = [
    "Category",
    " FY (2024-25) Male",
    " FY (2024-25) Female",
    " FY (2024-25) Total",
    " FY (2023-24) Male",
    " FY (2023-24) Female",
    " FY (2023-24) Total",
    " FY (2022-23) Male",
    " FY (2022-23) Female",
    " FY (2022-23) Total",

    ]

    keys_3 = [
    "S.no",
    "Category",
    " FY (2024-25) Male",
    " FY (2024-25) Female",
    " FY (2024-25) Total",
    " FY (2023-24) Male",
    " FY (2023-24) Female",
    " FY (2023-24) Total",
    " FY (2022-23) Male",
    " FY (2022-23) Female",
    " FY (2022-23) Total",        
    ]
    

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break


    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_10 = []
    final_11 = []
    for f in output_rows:
        if len(f) == 10:
            final_10.append(f)
        elif len(f) == 11:
            final_11.append(f)

    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_10) > len(final_11):
        for row in final_10:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_11) > len(final_10):
        for row in final_11:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Turnover_rate("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")


                                        ######## PART V #########


def  Names_of_holding(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Names of holding / subsidiary / associate companies / joint ventures",
        "Names of holding / subsidiary / associate companies",
        "joint ventures"
    ]
    q_ends = [
        "Do any other entity/entities",
        "CSR Details",
        "Whether CSR is applicable"
    ]

    keys = [
              "Name of the holding / subsidiary / associate companies / joint ventures (A)",
              "Indicate whether holding/ Subsidiary/ Associate/ Joint Venture",
              "% of shares held by listed entity",
              "Does the entity indicated at column A, participate in the Business Responsibility initiatives of the listed entity? (Yes/ No)"        

    ]

    keys_3 = [
        "S.no",
              "Name of the holding / subsidiary / associate companies / joint ventures (A)",
              "Indicate whether holding/ Subsidiary/ Associate/ Joint Venture",
              "% of shares held by listed entity",
              "Does the entity indicated at column A, participate in the Business Responsibility initiatives of the listed entity? (Yes/ No)"        
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:13]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_4 = []
    final_5 = []
    for f in output_rows:
        if len(f) == 4:
            final_4.append(f)
        elif len(f) == 5:
            final_5.append(f)


    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_4) > len(final_5):
        for row in final_4:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_5) > len(final_4):
        for row in final_5:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

# print(Names_of_holding("C:/Users/coda/Documents/vendanta.pdf"))
# print("************")

def  Do_any_other_entity(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Do any other entity/entities (e.g. suppliers, distributors etc",
        "participate in the BR initiatives of the Company",
        "percentage of such entity/entities?"
    ]
    q_ends = [
        "CSR Details",
        "Whether CSR is applicable as per section 135",
        "Whether CSR is applicable"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ## #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"

#@ print(Do_any_other_entity("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

                                        ######## PART VI #########


def Whether_CSR(pdf_path):    
    with pdfplumber.open(pdf_path) as pdf:
        print("PART VI")
        ## #@ print("file opend")
        question="Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)"
        question_2="Whether CSR is applicable as per section 135 of Companies Act, 2013"
        question_3="Whether CSR is applicable as per section"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # ## #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Turnover (` in million)" 
                sec_quest_2="Turnover"
                sec_quest_3="Turnover"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # ## #@ print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                if finallist:
                    return finallist
                else:
                    return "Not Applicable"
#@ print(Whether_CSR("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

def Turnover(pdf_path):    
    with pdfplumber.open(pdf_path) as pdf:
        ## #@ print("file opend")
        question="Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)"
        question_2="Whether CSR is applicable"
        question_3="per section 135 of Companies Act, 2013"
        
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # ## #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Net worth" 
                sec_quest_2="Net worth"
                sec_quest_3="Net worth"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # ## #@ print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                if finallist:
                    return finallist
                else:
                    return "Not Applicable"
#@ print(Turnover("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")

def Net_worth(pdf_path):    
    with pdfplumber.open(pdf_path) as pdf:
        ## #@ print("file opend")
        question="Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)"
        question_2="Whether CSR is applicable"
        question_3="per section 135 of Companies Act, 2013"
        
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # ## #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Transparency and Disclosures Compliances" 
                sec_quest_2="Disclosures Compliances"
                sec_quest_3="Complaints/Grievances on any of the principles"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i+2:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i+2:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+2:]
                # ## #@ print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                if finallist:
                    return finallist
                else:
                    return "Not Applicable"
#@ print(Net_worth("C:/Users/coda/Documents/narendra.pdf"))
#@ print("************")


                                        ######## PART VII #########



def   Complaints_Grievances(pdf_file):
    print("PART VII")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Complaints/Grievances on any of the principles",
        "under the National Guidelines",
        "Responsible Business Conduct"

    ]
    q_ends = [
        "Overview of the entity’s material responsible business conduct issues",
        "Overview of the entity’s",
        "responsible business conduct issues"
    ]


    keys = [
              "Stakeholder group from whom complaint is received ",
              "Grievance Redressal Mechanism in Place (Yes/No) (If Yes, then provide web-link for grievance redress policy)",
              "Number of complaints filed during the year(FY 2024-25)",
              "Number of complaints pending resolution at close of the year(FY 2024-25)",
              "Remark(FY 2024-25)",
              "Number of complaints filed during the year(FY 2023-24)",
              "Number of complaints pending resolution at close of the year(FY 2023-24)",
              "Remark(FY 2023-24)"    ]

    keys_3 = [
              "S.no",
              "Stakeholder group from whom complaint is received ",
              "Grievance Redressal Mechanism in Place (Yes/No) (If Yes, then provide web-link for grievance redress policy)",
              "Number of complaints filed during the year(FY 2024-25)",
              "Number of complaints pending resolution at close of the year(FY 2024-25)",
              "Remark(FY 2024-25)",
              "Number of complaints filed during the year(FY 2023-24)",
              "Number of complaints pending resolution at close of the year(FY 2023-24)",
              "Remark(FY 2023-24)"    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:18]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    ##  print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_8 = []
    final_9 = []
    for f in output_rows:
        if len(f) == 8:
            final_8.append(f)
        elif len(f) == 9:
            final_9.append(f)

    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_8) > len(final_9):
        for row in final_8:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_9) > len(final_8):
        for row in final_9:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Complaints_Grievances("C:/Users/coda/Documents/titan.pdf"))
#@ print("************")



def  Please_indicate_material(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Overview of the entity’s material responsible",
        "Please indicate material responsible business",
        "business conduct issues"

    ]
    q_ends = [
        "SECTION B",
        "MANAGEMENT AND PROCESS DISCLOSURES",
        "SECTION B: MANAGEMENT AND PROCESS DISCLOSURES"
    ]
    
    keys = [
        "Material issue identified",
        "Indicate whether risk or opportunity (R/O)",
        "Rationale for identifying the risk/opportunity",
        "In case of risk, approach to adapt or mitigate",
        "Financial implications of the risk or opportunity (Indicate positive or negative implications)"
    ]

    keys_3 = [
              "S.no",
        "Material issue identified",
        "Indicate whether risk or opportunity (R/O)",
        "Rationale for identifying the risk/opportunity",
        "In case of risk, approach to adapt or mitigate",
        "Financial implications of the risk or opportunity (Indicate positive or negative implications)"
              
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:18]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}


    # print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_5 = []
    final_6 = []
    for f in output_rows:
        if len(f) == 5:
            final_5.append(f)
        elif len(f) == 6:
            final_6.append(f)

    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_5) > len(final_6):
        for row in final_5:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_6) > len(final_5):
        for row in final_6:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return None


    return myout

#@ print(Please_indicate_material("C:/Users/coda/Documents/deigeo.pdf"))
#@ print("************")




SA_II_1={
    "question":"Details of business activities (accounting for 90% of the turnover):",
    "columns":[
            "Description of Main Activity",
            "Description of Business Activity",
            "% of Turnover of the entity",
            ],
}



