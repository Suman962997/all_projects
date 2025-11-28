import pdfplumber
import pytesseract
from PIL import Image
import io
import re

                                ###### PRINCIPLE VIII #######

def  Details_of_Social_Impact(pdf_file):
    #@ print("PRINCIPLE 8")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of Social Impact Assessments (SIA) of projects undertaken by the entity",
        "Details of Social Impact Assessments",
        "the current financial year"
    ]
    q_ends = [
        "Provide information on project(s) for which ongoing Rehabilitation and Resettlement",
        "Provide information on project",
        "entity, in the following format"
    ]
    keys = [
        "Name and brief details of project",
        "SIA Notification No.",
        "Date of notification",
        "Whether conducted by independent external agency (Yes / No)",
        "Results communicated in public domain (Yes / No)",
        "Relevant Web link"
    ]
    keys_3 = [
        "S.No",
        "Name and brief details of project",
        "SIA Notification No.",
        "Date of notification",
        "Whether conducted by independent external agency (Yes / No)",
        "Results communicated in public domain (Yes / No)",
        "Relevant Web link"
    ]


    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2]:
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

    # # #@ print("#######",lines_between)
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
    # for row in final_5:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_7) > len(final_6):
        for row in final_7:
            data = dict(zip(keys, row))
            myout.append(data)
    else:
        for row in output_rows:
            data = dict(zip(keys_3, row))
            myout.append(data)


    if not myout:
        return "Not Applicable"


    return myout

#@ print(Details_of_Social_Impact("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Provide_information_on_project(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide information on project(s) for which ongoing",
        "Provide information on project",
        "Rehabilitation and Resettlement"
        
    ]
    q_ends = [
        "Describe the mechanisms to receive",
        "receive and redress grievances",
        "grievances of the community"
    ]
    keys = [
        "Name of Project for which R&R is ongoing",
        "State",
        "District",
        "No. of Project Affected Families (PAFs)",
        "% of PAFs covered by R&R",
        "Amounts paid to PAFs in the FY (In INR)"

    ]
    keys_3 = [
        "S.No",
        "Name of Project for which R&R is ongoing",
        "State",
        "District",
        "No. of Project Affected Families (PAFs)",
        "% of PAFs covered by R&R",
        "Amounts paid to PAFs in the FY (In INR)"

    ]


    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2]:
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

    # # #@ print("#######",lines_between)
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
    # for row in final_5:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_7) > len(final_6):
        for row in final_7:
            data = dict(zip(keys, row))
            myout.append(data)
    else:
        for row in output_rows:
            data = dict(zip(keys_3, row))
            myout.append(data)


    if not myout:
        return "Not Applicable"


    return myout

#@ print(Provide_information_on_project("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Describe_the_mechanisms_to_receive(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Describe the mechanisms to receive and redress grievances of the community",
        "Describe the mechanisms to receive",
        "redress grievances of the community"
    ]
    q_ends = [
        "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
        "inputs to total inputs by value",
        "sourced from suppliers"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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

    # #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else :
        return "Not Applicable"

#@ print(Describe_the_mechanisms_to_receive("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Percentage_of_input_material(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
        "inputs to total inputs by value",
        "sourced from suppliers"
    ]
    q_ends = [
        "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers",
        "Disclose wages paid to persons employed",
        "following locations, as % of total wage cost"
    ]
    keys = [
        "Particulars",
        "FY 2023-24 (Current Financial Year)",
        "FY 2022-23 (Previous Financial year)"

    ]


    keys_3 = [
        "S.No.",
        "Particulars",
        "FY 2023-24 (Current Financial Year)",
        "FY 2022-23 (Previous Financial year)"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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

    # # #@ print("#######",lines_between)
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
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(keys, row))
            myout.append(data)

    elif len(final_4) > len(final_3):
        for row in final_4:
            data = dict(zip(keys_3, row))
            myout.append(data)


    if not myout:
        return "Not Applicable"


    return myout

