import inflect
import re

p = inflect.engine()

def convert_number(text):
    return re.sub(r'\d+',
        lambda match: p.number_to_words(int(match.group())),
        text      
    )


input_str = "There are 3 balls in this bag, and 12 in the other one."
print(convert_number(input_str))