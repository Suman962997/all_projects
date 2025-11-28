import pdfplumber
import pytesseract
from PIL import Image
import io
import re
# 
def clean_answer(answer, question):
    # Remove extra spaces and newlines for comparison
    normalized_question = re.sub(r'\s+', ' ', question.strip())
    normalized_answer = re.sub(r'\s+', ' ', answer.strip())

    # If question exists in answer, remove it
    if normalized_question in normalized_answer:
        cleaned_answer = normalized_answer.replace(normalized_question, '').strip()
        return cleaned_answer
    return answer.strip()


def Whether_your_entity(pdf_path):
    found = False
    question_of_answer="""
Whether your entity’s policy/policies cover"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Whether your entity’s policy"
        question_2="Policy and management processes"
        question_3="entity's policy/policies"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Has the policy been approved by the Board" 
                sec_quest_2="Has the policy been" 
                sec_quest_3="approved by the Board" 
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i-1:]
                        break
                    elif  question_2.lower() in line.lower():
                        list=lines[i-1:]
                        break                    
                    elif  question_3.lower() in line.lower():
                        list=lines[i-1:]
                        break
                    

                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

                elif len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Whether_your_entity("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Has_the_policy(pdf_path):
    found = False
    question_of_answer="""
Has the policy been approved by the Board    """
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Has the policy been approved by the Board"
        question_2="policy been approved"
        question_3="policy been"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Web Link of the Policies" 
                sec_quest_2="Web Link"
                sec_quest_3="of the Policies"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i-1:]
                        break
                    elif  question_2.lower() in line.lower():
                        list=lines[i-1:]
                        break                    
                    elif  question_3.lower() in line.lower():
                        list=lines[i-1:]
                        break
                    

                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

                elif len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Has_the_policy("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Web_Link_of_Policies(pdf_path):
    found = False
    question_of_answer="""
    Web Link of the Policies
    """
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Web Link of the Policies, if available"
        question_2="Web Link of the Policies"
        question_3="Web Link"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether the entity has translated" 
                sec_quest_2="has translated"
                sec_quest_3="procedures."
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                        break
                    elif  question_2.lower() in line.lower():
                        list=lines[i:]
                        break                    
                    elif  question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                    

                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                    
                if finallist:
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                else:
                    return "Not Applicable"    

                    
            
    if not found:
        return "Not Applicable"

#@ print(Web_Link_of_Policies("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")



def Whether_entity_translated(pdf_path):
    found = False
    question_of_answer="""