#@ print(Percentage_of_input_material("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Job_creation_in_smaller_towns(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Job creation in smaller towns",
        "Job creation",
        "of total wage cost"
    ]
    q_ends = [
        "Provide details of actions taken to mitigate any negative",
        "Provide details of actions",
        "Essential Indicators above"
    ]
    keys = [
            "Location",
            "FY 2024-25Current Financial Year",
            "FY 2023-24Previous Financial Year"
    ]

    keys_3 = [
            "S.No.",
            "Location",
            "FY 2024-25Current Financial Year",
            "FY 2023-24Previous Financial Year"
    ]
    

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2]:
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

    # # #@ print("#######",lines_between)
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
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

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
#@ print(Job_creation_in_smaller_towns("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Provide_details_of_actions_taken(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact",
        "any negative social impacts"
        "1 of Essential Indicators above"
    ]
    q_ends = [
        "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts",
        "your entity in designated",
        "government bodies"        
    ]

    keys = [
        "Details of negative social impact identified",
        "Corrective action taken"
    ]

    keys_4 = [
        "Sl.No",
        "Details of negative social impact identified",
        "Corrective action taken"        
    ]
    
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2]:
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

    # # #@ print("#######",lines_between)
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
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_2) > len(final_3):
        for row in final_2:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_3) > len(final_2):
        for row in final_3:
            data = dict(zip(keys_4, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout
#@ print(Provide_details_of_actions_taken("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Provide_the_following_information(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide the following information on CSR projects undertaken by your entity in designated",
        "Provide the following information on CSR projects",
        "identified by government bodies"

    ]
    q_ends = [
        "Do you have a preferential procurement policy where you give preference",
        "Do you have a preferential procurement policy",
        "vulnerable groups"
    ]
    keys = [
        "State",
        "Aspirational District",
        "Amount Spent in INR"   
    ]
    keys_3 = [
        "S.no",
        "State",
        "Aspirational District",
        "Amount Spent in INR"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:]:
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

    # #@ print("#######",lines_between)
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
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

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

#@ print(Provide_the_following_information("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Do_you_have_a_preferential(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Do you have a preferential procurement policy where you give preference",
        "Do you have a preferential procurement policy",
        "vulnerable groups"
    ]
    q_ends = [
        "Which marginalized /vulnerable groups do you procure",
        "Which marginalized",
        "vulnerable groups"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:]:
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

    # #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"
#@ print(Do_you_have_a_preferential("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  From_which_marginalized(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Which marginalized /vulnerable groups do you procure",
        "Which marginalized",
        "vulnerable groups"

    ]
    q_ends = [
        "What percentage of total procurement (by value) does it constitute",
        "What percentage of total procurement",
        "(by value) does it constitute"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:]:
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

    # #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"

#@ print(From_which_marginalized("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  What_percentage_of_total_procurement(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "What percentage of total procurement (by value) does it constitute",
        "What percentage of total procurement",
        "(by value) does it constitute"

    ]
    q_ends = [
        "Details of the benefits derived ",
        "properties owned or acquired",
        "based on traditional knowledge"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:]:
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

    # #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        return "Not Applicable"

#@ print(What_percentage_of_total_procurement("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Details_of_the_benefits_derived(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of the benefits derived and shared from the intellectual",
        "owned or acquired by your entity",
        "based on traditional knowledge:"

    ]
    q_ends = [
        "Details of corrective actions taken or underway",
        "adverse order in intellectual property",
        "traditional knowledge is involved"
                
    ]
    keys = [
        "Intellectual property based on traditional knowledge",
        "Owned/Acquired (Yes/No)",
        "Benefit Shared (Yes/No)",
        "Basis of calculating benefit share"
        

    ]
    keys_3 = [
        "S.no",
        "Intellectual property based on traditional knowledge",
        "Owned/Acquired (Yes/No)",
        "Benefit Shared (Yes/No)",
        "Basis of calculating benefit share"
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:]:
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

    # #@ print("#######",lines_between)
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

#@ print(Details_of_the_benefits_derived("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Details_of_corrective_actions_taken(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of corrective actions taken or underway",
        "adverse order in intellectual property related",
        "usage of traditional knowledge is involved"

    ]
    q_ends = [
        "Details of beneficiaries of CSR Projects",
        "Details of beneficiaries",
        "CSR Projects"
                
    ]
    keys = [
        "Name of authority",
        "Brief of the Case",
        "Corrective action taken"
    ]
    keys_3 = [
        "S.no",
        "Name of authority",
        "Brief of the Case",
        "Corrective action taken"
        
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:]:
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

    # #@ print("#######",lines_between)
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

#@ print(Details_of_corrective_actions_taken("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Details_of_beneficiaries(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of beneficiaries of CSR Projects",
        "Details of beneficiaries",
        "CSR Projects"

    ]
    q_ends = [
        "PRINCIPLE 9",
        "Businesses should engage",
        "consumers in a responsible manner"
    ]
    keys = [
        "CSR Project",
        "No. of persons benefited from CSR Projects",
        "% of beneficiaries from vulnerable and marginalized groups"
    ]
    keys_3 = [
        "S.no",
        "CSR Project",
        "No. of persons benefited from CSR Projects",
        "% of beneficiaries from vulnerable and marginalized groups"
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:-2]:
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

    # #@ print("#######",lines_between)
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

#@ print(Details_of_beneficiaries("C:/Users/coda/Documents/deigeo.pdf"))
#@ print("************")
