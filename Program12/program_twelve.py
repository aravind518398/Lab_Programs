import string

def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


input_str = "Hey, did you know that the Summer break is coming? Amazing right!! It's only 5 more days!!"
print("Original String: ")
print(input_str)
print("String after removing punctuation")
print(remove_punctuation(input_str))