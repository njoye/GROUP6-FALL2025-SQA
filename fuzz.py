import ast
import random
import string
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'MLForensics', 'FAMEML'))

from py_parser import (
    getPythonParseObject,
    checkLoggingPerData,
    getPythonAtrributeFuncs,
    checkAttribFuncsInExcept,
    func_def_log_check
)

def random_string(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fuzz_getPythonParseObject():
    for _ in range(10):
        s = random_string(30)
        try:
            getPythonParseObject(s)
        except Exception as e:
            print("getPythonParseObject:", e)

def fuzz_checkLoggingPerData():
    for _ in range(10):
        try:
            checkLoggingPerData(random_string(10))
        except Exception as e:
            print("checkLoggingPerData:", e)

def fuzz_getPythonAtrributeFuncs():
    for _ in range(10):
        try:
            getPythonAtrributeFuncs(random_string(15))
        except Exception as e:
            print("getPythonAtrributeFuncs:", e)

def fuzz_checkAttribFuncsInExcept():
    for _ in range(10):
        fake_tuple = tuple(random_string(5) for _ in range(random.randint(1, 6)))
        try:
            checkAttribFuncsInExcept(fake_tuple)
        except Exception as e:
            print("checkAttribFuncsInExcept:", e)

def fuzz_func_def_log_check():
    for _ in range(10):
        fake_ast = random_string(25)
        try:
            func_def_log_check(fake_ast)
        except Exception as e:
            print("func_def_log_check:", e)

print("Fuzzing start")
fuzz_getPythonParseObject()
fuzz_checkLoggingPerData()
fuzz_getPythonAtrributeFuncs()
fuzz_checkAttribFuncsInExcept()
fuzz_func_def_log_check()
print("Fuzzing done")
