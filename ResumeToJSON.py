import os
import pdfplumber
import docx

def extract_from_pdf(file_path):
    """Extract text from PDF using pdfplumber"""
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_from_docx(file_path):
    """Extract text from DOCX using python-docx"""
    doc = docx.Document(file_path)
    text = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(text)

def extract_from_txt(file_path):
    """Extract text from TXT file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_resume_text(file_path):
    """Detect file type and extract text"""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_from_pdf(file_path)
    elif ext == ".docx":
        return extract_from_docx(file_path)
    elif ext == ".txt":
        return extract_from_txt(file_path)
    else:
        raise ValueError("Unsupported file format. Please use PDF, DOCX, or TXT.")


if __name__ == "__main__":
    resume_file = "oblique-projects.pdf"                              # you can change resume file here

    print(f" Extracting text from {resume_file}...\n")
    text = extract_resume_text(resume_file)

    print(" Resume Text Extracted:\n")
    print(text)


print("\n\n")

print("llm model generated output" )

print("\n\n")


import ollama 

def ask_gemma(my_data_note: str, my_prompt_note: str) -> str:

    message_for_gemma = f"{my_prompt_note}\n\nHere is the information: {my_data_note}"

    try:
        gemma_response_object = ollama.generate(
            model='gemma2:2b',                                                                              #you can change model here
            prompt=message_for_gemma
        )
        gemma_final_answer = gemma_response_object['response']

        return gemma_final_answer 

    except Exception as e:
        print(f"Oops! Something went wrong: {e}")
        print("Make sure Ollama is running and you have 'gemma2:2b' installed.")
        return "Sorry, I couldn't get an answer."

if __name__ == "__main__":
    my_data_to_give_gemma = text

    my_prompt_for_gemma = """
can you convert my data into json format that i need structure can you convert
the data is :{text}

the json file i need structure is :
{
"status": "1",
"alert": "0",
"message": "Successfully analyzed and parsed resume PDF",
"token": "",
"data": {
"parsedData": {
"Name": "KRISH KAKADIYA",
"Mobile_Number": null,
"Address": "Surat, Gujarat, India",
"City": "Surat",
"Zip_Code": null,
"State": "Gujarat",
"Country": "India",
"Email": "kakadiyakrish2000@gmail.com",
"LinkedIn": null,
"GitHub": null,
"Experience": [
{
"Job_Title": "Software Engineer",
"Company": "Aarvi Technology",
"Start_Date": "2021-03-01",
"End_Date": "2025-04-01",
"Description": "A software development company specializing in modern web applications\\nArchitect and develop end-to-end web applications using modern \\ntechnologies\\nCollaborate with clients to gather and analyze requirements for tailored \\nsolutions\\nDesign and implement complex data models and database structures \\nfor performance\\nIntegrate third-party APIs to enhance system scalability and \\nfunctionality\\nOptimize applications for speed, security, and cross-device \\ncompatibility"
}
],
"Education": [
{
"Degree": "BCA",
"Institution": "Udhna College (UCCC & SPBCBA & SDHGCBCA & IT), Surat",
"Graduation_Start_Date": "2017-08-01",
"Graduation_End_Date": "2020-05-01"
},
{
"Degree": "12th",
"Institution": "Swaminarayan Gurukul, Damnagar",
"Graduation_Start_Date": "2016-06-01",
"Graduation_End_Date": "2018-05-01"
},
{
"Degree": "10th",
"Institution": "Swaminarayan Gurukul, Damnagar",
"Graduation_Start_Date": "2014-06-01",
"Graduation_End_Date": "2016-05-01"
}
],
"Years_of_Experience": "3.0",
"Skills": [
"full-stack development",
"web applications",
"Angular",
"Node.js",
"REST APIs",
"Bootstrap",
"MySQL",
"HTML5",
"CSS3",
"JavaScript",
"PHP",
"jQuery",
"SEO",
"HR",
"attendance",
"leave",
"analytics",
"PHP",
"MySQL"
],
"Languages": [
"Gujarati",
"Hindi",
"English"
]
}
}
}

dont generate any other text except json format
"""

    gemma_result_note = ask_gemma(my_data_to_give_gemma, my_prompt_for_gemma)

    # print("--- My Data Note ---")
    # print(my_data_to_give_gemma)
    # print("\n--- My Prompt Note ---")
    # print(my_prompt_for_gemma)
    print("\n--- Gemma's Answer Note ---")
    print(gemma_result_note)