Whether the entity has translated"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Whether the entity has translated the"
        question_2="the entity has"
        question_3="translated the policy"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i+1:]

                finallist=[]
                sec_quest="Do the enlisted policies extend to your" 
                sec_2="enlisted policies"                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_2.lower() in selist.lower():
                        finallist=list[:1+i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
                elif len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Whether_entity_translated("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Do_the_enlisted(pdf_path):
    found = False
    question_of_answer="""
Do the enlisted policies extend
"""
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Do the enlisted policies"
        question_2="enlisted policies"
        question_3="your value chain"
        
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="national and international" 
                sec_quest_2="Name of the national and"
                sec_quest_3="international codes"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i-1:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i-1:]
                    elif question_3.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i-1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    if sec_quest_2.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    if sec_quest_3.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4                
           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Do_the_enlisted("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Name_of_the_national(pdf_path):
    found = False
    question_of_answer="""
Name of the national and international"""
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="national and international codes/certifications/labels/ standards"
        question_2="Name of the national"
        question_3="national and international codes/certifications/labels/"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Specific commitments," 
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i+1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result

                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return "Not Applicable" 
            
    if not found:
        return "Not Applicable"

#@ print(Name_of_the_national("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")

def Specific_commitments(pdf_path):
    found = False
    question_of_answer="""
Specific commitments, goals"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Specific commitments, goals and targets"
        question_2="Specific commitments"
        question_3="entity with defined timelines"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Performance of the entity against" 
                sec_quest_2="along with reasons"
                sec_quest_3="same are not met"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return "Not Applicable" 
            
    if not found:
        return "Not Applicable"

#@ print(Specific_commitments("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Performance_of_the_entity(pdf_path):
    found = False
    question_of_answer="""
Performance of the entity against the specific"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="entity against the"
        question_2="Performance of the entity"
        question_3=" reasons in case the same"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Statement by director responsible" 
                sec_quest_2="Statement by director"
                sec_quest_3="business responsibility report"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                        break
                    
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
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
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable" 
            
    if not found:
        return "Not Applicable"

#@ print(Performance_of_the_entity("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")

                                    ###### second part #####
 
 

 
def Statement_by_director(pdf_path):
    #@ print("PART B")
    found = False
    question_of_answer="""
    Statement by director responsible"""

    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Statement by director responsible for the business"
        question_2="Statement by director"
        question_3="Statement by"

        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of the highest authority"
                sec_quest_2="Details of the highest" 
                sec_quest_3="Responsibility policy"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
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
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result

                else:
                    return "Not Applicable"
                
    if not found:
        return "Not Applicable"


#@ print(Statement_by_director("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Details_of_the_highest(pdf_path):
    found = False
    question_of_answer="""
Details of the highest authority responsible    
    """
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Details of the highest authority responsible"
        question_2="Details of the highest"
        question_3="sustainability related issues?"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have"
                sec_quest_2="Committee of the" 
                sec_quest_3="If yes, provide details"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                        break
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # #@ print("scs",finallist)
                if finallist:
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result

                else:
                    return "Not Applicable"
    if not found:
        return "Not Applicable"
                

                    
#@ print(Details_of_the_highest("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")



def Does_the_entity(pdf_path):
    found = False
    question_of_answer="""
Does the entity have a specified"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Does the entity have a specified Committee"
        question_2="specified Committee"
        question_3="making on sustainability"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of Review of NGRBCs by the Company"
                sec_quest_2="Details of Review" 
                sec_quest_3="Review of NGRBCs"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"                    
            
    if not found:
        return "Not Applicable"

#@ print(Does_the_entity("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


def Indicate_whether_review(pdf_path):
    found = False
    question_of_answer="""
Indicate whether review was undertaken"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Indicate whether review was undertaken"
        question_2="undertaken by Director"
        question_3="Indicate whether review"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Has the entity carried out independent assessment"
                sec_quest_2=" Has the entity carried out independent" 
                sec_quest_3=" Has the entity carried"
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
                        list=lines[i:]
                        break
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"
    if not found:
        return "Not Applicable"

#@ print(Indicate_whether_review("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")



def Frequency_Annually(pdf_path):
    found = False
    question_of_answer="""
Frequency(Annually/ Half yearly"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Frequency (Annually/ Half yearly/ Quarterly Any other"
        question_2="Frequency (Annually/ Half yearly/ Quarterly/"
        question_3="Frequency (Annually/"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                lines = ocr_text.splitlines()
                # #@ print(lines)
                sec_quest=" Has the entity carried out independent assessment"
                sec_quest_2=" Has the entity carried out independent" 
                sec_quest_3=" Has the entity carried"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        # #@ print("***q3")
                        list=lines[i:]
                    else:
                        finallist=list
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Frequency_Annually("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")




def Has_the_entity_carried(pdf_path):
    found = False
    question_of_answer="""
Has the entity carried out independent"""
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Has the entity carried out independent"
        question_2="Has the entity"
        question_3="If yes, provide name of the agency"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If answer to question (1) above"
                sec_quest_2="If answer to question" 
                sec_quest_3="Principles are covered by"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Has_the_entity_carried("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")


  ##### 12-th

def If_answer_to_question(pdf_path):
    found = False
    question_of_answer="""
If answer to question (1) above
    """
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="If answer to question (1) above is"
        question_2="If answer to question (1) above is “No”"
        question_3="answer to question"
        for i, page in enumerate(pdf.pages[3:20]):
            text = page.extract_text()
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Supply Chain Mangement"
                sec_quest_2="SECTION C" 
                sec_quest_3="PRINCIPLE WISE PERFORMANCE DISCLOSURE"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        # #@ print("::")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("ELIF")
                        list=lines[i+1:]
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        # break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("HBJAS")
                        finallist=list[:i]
                        # break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("KKKKs")
                        finallist=list[:1+i]
                        # break
                    else:
                        finallist=list[i]
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    ac_ans="\n".join(finallist)
                    result = clean_answer(ac_ans,question_of_answer)
                    return result
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(If_answer_to_question("C:/Users/coda/Documents/vendanta.pdf"))
#@ print("************")
