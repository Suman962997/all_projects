import pdfplumber
import pytesseract
from PIL import Image
import io
import re

                                                    ###### PRINCIPLE IV #########



def  Describe_the_processes(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # # ("file opend")
        #@ print("PRINCIPLE 4")

        question="Describe the processes for identifying key stakeholder groups of the entity"
        question_2="Describe the processes for identifying"
        question_3="stakeholder groups of the entity"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # # (f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # (ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group"
                sec_quest_2="List stakeholder groups identified as key for " 
                sec_quest_3=" engagement with each stakeholder group"
                list=[]     
                for i, line in enumerate(lines):
                    # # (i,line)
                    if question.lower() in line.lower():
                        # # ("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # ("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # ("****q3")
                        list=lines[i:]
                        break
                # # ("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # ("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # ("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # # ("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # # ("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # # ("finallist",finallist)
                return finallist                       

#@ print(Describe_the_processes("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")




def List_stakeholder(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "List stakeholder groups identified",
        "List stakeholder groups",
        "each stakeholder group"

    ]
    q_ends = [
        "PRINCIPLE 5",
        "Provide the processes",
        "provided to the Board"
    ]
    keys = [
        
        "Stakeholder Group",
        "Whether identified as Vulnerable & Marginalized Group (Yes/No)",
        "Channels of communication(Email, SMS, Newspaper, Pamphlets, Advertisement, Community Meetings, Notice Board, Website), Other",
        "Frequency of engagement(Annually/ Half yearly/ Quarterly / others – please specify)",
        "Purpose and scope of engagement including key topics and concerns raised during such engagement",
        
    ]

    keys_3 = [
        "S.no",
        "Stakeholder Group",
        "Whether identified as Vulnerable & Marginalized Group (Yes/No)",
        "Channels of communication(Email, SMS, Newspaper, Pamphlets, Advertisement, Community Meetings, Notice Board, Website), Other",
        "Frequency of engagement(Annually/ Half yearly/ Quarterly / others – please specify)",
        "Purpose and scope of engagement including key topics and concerns raised during such engagement",
        
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

    # # ("#######",lines_between)
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

#@ print(List_stakeholder("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



def Provide_the_processes(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # # ("file opend")
        question="Provide the processes for consultation between stakeholders and the Board on economic"
        question_2="Provide the processes for consultation between stakeholders" 
        question_3="how is feedback from such consultations provided to the Board"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # # (f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # # (ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity"
                sec_quest_2="Whether stakeholder consultation is used to support the identification"
                sec_quest_3="stakeholders on these topics were incorporated into policies and activities"
                list=[]     
                for i, line in enumerate(lines):
                    # # (i,line)
                    if question.lower() in line.lower():
                        # # ("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # ("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # ("****q3")
                        list=lines[i:]
                        break
                # # ("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # ("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # ("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # # ("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # # ("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # # ("finallist",finallist)
                return finallist                       

#@ print(Provide_the_processes("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")




def Whether_stakeholder_consultation(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # # ("file opend")
        question="Whether stakeholder consultation is used to support the identification and management of environmental"
        question_2="Whether stakeholder consultation is used"
        question_3="incorporated into policies and activities of the entity"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # # (f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # # (ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups"
                sec_quest_2="Provide details of instances of engagement" 
                sec_quest_3=" address the concerns of vulnerable/ marginalized stakeholder groups"
                list=[]     
                for i, line in enumerate(lines):
                    # # (i,line)
                    if question.lower() in line.lower():
                        # # ("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # ("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # ("****q3")
                        list=lines[i:]
                        break
                # # ("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # ("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # ("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # # ("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # # ("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # # ("finallist",finallist)
                return finallist                       

#@ print(Whether_stakeholder_consultation("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")




def Provide_details_of_instances (pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # # ("file opend")
        question="Provide details of instances of engagement with, and actions taken to, address the concerns"
        question_2="Provide details of instances of engagement with, and actions taken to"
        question_3="vulnerable/ marginalized stakeholder groups"
        for i, page in enumerate(pdf.pages[10:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                # # (f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # # (ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Principle 5:"
                sec_quest_2="Businesses should respect and promote human rights." 
                sec_quest_3="Businesses should respect"
                list=[]     
                for i, line in enumerate(lines):
                    # # (i,line)
                    if question.lower() in line.lower():
                        # # ("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # ("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # ("****q3")
                        list=lines[i:]
                        break
                # # ("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # ("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # ("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # # ("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # # ("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # # ("finallist",finallist)
                return finallist                       

#@ print(Provide_details_of_instances("C:/Users/coda/Documents/bse.pdf"))
#@ print("************")



