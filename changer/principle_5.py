import pdfplumber
import pytesseract
from PIL import Image
import io
import re



                            ######### PRINCIPLE V ##########
                            



def  Employees_and_workers(pdf_file):
    print("PRINCIPLE 5")

    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
   "Employees and workers who have been provided ",
   "training on human rights issues"
   "of the entity, in the following format"
    ]
    q_ends = [
        "Details of minimum wages paid to employees and workers, in the following format",
        "Details of minimum wages paid",
        "employees and workers"
    ]
    keys = [
        "Category",
        "FY 2024-25Current Financial Year (Total (A))",
        "FY 2024-25Current Financial Year (No. of employees / workers covered (B))",
        "FY 2024-25Current Financial Year (% (B / A))",
        "FY 2023-24Previous Financial Year (Total (C))",
        "FY 2023-24Previous Financial Year (No. of employees / workers covered (D))",
        "FY 2023-24Previous Financial Year (% (D / C))                  "
    ]

    keys_3 = [
        "S.no",
        "Category",
        "FY 2024-25Current Financial Year (Total (A))",
        "FY 2024-25Current Financial Year (No. of employees / workers covered (B))",
        "FY 2024-25Current Financial Year (% (B / A))",
        "FY 2023-24Previous Financial Year (Total (C))",
        "FY 2023-24Previous Financial Year (No. of employees / workers covered (D))",
        "FY 2023-24Previous Financial Year (% (D / C))                  "
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_7 = []
    final_8 = []
    for f in output_rows:
        if len(f) == 7:
            final_7.append(f)
        elif len(f) == 8:
            final_8.append(f)


    
    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_7) > len(final_8):
        for row in final_7:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_8) > len(final_7):
        for row in final_8:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Employees_and_workers("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Details_of_minimum(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of minimum wages paid to employees and workers",
        "wages paid to employees and workers",
        "paid to employees and workers"
    ]
    q_ends = [
        "Details of remuneration/salary/wages",
        "remuneration/salary/wages",
        "salary/wages"
    ]
    keys = [
        "Category",
        "Total (A)",
        "Equal to Minimum Wage (No. (B))",
        "Equal to Minimum Wage (% (B / A))",
        "More than Minimum Wage (No. (C))",
        "More than Minimum Wage (% (C / A))",
        "Total (D)",
        "Equal to Minimum Wage (No. (E))",
        "Equal to Minimum Wage (% (E / D))",
        "More than Minimum Wage (No. (F))",
        "More than Minimum Wage (% (F / D))"
    ]

    keys_3 = [
        "S.No",
        "Category",
        "Total (A)",
        "Equal to Minimum Wage (No. (B))",
        "Equal to Minimum Wage (% (B / A))",
        "More than Minimum Wage (No. (C))",
        "More than Minimum Wage (% (C / A))",
        "Total (D)",
        "Equal to Minimum Wage (No. (E))",
        "Equal to Minimum Wage (% (E / D))",
        "More than Minimum Wage (No. (F))",
        "More than Minimum Wage (% (F / D))"
    ]
    

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_11 = []
    final_12= []
    for f in output_rows:
        if len(f) == 11:
            final_11.append(f)
        elif len(f) ==12:
            final_12.append(f)

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_11) > len(final_12):
        for row in final_12:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_12) > len(final_11):
        for row in final_11:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Details_of_minimum("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Details_of_remuneration(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of remuneration/salary/wages",
        "remuneration/salary/wages",
        "remuneration/salary/wages"


    ]
    q_ends = [
        "Gross Wages paid to females",
        "total wages paid by the entity",
        "Gross Wages paid to females"
    ]

    keys = [
        "category",
        "2023-24 Male Number",
        "2023-24 Male Median remuneration/ salary/ wages of respective category",
        "2023-24 Female Number",
        "2023-24 Female Median remuneration/ salary/ wages of respective category",
        "2022-23 Male Number",
        "2022-23 Male Median remuneration/ salary/ wages of respective category",
        "2022-23 Female Number",
        "2022-23 Female Median remuneration/ salary/ wages of respective category",

    ]

    keys_3 = [
        "S.no",
        "category",
        "2023-24 Male Number",
        "2023-24 Male Median remuneration/ salary/ wages of respective category",
        "2023-24 Female Number",
        "2023-24 Female Median remuneration/ salary/ wages of respective category",
        "2022-23 Male Number",
        "2022-23 Male Median remuneration/ salary/ wages of respective category",
        "2022-23 Female Number",
        "2022-23 Female Median remuneration/ salary/ wages of respective category",

        
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_9 = []
    final_10 = []
    for f in output_rows:
        if len(f) == 9:
            final_9.append(f)
        elif len(f) == 10:
            final_10.append(f)

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_9) > len(final_10):
        for row in final_9:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_10) > len(final_9):
        for row in final_10:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Details_of_remuneration("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


# def  Gross_wages_paid(pdf_file):
#     start_found = False
#     end_found = False
#     lines_between = []
#     custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

#     # Define multiple possible start and end strings
#     q_starts = [
#         "Gross Wages paid to females",
#         "total wages paid by the entity",
#         "Gross Wages paid to females"

#     ]
#     q_ends = [
#         "Do you have a focal point (Individual/ Committee)",
#         "Do you have a focal",
#         "caused or contributed to by the business"

#     ]

#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages[12:-2:]:
#             pil_image = page.to_image(resolution=300).original
#             text = pytesseract.image_to_string(pil_image, config=custom_config)

#             if not text:
#                 continue

#             for line in text.splitlines():
#                 # Check if line matches any start phrase
#                 if not start_found and any(start.lower() in line.lower() for start in q_starts):
#                     start_found = True
#                     continue  # skip the line containing start phrase

#                 # Check if line matches any end phrase
#                 if start_found and any(end.lower() in line.lower() for end in q_ends):
#                     end_found = True
#                     break

#                 if start_found:
#                     lines_between.append(line)

#             if end_found:
#                 break

#     if not start_found:
#         return [f"Start question not found:{q_starts[0]}"]
#     if not end_found:
#         return None
#     if not lines_between:
#         return {"error": "No content found between start and end questions."}

#     # ## #@ print("#######",lines_between)
#     output_rows = []
#     for line in lines_between:
#         output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

#     final_3 = []
#     final_4 = []
#     for f in output_rows:
#         if len(f) == 3:
#             final_3.append(f)
#         elif len(f) == 4:
#             final_4.append(f)

#     keys = [
#         "Category",
#         "FY 2024-25(Current Financial Year)",
#         "FY 2023-24(Previous Financial Year)"
#     ]

#     keys_3 = [
#         "S.no",
#         "Category",
#         "FY 2024-25(Current Financial Year)",
#         "FY 2023-24(Previous Financial Year)"
        
#     ]
    
#     myout = []
#     for row in output_rows:
#         data = dict(zip(keys, row))
#         myout.append(data)

#     if len(final_3) > len(final_4):
#         for row in final_3:
#             data = dict(zip(keys, row))
#             myout.append(data)
#     elif len(final_4) > len(final_3):
#         for row in final_4:
#             data = dict(zip(keys_3, row))
#             myout.append(data)
#     else:
#         return "\n".join(lines_between)



#     if not myout:
#         return "Not Applicable"


#     return myout

#@ print(Gross_wages_paid("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")





def  Do_you_have_a_focal_point(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Do you have a focal point (Individual/ Committee)"
        question_2="Do you have a focal point (Individual/ Committee)"
        question_3="issues caused or contributed to by the business"
        for i, page in enumerate(pdf.pages[-30:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Describe the internal mechanisms in place to redress grievances related to human rights issues"
                sec_quest_2="Describe the internal mechanisms " 
                sec_quest_3="grievances related to human rights issues"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Do_you_have_a_focal_point("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def Describe_the_internal_mechanisms(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Describe the internal mechanisms in place to redress "
        question_2="Describe the internal mechanisms in place"
        question_3="grievances related to human rights issues"
        for i, page in enumerate(pdf.pages[-28:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Number of Complaints on the following made by employees and workers"
                sec_quest_2="Number of Complaints on the following made by employees and workers" 
                sec_quest_3="following made by employees and workers"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Describe_the_internal_mechanisms("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Number_of_Complaints(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Number of Complaints on the following made by employees and workers",
        "by employees and workers"
        "Number of Complaints on the"
    ]
    q_ends = [
        "Complaints filed under the Sexual Harassment of Women at Workplace",
        "Complaints filed under the Sexual Harassment",
        "2013, in the following format"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_7 = []
    final_8 = []
    for f in output_rows:
        if len(f) == 7:
            final_7.append(f)
        elif len(f) == 8:
            final_8.append(f)

    keys = [
        "Category",
        "FY 2024-25Current Financial Year (Filed during the year)",
        "FY 2024-25Current Financial Year (Pending resolution at the end of year)",
        "FY 2024-25Current Financial Year (Remarks)",
        "FY 2023-24Previous Financial Year (Filed during the year)",
        "FY 2023-24Previous Financial Year (Pending resolution at the end of year)",
        "FY 2023-24Previous Financial Year (Remarks)"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "FY 2024-25Current Financial Year (Filed during the year)",
        "FY 2024-25Current Financial Year (Pending resolution at the end of year)",
        "FY 2024-25Current Financial Year (Remarks)",
        "FY 2023-24Previous Financial Year (Filed during the year)",
        "FY 2023-24Previous Financial Year (Pending resolution at the end of year)",
        "FY 2023-24Previous Financial Year (Remarks)"
    ]
    
    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_7) > len(final_8):
        for row in final_7:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_8) > len(final_7):
        for row in final_8:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Number_of_Complaints("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Complaints_filed_under(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Complaints filed under the Sexual Harassment of Women at Workplace",
        "Complaints filed under the Sexual Harassment",
        "Act, 2013, in the following format"
    ]
    q_ends = [
        "Mechanisms to prevent adverse consequences to the complainant in discrimination",
        "Mechanisms to prevent adverse consequences",
        "discrimination and harassment cases"
    ]
    keys = [
        "Category",
        "FY 2024-25(Current Financial Year)",
        "FY 2023-24(Previous Financial Year)"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "FY 2024-25(Current Financial Year)",
        "FY 2023-24(Previous Financial Year)"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
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
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

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

#@ print(Complaints_filed_under("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def Mechanisms_prevent(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Mechanisms to prevent adverse consequences to the complainant in discrimination"
        question_2="Mechanisms to prevent adverse consequences "
        question_3="discrimination and harassment cases"
        for i, page in enumerate(pdf.pages[-30:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Do human rights requirements form part of your business agreements and contracts"
                sec_quest_2="Do human rights requirements" 
                sec_quest_3="your business agreements and contracts"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Mechanisms_prevent("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Do_human_rights_requirements(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Do human rights requirements form part of your business agreements",
        "Do human rights requirements form",
        "business agreements and contracts"
    ]
    q_ends = [
        "Percentage of your plants & offices that were assessed (by entity or statutory authorities or third parties)",
        "Percentage of your plants"
        "authorities or third parties",
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"


#@ print(Do_human_rights_requirements("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Assessments(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
    "Assessments for the year",
    "Assessments for the year",
    "Assessments"
    ]
    q_ends = [
        "Provide details of any corrective actions taken or underway",
        "Provide details of any corrective actions",
        "concerns arising from the assessments at Question 9 above"
    ]
    keys = [
        "Category",
        "% of your plants and offices that were assessed (by entity or statutory authorities or third parties)"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "% of your plants and offices that were assessed (by entity or statutory authorities or third parties)"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
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


    
    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

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

#@ print(Assessments("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Provide_details_of_any_corrective(pdf_path,):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Provide details of any corrective actions taken or underway to"
        question_2="Provide details of any corrective actions"
        question_3="assessments at Question 9 above"
        for i, page in enumerate(pdf.pages[-25:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of a business process being modified / introduced"
                sec_quest_2="Details of a business process " 
                sec_quest_3="addressing human rights grievances/complaints"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Provide_details_of_any_corrective("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Details_of_a_business_process(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Details of a business process being modified"
        question_2="Details of a business process being modified / introduced"
        question_3="result of addressing human rights grievances/complaints"
        for i, page in enumerate(pdf.pages[-28:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of the scope and coverage of any Human rights due-diligence conducted"
                sec_quest_2="Details of the scope and coverage " 
                sec_quest_3="Human rights due-diligence conducted"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Details_of_a_business_process("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def Details_of_the_scope(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Details of the scope and coverage of any Human"
        question_2="Details of the scope and coverage"
        question_3="Human rights due-diligence conducted"
        for i, page in enumerate(pdf.pages[-28:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?"
                sec_quest_2="Is the premise/office of the entity accessible to differently" 
                sec_quest_3="Rights of Persons with Disabilities Act, 2016"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Details_of_the_scope("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def Is_the_premise(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        ## #@ print("file opend")
        question="Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the "
        question_2="Is the premise/office of the entity accessible"
        question_3=" Rights of Persons with Disabilities Act, 2016?"
        for i, page in enumerate(pdf.pages[-28:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details on assessment of value chain partners"
                sec_quest_2="Details on assessment of value chain partners" 
                sec_quest_3="Details on assessment of"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Is_the_premise("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Details_on_assessment_value_chain(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details on assessment of value chain partners",
        "Details on assessment",
        "value chain partners"
    ]
    q_ends = [
        "Provide details of any corrective actions taken or underway",
        "Provide details of any corrective actions",
        "from the assessments at Question 4 above"
    ]


    keys = [
        "Category",
        "% of value chain partners (by value of business done with such partners) that were assessed"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "% of value chain partners (by value of business done with such partners) that were assessed"   
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2:]:
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

    # ## #@ print("#######",lines_between)
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

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

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

#@ print(Details_on_assessment_value_chain("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")






def Provide_details_of_any(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        ## #@ print("file opend")
        question="Provide details of any corrective actions taken or underway to address significant risks"
        question_2="Provide details of any corrective actions taken"
        question_3="arising from the assessments at Question 4 above"
        for i, page in enumerate(pdf.pages[-28:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Principle 6"
                sec_quest_2="Businesses should respect and make efforts to protect and restore the environment" 
                sec_quest_3="Businesses should respect and make"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #@ print("****q3")
                        list=lines[i:]
                        break
                #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Provide_details_of_any("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




# def Describe_the_internal_mechanisms(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # ## #@ print("file opend")
        question="Describe the internal mechanisms in place to redress "
        question_2="Describe the internal mechanisms in place"
        question_3="grievances related to human rights issues"
        for i, page in enumerate(pdf.pages[-28:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # ## #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Number of Complaints on the following made by employees and workers"
                sec_quest_2="Number of Complaints on the following made by employees and workers" 
                sec_quest_3="following made by employees and workers"
                list=[]     
                for i, line in enumerate(lines):
                    # ## #@ print(i,line)
                    if question.lower() in line.lower():
                        # ## #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # ## #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # ## #@ print("****q3")
                        list=lines[i:]
                        break
                # ## #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # ## #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # ## #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # ## #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## #@ print("finallist",finallist)
                return finallist                       

#@ print(Describe_the_internal_mechanisms("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


