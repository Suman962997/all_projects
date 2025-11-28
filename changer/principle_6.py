import pdfplumber
import pytesseract
from PIL import Image
import io
import re

                                ###### PRINCIPLE VI #######
                                

def  Details_of_total_energy(pdf_file):
    #@ print("PRINCIPLE 6")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of total energy consumption (in Joules or multiples) ",
        "in Joules or multiples",
        "and energy intensity, in the following format"

    ]
    q_ends = [
        "Does the entity have any sites / facilities identified as designated consumers",
        "facilities identified as designated consumers",
        "PAT scheme have been achieved"
    ]
    keys = [
        "Parameter",
        "FY 2024-25(Current Financial Year)",
        "FY 2023-24(Previous Financial Year)"
    ]

    keys_3 = [
        "S.no",
        "Parameter",
        "FY 2024-25(Current Financial Year)",
        "FY 2023-24(Previous Financial Year)"
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

#@ print(Details_of_total_energy("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def Does_the_entity_have_any_sites(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        ### #@ print("file opend")
        question="Does the entity have any sites / facilities identified as designated"
        question_2="Does the entity have any sites"
        question_3="Scheme of the Government of India"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                ### #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ### #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Provide details of the following disclosures related to water, in the following format"
                sec_quest_2="Provide details of the following disclosures" 
                sec_quest_3="related to water, in the following format"
                list=[]     
                for i, line in enumerate(lines):
                    # ### #@ print(i,line)
                    if question.lower() in line.lower():
                        ### #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        ### #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        ### #@ print("****q3")
                        list=lines[i:]
                        break
                # ### #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ### #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ### #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        ### #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        ### #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ### #@ print("finallist",finallist)
                return finallist                       

#@ print(Does_the_entity_have_any_sites("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Provide_details_of_the_following(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details of the following disclosures related to water, in the following format",
        "Provide details of the following disclosures"
        "water, in the following format"

    ]
    q_ends = [
        "Provide the following details related to water discharged",
        "Provide the following details related",
        "related to water discharged"        
    ]

    keys = [
        "Parameter",
        "FY 2023-2024",
        "FY 2022-2023"
    ]

    keys_3 = [
        "S.no",
        "Parameter",
        "FY 2023-2024",
        "FY 2022-2023"
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

#@ print(Provide_details_of_the_following("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Provide_the_following_details(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide the following details related to Water Discharged",
        "Provide the following details",
        "related to Water Discharged"

    ]
    q_ends = [
        "Has the entity implemented a mechanism for Zero Liquid Discharge? If yes",
        "Has the entity implemented a mechanism for Zero Liquid Discharge",
        "coverage and implementation"
        
    ]
    keys = [
        "Parameter",
        "FY 2023-2024",
        "FY 2022-2023"
    ]

    keys_3 = [
        "S.no",
        "Parameter",
        "FY 2023-2024",
        "FY 2022-2023"
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

#@ print(Provide_the_following_details("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")




def Has_the_entity_implemented(pdf_path,):
    with pdfplumber.open(pdf_path) as pdf:
        ### #@ print("file opend")
        question="Has the entity implemented a mechanism for Zero Liquid Discharge"
        question_2="Zero Liquid Discharge"
        question_3="coverage and implementation"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                ### #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ### #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Please provide details of air emissions (other than GHG emissions) by the entity, in the following format"
                sec_quest_2="Please provide details of air emissions" 
                sec_quest_3="other than GHG emissions"
                list=[]     
                for i, line in enumerate(lines):
                    # ### #@ print(i,line)
                    if question.lower() in line.lower():
                        ### #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        ### #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        ### #@ print("****q3")
                        list=lines[i:]
                        break
                # ### #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ### #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ### #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        ### #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        ### #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ### #@ print("finallist",finallist)
                return finallist                       

#@ print(Has_the_entity_implemented("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Please_provide_details(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Please provide details of air emissions (other than GHG emissions) by the entity, in the following format",
        "other than GHG emissions",
        "air emissions"


    ]
    q_ends = [
        "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity",
        "Scope 1 and Scope 2 emissions",
        "greenhouse gas emissions"
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
        "Parameters",
        "Please specify unit",
        "FY 2023 - 2024",
        "FY 2022 – 2023"
    ]

    keys_3 = [
        "S.no",
        "Parameters",
        "Please specify unit",
        "FY 2023 - 2024",
        "FY 2022 – 2023"
    ]
    
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

