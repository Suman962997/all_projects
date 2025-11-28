import pdfplumber
import pytesseract
from PIL import Image
import io
import re




                        ###### PRINCIPLE IX #########
                        
                        
def  Describe_the_mechanisms(pdf_file):
    #@ print("PRINCIPLE 9")
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Describe the mechanisms in place",
        "respond to consumer complaints and feedback"
        "complaints and feedback",

    ]
    q_ends = [
        "Turnover of products and/ services as a percentage of turnover from all products/service",
        "Turnover of products and/ services",
        "turnover from all products/service"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Describe_the_mechanisms("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")



def  Turnover_products(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Turnover of products and/ services as a percentage of turnover from all",
        "Turnover of products and/ services",
        "products/service that carry"

    ]
    q_ends = [
        "Number of consumer complaints in respect",
        "Number of consumer",
        "complaints in respect"
    ]
    keys = [
        "Particulars",
        "As a percentage of total turnover"
    ]

    keys_3 = [
        "S.no",
        "Particulars",
        "As a percentage of total turnover"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Turnover_products("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")



def  Number_consumer(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Number of consumer complaints in respect of the following",
        "Number of consumer complaints",
        "complaints in respect"

    ]
    q_ends = [
        "Details of instances of product recalls on account of safety issues",
        "instances of product recalls on",
        "account of safety issues"
    ]
    keys = [
        "Category",
        "FY 2024-25(Current Financial Year)-(Received during the year)",
        "FY 2024-25(Current Financial Year)-(Pending resolution at end of year)",
        "FY 2024-25(Current Financial Year)-(Remarks)",
        "FY 2023-24(Previous Financial Year)-(Received during the year)",
        "FY 2023-24(Previous Financial Year)-(Pending resolution at end of year)",
        "FY 2023-24(Previous Financial Year)-(Remarks)"
        
    ]

    keys_3 = [
        "S.no",
        "Category",
        "FY 2024-25(Current Financial Year)-(Received during the year)",
        "FY 2024-25(Current Financial Year)-(Pending resolution at end of year)",
        "FY 2024-25(Current Financial Year)-(Remarks)",
        "FY 2023-24(Previous Financial Year)-(Received during the year)",
        "FY 2023-24(Previous Financial Year)-(Pending resolution at end of year)",
        "FY 2023-24(Previous Financial Year)-(Remarks)"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Number_consumer("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")


def  Details_of_instances_of_product(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of instances of product recalls on account of safety issues",
        "instances of product recalls on",
        "account of safety issues"

    ]
    q_ends = [
        "Does the entity have a framework/ policy",
        "cyber security and risks related",
        "risks related to data privacy"        
    ]
    keys = [
        "category",
        "Number",
        "Reasons for recall"
        
    ]

    keys_3 = [
        "S.no",
        "category",
        "Number",
        "Reasons for recall"
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Details_of_instances_of_product("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")


def  Does_the_entity_have_a_framework(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Does the entity have a framework/policy",
        "risks related to data privacy",
        "available, provide weblink of the policy"
    ]
    q_ends = [
        "Provide details of any corrective actions taken or underway",
        "cyber security and data privacy",
        "regulatory authorities"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Does_the_entity_have_a_framework("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")



def  Provide_details_of_any_corrective(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details of any corrective actions taken or underway ",
        "cyber security and data privacy",
        "taken by regulatory authorities on safety"
    ]
    q_ends = [
        "data breaches",
        "Channels / platforms where information",
        "products and services of the entity"

    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Provide_details_of_any_corrective("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")



def  Provide_the_following_information(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide the following information relating to data breaches",
        "informationrelating to data breaches",
        "relating to data breaches"

    ]
    q_ends = [
        "Channels/platforms where information",
        "products and services of the entity",
        "provide web link"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Provide_the_following_information("C:/Users/coda/Documents/titan.pdf"))
#@ print("************")



def  Channels_platforms(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Channels/platforms where information",
        "on products and services of the entity",
        "provide web link"

    ]
    q_ends = [
        "Steps taken to inform and educate consumers",
        "Steps taken to inform and educate",
        "products and/or services"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Channels_platforms("C:/Users/coda/Documents/titan.pdf"))
#@ print("************")



def  Steps_taken(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Steps taken to inform and educate consumers",
        "Steps taken to inform and educate",
        "products and/or services"

    ]
    q_ends = [
        "Mechanisms in place to inform consumers",
        "any risk of disruption",
        "discontinuation of essential services"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Steps_taken("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")



def  Mechanisms_place(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Mechanisms in place to inform consumers",
        "any risk of disruption",
        "discontinuation of essential services"

    ]
    q_ends = [
        "Does the entity display product information",
        "what Is mandated as per local laws",
        "product over and above what Is"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:
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

#@ print(Mechanisms_place("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")



def Does_the_entity_display_product_information(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Does the entity display product information on the product over and above what is mandated"
        question_2="Does the entity display product information on the product over and above what is "
        question_3="mandated as per local laws"
        for i, page in enumerate(pdf.pages[-6:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide the following information relating to data breaches"
                sec_quest_2="Provide the following information " 
                sec_quest_3="relating to data breaches"
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
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
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#@ print(Does_the_entity_display_product_information("C:/Users/coda/Documents/ppap.pdf"))
#@ print("************")


# def Provide_the_following_information(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         #("file opend")
#         question="Provide the following information relating to data breaches"
#         question_2="Provide the following information relating"
#         question_3="data breaches"
#         for i, page in enumerate(pdf.pages[-6:]):
#             text = page.extract_text()
#             if text and question in text or question_2 in text  or question_3 in text:
#                 #(f"Question found on page {i}")
#                 image = page.to_image(resolution=300).original  # 300 DPI is usually enough

#                 # Run Tesseract with config to preserve whitespaces
#                 custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
#                 ocr_text = pytesseract.image_to_string(image, config=custom_config)
#                 # # #(ocr_text)
#                 lines = ocr_text.splitlines()
#                 sec_quest="Number of instances of data breaches along-with impact"
#                 sec_quest_2="Number of instances " 
#                 sec_quest_3="along-with impact"
#                 list=[]     
#                 for i, line in enumerate(lines):
#                     # #(i,line)
#                     if question.lower() in line.lower():
#                         #("***q1")
#                         list=lines[i:]
#                         break
#                     elif question_2.lower() in line.lower():
#                         #("***q2")
#                         list=lines[i:]
#                         break
#                     elif question_3.lower() in line.lower():
#                         #("****q3")
#                         list=lines[i:]
#                         break
#                 # #("405 **",list)
#                 finallist=[]
                
#                 for i,selist in enumerate(list):
#                     # #("*",i,selist)
#                     if sec_quest.lower() in selist.lower():
#                         #("#########",i,selist)
#                         finallist=list[:i]
#                         break
#                     elif sec_quest_2.lower() in selist.lower():
#                         #("### sec_2")
#                         finallist=list[:i]
#                         break
#                     elif sec_quest_3.lower() in selist.lower():
#                         #("&& sec3")
#                         finallist=list[:i]
#                         break
#                     else :
#                         finallist=list
#                 # #("finallist",finallist)
#                 return finallist                       

# #@ print(Provide_the_following_information("C:/Users/coda/Documents/ppap.pdf"))
# #@ print("************")



# def Number_of_instances(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         #("file opend")
#         question="Number of instances of data breaches along-with impact"
#         question_2="Number of instances of data breaches "
#         question_3="along-with impact"
#         for i, page in enumerate(pdf.pages[-6:]):
#             text = page.extract_text()
#             if text and question in text or question_2 in text  or question_3 in text:
#                 #(f"Question found on page {i}")
#                 image = page.to_image(resolution=300).original  # 300 DPI is usually enough

#                 # Run Tesseract with config to preserve whitespaces
#                 custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
#                 ocr_text = pytesseract.image_to_string(image, config=custom_config)
#                 # # #(ocr_text)
#                 lines = ocr_text.splitlines()
#                 sec_quest="Percentage of data breaches involving personally identifiable information of customers"
#                 sec_quest_2="Percentage of data breaches " 
#                 sec_quest_3="information of customers"
#                 list=[]     
#                 for i, line in enumerate(lines):
#                     # #(i,line)
#                     if question.lower() in line.lower():
#                         #("***q1")
#                         list=lines[i:]
#                         break
#                     elif question_2.lower() in line.lower():
#                         #("***q2")
#                         list=lines[i:]
#                         break
#                     elif question_3.lower() in line.lower():
#                         #("****q3")
#                         list=lines[i:]
#                         break
#                 # #("405 **",list)
#                 finallist=[]
                
#                 for i,selist in enumerate(list):
#                     # #("*",i,selist)
#                     if sec_quest.lower() in selist.lower():
#                         #("#########",i,selist)
#                         finallist=list[:i]
#                         break
#                     elif sec_quest_2.lower() in selist.lower():
#                         #("### sec_2")
#                         finallist=list[:i]
#                         break
#                     elif sec_quest_3.lower() in selist.lower():
#                         #("&& sec3")
#                         finallist=list[:i]
#                         break
#                     else :
#                         finallist=list
#                 # #("finallist",finallist)
#                 return finallist                       

# #@ print(Number_of_instances("C:/Users/coda/Documents/ppap.pdf"))
# #@ print("************")




# def Percentage_data_breaches(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         #("file opend")
#         question="Percentage of data breaches involving personally identifiable information of customers"
#         question_2="Percentage of data breaches involving "
#         question_3="identifiable information of customers"
#         for i, page in enumerate(pdf.pages[-6:]):
#             text = page.extract_text()
#             if text and question in text or question_2 in text  or question_3 in text:
#                 #(f"Question found on page {i}")
#                 image = page.to_image(resolution=300).original  # 300 DPI is usually enough

#                 # Run Tesseract with config to preserve whitespaces
#                 custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
#                 ocr_text = pytesseract.image_to_string(image, config=custom_config)
#                 # # #(ocr_text)
#                 lines = ocr_text.splitlines()
#                 sec_quest="last"
#                 sec_quest_2="dc d" 
#                 sec_quest_3="cdcd"
#                 list=[]     
#                 for i, line in enumerate(lines):
#                     # #(i,line)
#                     if question.lower() in line.lower():
#                         #("***q1")
#                         list=lines[i:]
#                         break
#                     elif question_2.lower() in line.lower():
#                         #("***q2")
#                         list=lines[i:]
#                         break
#                     elif question_3.lower() in line.lower():
#                         #("****q3")
#                         list=lines[i:]
#                         break
#                 # #("405 **",list)
#                 finallist=[]
                
#                 for i,selist in enumerate(list):
#                     # #("*",i,selist)
#                     if sec_quest.lower() in selist.lower():
#                         #("#########",i,selist)
#                         finallist=list[:i]
#                         break
#                     elif sec_quest_2.lower() in selist.lower():
#                         #("### sec_2")
#                         finallist=list[:i]
#                         break
#                     elif sec_quest_3.lower() in selist.lower():
#                         #("&& sec3")
#                         finallist=list[:i]
#                         break
#                     else :
#                         finallist=list
#                 # #("finallist",finallist)
#                 return finallist                       

# #@ print(Percentage_data_breaches("C:/Users/coda/Documents/ppap.pdf"))
# #@ print("************")
