from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
nltk.download('punkt_tab')



def remove_stopwords(text):
    stop_words = stopwords.words("english")
    word_tokens = word_tokenize(text)

    filtered_text =[]
    
    for word in word_tokens:
        if word not in stop_words:
            filtered_text.append(word)

    return filtered_text

example_text = "This is a Sample Sentence and We are going to remove the Stopwords from this."
print("Original Text")
print(example_text)
print("Resultant text after removing stopwords")
print(remove_stopwords(example_text))