import string

def remove_whitespace(text):
    return "".join(text.split())

input_str = "We don't need the given questions"

print(remove_whitespace(input_str))