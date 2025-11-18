import ast
import random
import string

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fuzz_file_like_input(data):
    try:
        return data.encode('utf-8')
    except Exception as e:
        print(f"Exception caught in fuzz_file_like_input: {e}")

def fuzz_ast_and_str(data):
    try:
        node = ast.parse(data)
        print(f"Parsed AST successfully: {ast.dump(node, annotate_fields=False)}")
    except Exception as e:
        print(f"Exception caught in fuzz_ast_and_str: {e}")

def fuzz_ast_list(data_list):
    for idx, data in enumerate(data_list):
        try:
            node = ast.parse(data)
            _ = node.__dict__
        except Exception as e:
            print(f"Exception caught in fuzz_ast_list: {e}")

def fuzz_tuple_list(tuple_list):
    for tup in tuple_list:
        try:
            a, b, c, d = tup
        except Exception as e:
            print(f"Exception caught in fuzz_tuple_list: {e}")

print("Fuzzing start")

for _ in range(10):
    s = random_string(random.randint(1, 50))
    fuzz_file_like_input(s)
    fuzz_ast_and_str(s)

str_list = [random_string(random.randint(5, 30)) for _ in range(5)]
fuzz_ast_list(str_list)

tuple_list = [
    tuple(random_string(2) for _ in range(random.randint(1, 6)))
    for _ in range(5)
]
fuzz_tuple_list(tuple_list)

print("Fuzzing done")
