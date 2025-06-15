import google.generativeai as genai
from dotenv import load_dotenv
from split_function import extract_functions_from_c_code
import os
from datetime import datetime


def set_working_directory():
    # Get the absolute path of the currently executing Python file
    current_file_path = os.path.abspath(__file__)

    # Get the directory containing the Python file
    current_directory = os.path.dirname(current_file_path)

    # Change the working directory to the Python file's directory
    os.chdir(current_directory)

if __name__ == "__main__":
    set_working_directory()

    # .env 파일 로드
    load_dotenv()

    # sample.c 파일 읽기
    f = open("./../sample_code/sample.c", "r")
    source_code = f.read()
    f.close()
    functions = extract_functions_from_c_code(source_code)

    # 환경 변수에서 API 키 가져오기
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(
        "gemini-2.0-flash-lite"
    )  # 모델 이름은 필요에 따라 변경 가능
    generation_config = {
        "temperature": 0.0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 4096,
    }


    # convension.md 파일 읽기
    f = open("./../rules/convension.md", "r", encoding="utf-8")
    convension = f.read()
    f.close()

    # reports_format.md 파일 읽기
    f = open("./../rules/reports_format.md", "r", encoding="utf-8")
    report_format = f.read()
    f.close()

    # Get the current date and time
    now = datetime.now()
    # Format the date and time as a string
    timestamp = now.strftime("%Y-%m-%d_%H-%M")
    # Create a directory with the timestamp
    directory = f"reports_{timestamp}"

    print("Generating reports...")
    for name, function in functions:
        prompt = f"""
 You are an expert in C programming style and conventions. Analyze the following C function based on the given coding conventions and generate a compliance report.
### Coding Conventions:
{convension}
### C Function:
{function}
### Compliance Report:
{report_format}
    """
        # print("prompt: ", prompt)


        response = model.generate_content(prompt, generation_config=generation_config)
        # print(response.text)
        # make folder with date and time and save the report
        
        os.makedirs(directory, exist_ok=True)
        # Save the report in the directory
        with open(f"{directory}/report_{name}.md", "w", encoding="utf-8") as file:
            file.write(response.text)