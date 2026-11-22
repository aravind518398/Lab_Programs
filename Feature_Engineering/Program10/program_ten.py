import re

def remove_numbers(text):
    result = re.sub(r"\d+","",text)
    return result

print("Original String: ")
input_str = "There are 3 balls in this bag, and 12 in the other one."
print(input_str)
print("String after removing numbers")
print(remove_numbers(input_str))