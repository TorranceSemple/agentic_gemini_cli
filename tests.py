from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test_info():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

def test_file():
    result = get_file_content("calculator", "main.py")
    print(result)
    print("========================")
    
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print("========================")
    
    result = get_file_content("calculator", "/bin/cat")
    print(result)

if __name__ == "__main__":
    test_file()