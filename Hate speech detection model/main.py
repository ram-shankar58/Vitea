from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import joblib

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    # Tokenize text
    words = word_tokenize(text)
    
    filtered_words = [ps.stem(word) for word in words if word.lower() not in stop_words]
    
    processed_text = " ".join(filtered_words)
    
    return processed_text

def predict_hate_speech(text):
    model = joblib.load('model/hatemodellatest.pkl')

    tfidf_vectorizer = joblib.load('model/tfidifsecond.joblib')
    
    processed_text = preprocess_text(text)
    
    text_tfidf = tfidf_vectorizer.transform([processed_text])
    
    predicted_class = model.predict(text_tfidf)[0]
    
    return predicted_class

input_text = input() #enter the string in.
predicted_class = predict_hate_speech(input_text)
print("Predicted class:", predicted_class)
