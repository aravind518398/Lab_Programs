import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

def lemma_words(text):
    word_token = word_tokenize(text)
    lemmas = []
    for word in word_token:
        lemmas.append(lemmatizer.lemmatize(word))

    return lemmas

text = "Data science uses scientific methods algorithms and many types of processes"
print("Original text: ")
print(text)
print("Result after lemmatization: ")
print(lemma_words(text))

