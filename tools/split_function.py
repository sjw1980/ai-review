import re

def extract_functions_from_c_code(c_code):
    """
    C 소스 코드에서 함수 단위로 코드를 잘라내는 함수
    """
    # 정규 표현식으로 함수 정의를 찾음
    function_pattern = re.compile(
        r'([a-zA-Z_][\w]*)\s*\([^)]*\)\s*\{(?:[^{}]*|\{[^{}]*\})*\}',
        re.DOTALL
    )
    
    # 매칭된 모든 함수 정의를 리스트로 반환
    results = []
    for match in function_pattern.finditer(c_code):
        func_code = match.group(0)
        func_name = match.group(1)
        results.append((func_name, func_code))

    return results

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
    for name, code in functions:
        print(f"Function name: {name}\nFunction code:\n{code}\n")