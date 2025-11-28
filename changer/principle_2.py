import pdfplumber
import pytesseract
from PIL import Image
import io
import re



                                #  PRINICIPLE II 



def  Percentage_of_R_and_D(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage of R&D and capital expenditure (capex) investments in specific",
        "Percentage of R&D and capital",
        "Percentage of R&D"

    ]
    q_ends = [
        "Does the entity have procedures in place for sustainable sourcing? (Yes/No)",
        "Does the entity have procedures",
        "place for sustainable sourcing"
    ]
    
    keys = [
            "Category",
            "FY 2024-25(Current Financial Year)",
            "FY 2023-24(Previous Financial Year)",
            "Details of improvements in environmental and social impacts",
    ]

    keys_3 = [
            "S.no",
            "Category",
            "FY 2024-25(Current Financial Year)",
            "FY 2023-24(Previous Financial Year)",
            "Details of improvements in environmental and social impacts",
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:-3]:
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

#@ print(Percentage_of_R_and_D("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Does_the_entity_have_procedures(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Does the entity have procedures in place for sustainable sourcing"
        question_2="Does the entity have procedures"
        question_3="for sustainable sourcing"
        for i, page in enumerate(pdf.pages[6:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If yes, what percentage of inputs were sourced sustainably?"
                sec_quest_2="If yes, what percentage of inputs " 
                sec_quest_3="If yes, what percentage"
                list=[]     
                for i, line in enumerate(lines):
                     #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                 #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      #("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 #("finallist",finallist)
                return "\n".join(finallist)                   

#@ print(Does_the_entity_have_procedures("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  b_If_yes_what_percentage(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="If yes, what percentage of inputs were sourced sustainably"
        question_2="If yes, what percentage"
        question_3="were sourced sustainably"
        for i, page in enumerate(pdf.pages[6:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Describe the processes in place to safely reclaim your products"
                sec_quest_2="Describe the processes in place" 
                sec_quest_3="products for reusing"
                list=[]     
                for i, line in enumerate(lines):
                     #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                 #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      #("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 #("finallist",finallist)
                return "\n".join(finallist)                   

#@ print(b_If_yes_what_percentage("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Describe_the_processes_in_place(pdf_path,):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Describe the processes in place to safely reclaim your products for reusing"
        question_2="Describe the processes in place"
        question_3="E-waste (c) Hazardous waste and (d) other waste."
        for i, page in enumerate(pdf.pages[6:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities"
                sec_quest_2="Whether Extended Producer Responsibility" 
                sec_quest_3="provide steps taken to address the same"
                list=[]     
                for i, line in enumerate(lines):
                     #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                 #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      #("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 #("finallist",finallist)
                return "\n".join(finallist)                   

#@ print(Describe_the_processes_in_place("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def Whether_Extended_Producer_Responsibility_EPR(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Whether Extended Producer Responsibility (EPR) is applicable"
        question_2="Whether Extended Producer"
        question_3="Whether Extended Producer Responsibility (EPR)"
        for i, page in enumerate(pdf.pages[6:-3]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing"
                sec_quest_2="Has the entity conducted Life Cycle Perspective / Assessments" 
                sec_quest_3="Has the entity conducted Life Cycle"
                list=[]     
                for i, line in enumerate(lines):
                    #(i,line)
                    if question.lower() in line.lower():
         #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 #("finallist",finallist)
                return "\n".join(finallist)                   

#@ print(Whether_Extended_Producer_Responsibility_EPR("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def  Has_the_entity_conducted_Life(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Has the entity conducted Life Cycle Perspective",
        "Has the entity conducted Life",
        "Cycle Perspective"

    ]
    q_ends = [
        "If there are any significant social or environmental",
        "If there are any significant",
        "significant social or environmental"

    ]
    
    keys = [
              "NIC Code",
              "Name of Product /Service",
              "% of total Turnover contributed",
              "Boundary for which the Life Cycle Perspective / Assessment was conducted",
              "Whether conducted by independent external agency(Yes/No)",
              "Results communicated in public domain (Yes/No). If yes, provide the web-link."


    ]

    keys_3 = [
              "S.No",
              "NIC Code",
              "Name of Product /Service",
              "% of total Turnover contributed",
              "Boundary for which the Life Cycle Perspective / Assessment was conducted",
              "Whether conducted by independent external agency(Yes/No)",
              "Results communicated in public domain (Yes/No). If yes, provide the web-link."
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:-3]:
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

    final_6 = []
    final_7 = []
    for f in output_rows:
        if len(f) == 6:
            final_6.append(f)
        elif len(f) == 7:
            final_7.append(f)

    
    myout = []

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

#@ print(Has_the_entity_conducted_Life("C:/Users/coda/Documents/titan.pdf"))
#@ print("************")


def  If_there_are_any_significant_social(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "If there are any significant social or environmental",
        "environmental concerns and/or risks arising",
        "action taken to mitigate the same"

    ]
    q_ends = [
        "Percentage of recycled or reused input material",
        "Percentage of recycled or reused",
        "providing services (for service industry)"
    ]
    
    keys = [
            "Name of Product / Service",
            "Description of the risk / concern",
            "Action Taken"
              ]

    keys_3 = [
            "S.no",
            "Name of Product / Service",
            "Description of the risk / concern",
            "Action Taken"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:-3]:
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

#@ print(If_there_are_any_significant_social("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Percentage_of_recycled(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage of recycled or reused input material to total material",
        "Percentage of recycled or reused",
        "providing services (for service industry)"

    ]
    q_ends = [
        "Of the products and packaging reclaimed at end of life",
        "Of the products and packaging reclaimed",
        "reused, recycled, and safely disposed"
    ]
    
    keys = [
              "Indicate input material",
              "Recycled or re-used input material to total material(FY 2024-25(Current Financial Year))",
              "Recycled or re-used input material to total material(FY 2023-24(Previous Financial Year))",
    ]
    
    keys_3 = [
                "S.no",
              "Indicate input material",
              "Recycled or re-used input material to total material(FY 2024-25(Current Financial Year))",
              "Recycled or re-used input material to total material(FY 2023-24(Previous Financial Year))",
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:-3]:
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

#@ print(Percentage_of_recycled("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")

def  Of_the_products_and_packaging(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Of the products and packaging reclaimed at end of life",
        "Of the products and packaging reclaimed",
        "reused, recycled, and safely disposed"

    ]
    q_ends = [
        "Reclaimed products and their packaging materials (as percentage",
        "Reclaimed products and their packaging materials",
        "products sold) for each product category"
    ]
    
    keys = [
              "Category",
              "Reused FY 2024-25",
              "Recycled FY 2024-25",
              "Safely Disposed FY 2024-25",
              "Reused FY 2022-23",
              "Recycled FY 2022-23",
              "Safely Disposed FY 2022-23"
        
    ]

    keys_3 = [
            "S.no",
              "Category",
              "Reused FY 2024-25",
              "Recycled FY 2024-25",
              "Safely Disposed FY 2024-25",
              "Reused FY 2022-23",
              "Recycled FY 2022-23",
              "Safely Disposed FY 2022-23"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:-3]:
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

#@ print(Of_the_products_and_packaging("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")


def  Reclaimed_products(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Reclaimed products and their packaging materials (as percentage",
        "Reclaimed products and their packaging materials",
        "products sold) for each product category"

    ]
    q_ends = [
        "PRINCIPLE 3: BUSINESSES SHOULD RESPECT AND PROMOTE THE WELL-BEING OF ALL EMPLOYEE",
        "PRINCIPLE 3",
        "BUSINESSES SHOULD RESPECT"
    ]
    
    keys = [
              "Indicate product category",
              "Reclaimed products and their packaging materials as % of total products sold in respective category",
        
    ]

    keys_3 = [
            "S.no",
              "Indicate product category",
              "Reclaimed products and their packaging materials as % of total products sold in respective category",
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:-3]:
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

#@ print(Reclaimed_products("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")
