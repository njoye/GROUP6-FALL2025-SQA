import random
import string
import sys 
import os

from MLForensics.FAMEML.py_parser import getPythonParseObject
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'MLForensics'))

def generate_random_string(length):
    """Generates a random string of a specified length."""
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def fuzz_function(function_to_fuzz):
    for count in range(1, 100):
        random_input = generate_random_string(count)
        try:
            return_value = function_to_fuzz(random_input)
        except Exception as e:
            print(f"Exception caught: {e}")
            
            
if __name__ == "__main__":
    print("Fuzzing")
    fuzz_function(getPythonParseObject)