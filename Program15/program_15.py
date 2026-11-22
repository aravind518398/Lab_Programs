from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

def stem_words(text):
    word_token = word_tokenize(text) 
    stems = []
    for word in word_token:
        stems.append(stemmer.stem(word))
    return stems

text = "Data Sciences uses Scientific methods, algorithms and many types of processes"
print("Original Text: ")
print(text)
print("Result after stemming: ")
print(stem_words(text))