#@ print(Please_provide_details("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Provide_details_of_greenhouse(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity",
        "Scope 1 and Scope 2 emissions",
        "greenhouse gas emissions"

    ]
    q_ends = [
        "Does the entity have any project related to reducing Green House Gas emission? If Yes, then provide details",
        "reducing Green House Gas emission",
        "Does the entity have any project"
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
        "Parameters",
        "Please specify unit",
        "FY 2023 - 2024",
        "FY 2022 – 2023"
    ]

    keys_3 = [
        "S.no",
        "Parameters",
        "Please specify unit",
        "FY 2023 - 2024",
        "FY 2022 – 2023"
    ]
    
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

#@ print(Provide_details_of_greenhouse("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Does_the_entity_have_any_project(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Does the entity have any project related to reducing Green House Gas emission? If Yes, then provide details",
        "reducing Green House Gas emission",
        "Does the entity have any project"
    ]
    q_ends = [
        "Provide details related to waste management by the entity",
        "Provide details related to waste management",
        "entity, in the following format"
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

    ## #@ print("#######",lines_between)
    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        None
#@ print(Does_the_entity_have_any_project("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Provide_details_related(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details related to waste management by the entity, in the following format",
        "Provide details related to waste management by the entity",
        "related to waste management by the entity"

    ]
    q_ends = [
        "Briefly describe the waste management practices adopted in your establishments",
        "Briefly describe the waste management practices",
        "practices adopted to manage such wastes"        
    ]

    keys = [
        "Total Waste generated (in metric tonnes)",
        "FY 2023 - 2024",
        "FY 2022 – 2023"
    ]

    keys_3 = [
        "S.no",
        "Total Waste generated (in metric tonnes)",
        "FY 2023 - 2024",
        "FY 2022 – 2023"   
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

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_3 = []
    final_4 = []
    for f in output_rows:
        if len(f) ==3:
            final_3.append(f)
        elif len(f) ==4:
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

#@ print(Provide_details_related("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Briefly_describe_the_waste(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        ### #@ print("file opend")
        question="Briefly describe the waste management practices adopted in your establishments"
        question_2="Briefly describe the waste management practices adopted"
        question_3="products and processes and the practices"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                ### #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ### #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries,"
                sec_quest_2="If the entity has operations/offices in/around ecologically sensitive areas" 
                sec_quest_3="required, please specify details in the following"
                list=[]     
                for i, line in enumerate(lines):
                    # ### #@ print(i,line)
                    if question.lower() in line.lower():
                        ### #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        ### #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        ### #@ print("****q3")
                        list=lines[i:]
                        break
                # ### #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ### #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ### #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        ### #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        ### #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ### #@ print("finallist",finallist)
                return finallist                       

#@ print(Briefly_describe_the_waste("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  If_the_entity_has_operations(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere",
        "If the entity has operations/offices in/around ecologically sensitive areas",
        "required, please specify details in the following"


    ]
    q_ends = [
        "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws",
        "Details of environmental impact assessments of projects undertaken",
        "current financial year"
    ]

    keys = [
        "Location of operations/offices",
        "Type of operations",
        "Whether the conditions of environmental approval / clearance are being complied with? (Y/N) If no, the reasons thereof and corrective action taken, if any"
    ]

    keys_3 = [
        "S.no",
        "Location of operations/offices",
        "Type of operations",
        "Whether the conditions of environmental approval / clearance are being complied with? (Y/N) If no, the reasons thereof and corrective action taken, if any"
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

#@ print(If_the_entity_has_operations("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Details_of_environmental(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws",
        "Details of environmental impact assessments of projects undertaken",
        "current financial year"

    ]
    q_ends = [
        "Is the entity compliant with the applicable environmental",
        "Prevention and Control of Pollution) Act",
        "Environment protection act and rules thereunder"        
    ]

    keys = [
        "Name and brief details of project",
        "EIA Notification No",
        "Date",
        "Whether conducted by independent external agency (Yes / No)",
        "Results communicated in public domain(Yes / No)",
        "Relevant Web link"
    ]

    keys_3 = [
        "S.no",
        "Name and brief details of project",
        "EIA Notification No",
        "Date",
        "Whether conducted by independent external agency (Yes / No)",
        "Results communicated in public domain(Yes / No)",
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

#@ print(Details_of_environmental("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Is_the_entity_compliant(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Is the entity compliant with the applicable environmental",
        "Prevention and Control of Pollution) Act",
        "Environment protection act and rules thereunder"

    ]
    q_ends = [
    "LEADERSHIP INDICATORS",
    "Water withdrawal, consumption and discharge in areas of water stress",
    "areas of water stress"        
    ]

    keys = [
        "Specify the law / regulation / guidelines which was not complied with",
        "Provide details of the non-compliance",
        "Any fines / penalties / action taken by regulatory agencies such as pollution control boards or by courts",
        "Corrective action taken, if any"
        
    ]

    keys_3 = [
        "S.no",
        "Specify the law / regulation / guidelines which was not complied with",
        "Provide details of the non-compliance",
        "Any fines / penalties / action taken by regulatory agencies such as pollution control boards or by courts",
        "Corrective action taken, if any"
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

#@ print(Is_the_entity_compliant("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


# Leadership Indicators



def  Water_withdrawal(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Water withdrawal, consumption and discharge in areas of water stress",
        "Water withdrawal, consumption",
        "water stress (in kilo liters)"

    ]
    q_ends = [
        "Please provide details of total Scope 3 emissions and its intensity",
        "details of total Scope 3",
        "emissions and its intensity"        
    ]
    keys = [
        "Parameter",
        "FY 2023-2024",
        "FY 2022-2023"
    ]

    keys_3 = [
        "S.no",
        "Parameter",
        "FY 2023-2024",
        "FY 2022-2023"
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

    ## #@ print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_3 = []
    final_4 = []
    for f in output_rows:
        if len(f) ==3:
            final_3.append(f)
        elif len(f) ==4:
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

#@ print(Water_withdrawal("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")





def  Please_provide_details(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Please provide details of total Scope 3 emissions",
        "Please provide details of total Scope 3",
        "Scope 3 emissions & its intensity"

    ]
    q_ends = [
        "With respect to the ecologically sensitive areas reported",
        "With respect to the ecologically",
        "provide details of significant"
    ]
    keys = [
        "Parameter",
        "Unit",
        "FY 2023-24",
        "FY 2022-23"
        
    ]

    keys_3 = [
        "S.no",
        "Parameter",
        "Unit",
        "FY 2023-2024",
        "FY 2022-2023"
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

#@ print(Please_provide_details("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")






def  With_respect_to_the_ecologically(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "With respect to the ecologically sensitive areas reported",
        "With respect to the ecologically",
        "Essential Indicators above, provide details of significant"
    ]
    q_ends = [
        "If the entity has undertaken any specific initiatives or used innovative technology or solutions to",
        "used innovative technology or solutions",
        "please provide details of the same as well as outcome"
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

    ## #@ print("#######",lines_between)

    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        None
#@ print(With_respect_to_the_ecologically("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")




def  If_the_entity_has_undertaken(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource",
        "innovative technology or solutions to improve resource",
        "please provide details of the same as well as outcome"


    ]
    q_ends = [
        "Does the entity have a business continuity and disaster management plan",
        "have a business continuity and disaster"
        "Give details in 100 words/ web link"        
    ]

    keys = [
        "Initiative undertaken",
        "Details of the initiative (Web-link, if any, may be provided along-with summary)",
        "Outcome of the initiative"

    ]

    keys_3 = [
        "S.no",
        "Initiative undertaken",
        "Details of the initiative (Web-link, if any, may be provided along-with summary)",
        "Outcome of the initiative"
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

#@ print(If_the_entity_has_undertaken("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Does_the_entity_have_a_business(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Does the entity have a business continuity and disaster management plan",
        "have a business continuity and disaster"
        "Give details in 100 words/ web link"
    ]
    q_ends = [
        "Disclose any significant adverse impact to the environment, arising from the value chain of the entity",
        "Disclose any significant adverse impact to the environment",
        "have been taken by the entity in this regard"
        
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

    ## #@ print("#######",lines_between)

    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        None

#@ print(Does_the_entity_have_a_business("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Disclose_any_significant(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Disclose any significant adverse impact to the environment, arising from the value chain of the entity",
        "Disclose any significant adverse impact to the environment",
        "have been taken by the entity in this regard"
    ]
    q_ends = [
        "Percentage of value chain partners (by value of business done with such partners)",
        "by value of business done with such partners",
        "that were assessed for environmental impacts"
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

    ## #@ print("#######",lines_between)

    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        None

#@ print(Disclose_any_significant("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Percentage_of_value_chain(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage of value chain partners (by value of business done with such partners)",
        "by value of business done with such partners",
        "that were assessed for environmental impacts"
    ]
    q_ends = [
        "PRINCPLE 7",
        "BUSINESSES, WHEN ENGAGING IN INFLUENCING PUBLIC",
        "Number of affiliations with trade and industry chambers/ associations"
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

    ## #@ print("#######",lines_between)

    if lines_between:
        answer_text = "\n".join(lines_between)
        return answer_text
    else:
        None

#@ print(Percentage_of_value_chain("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

