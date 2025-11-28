import pdfplumber
import pytesseract
from PIL import Image
import re



                            #  PRINCIPLE III 
                         
                        
def  well_being_of_employees(pdf_file):
    print("PRINCIPLE 3")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of measures for the well-being of employees",
        "well-being of employees"
        "Details of measures for the",

    ]
    q_ends = [
        "Details of measures for the well-being of workers",
        "well-being of workers"
        "Details of measures for the",
    ]


    keys = [
        "Category",
        "Total (A)",
        "Health insurance (Number (B))",
        "Health insurance (% (B / A))",
        "Accident insurance (Number (C))",
        "Accident insurance (% (C / A))",
        "Maternity Benefits (Number (D))",
        "Maternity Benefits (% (D / A))",
        "Paternity Benefits (Number (E))",
        "Paternity Benefits (% (E / A))",
        "Day Care Facilities (Number (F))",
        "Day Care Facilities (% (F / A))"

    ]

    keys_3 = [
        "S.no",
        "Category",
        "Total (A)",
        "Health insurance (Number (B))",
        "Health insurance (% (B / A))",
        "Accident insurance (Number (C))",
        "Accident insurance (% (C / A))",
        "Maternity Benefits (Number (D))",
        "Maternity Benefits (% (D / A))",
        "Paternity Benefits (Number (E))",
        "Paternity Benefits (% (E / A))",
        "Day Care Facilities (Number (F))",
        "Day Care Facilities (% (F / A))"

    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_12 = []
    final_13 = []
    for f in output_rows:
        if len(f) == 12:
            final_12.append(f)
        elif len(f) == 13:
            final_13.append(f)

    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_12) > len(final_13):
        for row in final_12:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_13) > len(final_12):
        for row in final_13:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(well_being_of_employees("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

def  well_being_of_Workers(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of measures for the well-being of workers",
        "Details of measures for the",
        "well-being of workers"

    ]
    q_ends = [
        "Details of retirement benefits, for Current",
        "Details of retirement",
        "Current FY and Previous"
    ]
    keys = [
        "Category",
        "Total (A)",
        "Health insurance (Number (B))",
        "Health insurance (% (B / A))",
        "Accident insurance (Number (C))",
        "Accident insurance (% (C / A))",
        "Maternity Benefits (Number (D))",
        "Maternity Benefits (% (D / A))",
        "Paternity Benefits (Number (E))",
        "Paternity Benefits (% (E / A))",
        "Day Care Facilities (Number (F))",
        "Day Care Facilities (% (F / A))"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "Total (A)",
        "Health insurance (Number (B))",
        "Health insurance (% (B / A))",
        "Accident insurance (Number (C))",
        "Accident insurance (% (C / A))",
        "Maternity Benefits (Number (D))",
        "Maternity Benefits (% (D / A))",
        "Paternity Benefits (Number (E))",
        "Paternity Benefits (% (E / A))",
        "Day Care Facilities (Number (F))",
        "Day Care Facilities (% (F / A))"
        ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_12 = []
    final_13 = []
    for f in output_rows:
        if len(f) == 12:
            final_12.append(f)
        elif len(f) == 13:
            final_13.append(f)




    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_12) > len(final_13):
        for row in final_12:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_13) > len(final_12):
        for row in final_13:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(well_being_of_Workers("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Details_retirement_benefits(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of retirement benefits, for Current FY and Previous Financial Year",
        "Details of retirement benefits",
        "Current FY and Previous Financial Year"

    ]
    q_ends = [
        "Accessibility of workplaces",
        "Accessibility",
        "workplaces"
    ]

    keys = [
        "Benefits",
        "No. of employees covered as a % of total employees",
        "No. of workers covered as a % of total workers",
        "Deducted and deposited with the authority(Y/N/N.A.)",
        "No. of employees covered as a % of total employees",
        "No. of workers covered as a % of total worker",
        "Deducted and deposited with the authority(Y/N/N.A.)"
    ]

    keys_3 = [
        "S.no",
        "Benefits",
        "No. of employees covered as a % of total employees",
        "No. of workers covered as a % of total workers",
        "Deducted and deposited with the authority(Y/N/N.A.)",
        "No. of employees covered as a % of total employees",
        "No. of workers covered as a % of total worker",
        "Deducted and deposited with the authority(Y/N/N.A.)"
        ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_7 = []
    final_8 = []
    for f in output_rows:
        if len(f) == 7:
            final_7.append(f)
        elif len(f) == 8:
            final_8.append(f)


    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

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

#@ print(Details_retirement_benefits("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def  Accessibility_of_workplaces(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Accessibility of workplaces"
        question_2="Accessibility of workplaces"
        question_3="Accessibility of workplaces"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities"
                sec_quest_2="Does the entity have an equal opportunity" 
                sec_quest_3=" Rights of Persons with Disabilities Act, 2016?"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(Accessibility_of_workplaces("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

def  Does_the_entity_have_an_equal(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities",
        "equal opportunity policy",
        "web-link to the policy"

    ]
    q_ends = [
        "Return to work and Retention rates of permanent",
        "Return to work and Retention",
        "workers that took parental leave"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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
#@ print(Does_the_entity_have_an_equal("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def  Return_to_work(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Return to work and Retention rates of permanent employees",
        "Return to work and Retention rates",
        "workers that took parental leave"

    ]
    q_ends = [
        "Is there a mechanism available to receive and redress grievances",
        "receive and redress grievances",
        "categories of employees"
    ]
    
    keys = [
    "Gender",
    "Return to work rate",
    "Retention rate",
    "Return to work rate",
    "Retention rate"   
    ]

    keys_3 = [
    "S.no",
    "Gender",
    "Return to work rate",
    "Retention rate",
    "Return to work rate",
    "Retention rate"   


    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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
        return "Not Applicable"


    return myout

#@ print(Return_to_work("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Is_there_mechanism(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Is there a mechanism available to receive and redress grievances",
        "receive and redress grievances",
        "categories of employees"

    ]
    q_ends = [
        "Membership of employees and worker in association(s)",
        "Membership of employees and worker",
        "Unions recognised by the listed entity"
    ]

    keys = [
        "Particulars",
        "Yes/No(If Yes, then give details of the mechanism in brief)"
    ]

    keys_3 = [
        "S.no",
        "Particulars",
        "Yes/No(If Yes, then give details of the mechanism in brief)"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Is_there_mechanism("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Membership_of_employees(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Membership of employees and worker in association(s) or Unions",
        "Membership of employees and worker",
        "recognised by the listed entity"

    ]
    q_ends = [
        "Details of training given to employees and workers",
        "Details of training given to",
        "employees and workers"
        
    ]
    keys = [
        "category",
        "FY 2024-25(Current Financial Year)-(Total employees / workers in respective category(A))",
        "FY 2024-25(Current Financial Year)-(No. of employees / workers in respective category, who are part of association(s) or Union(B))",
        "FY 2024-25(Current Financial Year)-(% (B / A))",
        "FY 2023-24(Previous Financial Year)-(Total employees / workers in respective category(C))",
        "FY 2023-24(Previous Financial Year)-(No. of employees / workers in respective category, who are part of association(s) or Union(D))",
        "FY 2023-24(Previous Financial Year)-(% (D / C))"
        
        
    ]

    keys_3 = [
        "S.no",
        "category",
        "FY 2024-25(Current Financial Year)-(Total employees / workers in respective category(A))",
        "FY 2024-25(Current Financial Year)-(No. of employees / workers in respective category, who are part of association(s) or Union(B))",
        "FY 2024-25(Current Financial Year)-(% (B / A))",
        "FY 2023-24(Previous Financial Year)-(Total employees / workers in respective category(C))",
        "FY 2023-24(Previous Financial Year)-(No. of employees / workers in respective category, who are part of association(s) or Union(D))",
        "FY 2023-24(Previous Financial Year)-(% (D / C))"

    ]
    

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_7 = []
    final_8 = []
    for f in output_rows:
        if len(f) == 7:
            final_7.append(f)
        elif len(f) == 8:
            final_8.append(f)

    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

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

#@ print(Membership_of_employees("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Details_of_training(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of training given to employees and workers",
        "Details of training given to",
        "employees and workers"

    ]
    q_ends = [
        "Details of performance and career development reviews of employees and workers",
        "Details of performance and career",
        "reviews of employees and workers"
    ]

    keys = [
        "category",
        "Total (A)",
        "On Health and safety measures (No. (B))",
        "On Health and safety measures (% (B / A))",
        "On Skill upgradation (No. (C))",
        "On Skill upgradation (% (C / A))",
        "Total (D)",
        "On Health and safety measures (No. (E))",
        "On Health and safety measures (% (E / D))",
        "On Skill upgradation (No. (F))",
        "On Skill upgradation (% (F / D))"
        
    ]

    keys_3 = [
        "S.no",
        "category",
        "Total (A)",
        "On Health and safety measures (No. (B))",
        "On Health and safety measures (% (B / A))",
        "On Skill upgradation (No. (C))",
        "On Skill upgradation (% (C / A))",
        "Total (D)",
        "On Health and safety measures (No. (E))",
        "On Health and safety measures (% (E / D))",
        "On Skill upgradation (No. (F))",
        "On Skill upgradation (% (F / D))"
    ]
    

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_11 = []
    final_12 = []
    for f in output_rows:
        if len(f) == 11:
            final_11.append(f)
        elif len(f) == 12:
            final_12.append(f)


    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_11) > len(final_12):
        for row in final_11:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_12) > len(final_11):
        for row in final_12:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Details_of_training("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Details_of_performance(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of performance and career development reviews of employees and workers",
        "Details of performance and career",
        "reviews of employees and workers"

    ]
    q_ends = [
        "Health and safety management system",
        "Whether an occupational health and safety management system",
        "If yes, the coverage such system"
    ]
    keys = [
        "category",
        "FY 2024-25(Current Financial Year)-(Total (A))",
        "FY 2024-25(Current Financial Year)-(No. (B))",
        "FY 2024-25(Current Financial Year)-(% (B / A))",
        "FY 2023-24(Previous Financial Year)-(Total (C))",
        "FY 2023-24(Previous Financial Year)-(No. (D))",
        "FY 2023-24(Previous Financial Year)-(% (D / C))"        
    ]

    keys_3 = [
        "S.no",
        "category",
        "FY 2024-25(Current Financial Year)-(Total (A))",
        "FY 2024-25(Current Financial Year)-(No. (B))",
        "FY 2024-25(Current Financial Year)-(% (B / A))",
        "FY 2023-24(Previous Financial Year)-(Total (C))",
        "FY 2023-24(Previous Financial Year)-(No. (D))",
        "FY 2023-24(Previous Financial Year)-(% (D / C))"        

    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_7 = []
    final_8 = []
    for f in output_rows:
        if len(f) == 7:
            final_7.append(f)
        elif len(f) == 8:
            final_8.append(f)


    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

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

#@ print(Details_of_performance("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def a_Whether_an_occupational(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Health and safety management system"
        question_2="Health and safety management"
        question_3="Health and safety"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether an occupational health and safety management system has been implemented by the entity"
                sec_quest_2="Whether an occupational health and safety" 
                sec_quest_3="system has been implemented by the entity"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(a_Whether_an_occupational("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def b_What_are_the_processes(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="What are the processes used to identify work-related hazards and assess risks on a routine"
        question_2="What are the processes used to identify"
        question_3="risks on a routine and non-routine basis by the entity"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether you have processes for workers to report the work related hazards and to remove themselves from such risks"
                sec_quest_2="Whether you have processes for workers to report" 
                sec_quest_3=" the work related hazards and to remove themselves from such risks. (Y/N)"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(b_What_are_the_processes("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  c_Whether_you_have_processes_for_workers(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Whether you have processes for workers to report the work related hazards"
        question_2="Whether you have processes for workers to report the work"
        question_3=" related hazards and to remove themselves from such risks"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (Yes/ No)"
                sec_quest_2="Do the employees/ worker of the entity have" 
                sec_quest_3=" non-occupational medical and healthcare services"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(c_Whether_you_have_processes_for_workers("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  d_Do_the_employees_workers(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Do the employees/ worker of the entity have access to non-occupational"
        question_2="Do the employees/ worker of the entity"
        question_3="non-occupational medical and healthcare services"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of safety related incidents, in the following format"
                sec_quest_2="Details of safety related incidents" 
                sec_quest_3="incidents, in the following format"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(d_Do_the_employees_workers("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Details_safety_related(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of safety related incidents, in the following format",
        "Details of safety related incidents",
        "safety related incidents"

    ]
    q_ends = [
        "Describe the measures taken by the entity",
        "Describe the measures taken",
        "safe and healthy workplace"
    ]
    keys = [
        "Safety Incident/Number",
        "Category",
        "FY 2022",
        "FY 2021"
    ]

    keys_3 = [
        "S.no",
        "Safety Incident/Number",
        "Category",
        "FY 2022",
        "FY 2021"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

#@ print(Details_safety_related("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def Describe_the_measures (pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Describe the measures taken by the entity to ensure a safe and healthy work place"
        question_2="Describe the measures taken by the entity to ensure a safe and healthy workplace"
        question_3="safe and healthy work place"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Number of Complaints on the following made by employees and workers:"
                sec_quest_2="Number of Complaints on the " 
                sec_quest_3=" made by employees and workers:"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(Describe_the_measures("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Number_of_Complaints(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Number of Complaints on the following made by employees and workers",
        "Number of Complaints on the following",
        "made by employees and workers"
    ]
    q_ends = [
        "Assessments for the year",
        "Assessments for the year",
        "Assessments"
    ]

    keys = [
        "Category",
        "Filed during the year",
        "Pending resolution at the end of year",
        "Remarks",
        "Filed during the year",
        "Pending resolution at the end of year",
        "Remarks"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "Filed during the year",
        "Pending resolution at the end of year",
        "Remarks",
        "Filed during the year",
        "Pending resolution at the end of year",
        "Remarks"
        ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_7 = []
    final_8 = []
    for f in output_rows:
        if len(f) == 7:
            final_7.append(f)
        elif len(f) == 8:
            final_8.append(f)


    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_7) > len(final_8):
        for row in final_7:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_8) > len(final_7):
        for row in final_7:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Number_of_Complaints("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")






def  Assessments_for_the_year(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Assessments for the year",
        "Assessments",
        "Assessments for"
    ]
    q_ends = [
        "Provide details of any corrective action taken or underway to address safety-related",
        "address safety-related",
        "assessments of health & safety"
    ]
    keys = [
        "Category",
        "% of your plants and offices that were assessed (by entity or statutory authorities or third parties"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "% of your plants and offices that were assessed (by entity or statutory authorities or third parties"
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

#@ print(Assessments_for_the_year("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




def Provide_details_of_any_corrective(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Provide details of any corrective action taken or underway to address safety-related incidents (if any)"
        question_2="Provide details of any corrective action taken or underway to address safety-related"
        question_3=" arising from assessments of health & safety practices and working conditions"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity extend any life insurance or any compensatory Package in the event of death"
                sec_quest_2="Package in the event of death" 
                sec_quest_3="Does the entity extend any life insurance"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(Provide_details_of_any_corrective("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Does_the_entity_extend(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Does the entity extend any life insurance or any compensatory package"
        question_2="Does the entity extend any life insurance"
        question_3="event of death of (A) Employees (Y / N); (B) Workers (Y / N)"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners"
                sec_quest_2="Provide the measures undertaken by the entity to ensure" 
                sec_quest_3="have been deducted and deposited by the value chain partners"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print( Does_the_entity_extend("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def  Provide_the_measures_undertaken(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and "
        question_2="Provide the measures undertaken"
        question_3="deposited by the value chain partners"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide the number of employees / workers having"
                sec_quest_2="Provide the number of employees / workers" 
                sec_quest_3="family members have been placed in suitable employment"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(Provide_the_measures_undertaken("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def  Provide_the_number_of_employees(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide the number of employees",
        "workers having suffered high",
        "suitable employmen"

    ]
    q_ends = [
        "Does the entity provide transition assistance",
        "resulting from retirement",
        "termination of employment"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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

    final_5 = []
    final_6 = []
    for f in output_rows:
        if len(f) == 5:
            final_5.append(f)
        elif len(f) == 6:
            final_6.append(f)

    keys = [
        "Category",
        "Total no. of affected employees/ workers (FY 2024-25(Current Financial Year))",
        "Total no. of affected employees/ workers (FY 2023-24(Previous Financial Year))",
        "No. of employees/workers that are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment (FY 2024-25(Current Financial Year))",
        "No. of employees/workers that are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment (FY 2023-24(Previous Financial Year))"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "Total no. of affected employees/ workers (FY 2024-25(Current Financial Year))",
        "Total no. of affected employees/ workers (FY 2023-24(Previous Financial Year))",
        "No. of employees/workers that are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment (FY 2024-25(Current Financial Year))",
        "No. of employees/workers that are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment (FY 2023-24(Previous Financial Year))"
    ]
    
    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

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
        return "Not Applicable"


    return myout

#@ print(Provide_the_number_of_employees("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Does_the_entity_provide_transition(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting"
        question_2="Does the entity provide transition"
        question_3="retirement or termination of employment? (Yes/ No)"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details on assessment of value chain partners:"
                sec_quest_2="Details on assessment of value chain partners" 
                sec_quest_3="Details on assessment"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(Does_the_entity_provide_transition("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Details_on_assessment(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Details on assessment of value chain partners"
        question_2="Details on assessment"
        question_3="Details on assessment of value chain"
        for i, page in enumerate(pdf.pages[7:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health"
                sec_quest_2="Provide details of any corrective actions taken or underway to address significant risks" 
                sec_quest_3="arising from assessments of health"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("****q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #@ print("finallist",finallist)
                return finallist                       

#@ print(Details_on_assessment("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Provide_details_of_any_corrective_actions(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details of any corrective actions taken or underway to address significant",
        "underway to address significant",
        "working conditions of value chain partners"

    ]
    q_ends = [
        "PRINCIPLE 4",
        "Businesses should respect the interests",
        "responsive to all its stakeholders"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:-3]:
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
#@ print(Provide_details_of_any_corrective_actions("C:/Users/coda/Documents/siemens.pdf"))
#@ print("************")


