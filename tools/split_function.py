import re

def extract_functions_from_c_code(c_code):
    """
    C 소스 코드에서 함수 단위로 코드를 잘라내는 함수
    """
    # 정규 표현식으로 함수 정의를 찾음
    function_pattern = re.compile(
        r'(?:(?:static|extern|inline|const|unsigned|signed|void|int|float|double|char)[\w\s\*]+)?\s+[\w\s\*]+\s+\w+\s*\([^)]*\)\s*\{(?:[^{}]*|\{[^{}]*\})*\}',
        re.DOTALL
    )
    
    # 매칭된 모든 함수 정의를 리스트로 반환
    functions = function_pattern.findall(c_code)
    return functions

if __name__ == "__main__":
    c_code_example = """
    #include <stdio.h>

    void hello_world() {
        printf("Hello, World!\\n");
    }

    int add(int a, int b) {
        return a + b;
    }

    static void static_function() {
        printf("This is a static function.\\n");
    }
    """

    # 함수 추출 실행
    functions = extract_functions_from_c_code(c_code_example)

    # 결과 출력
    for i, func in enumerate(functions, start=1):
        print(f"Function {i}:\n{func}\n")