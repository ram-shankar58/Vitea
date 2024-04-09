from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import joblib

# Text preprocessing
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    # Tokenize text
    words = word_tokenize(text)
    
    # Remove stopwords and perform stemming
    filtered_words = [ps.stem(word) for word in words if word.lower() not in stop_words]
    
    # Join the words back into a string
    processed_text = " ".join(filtered_words)
    
    return processed_text

def predict_hate_speech(text):
    # Load the trained model
    model = joblib.load('model/hatemodellatest.pkl')

    # Load the fitted TF-IDF vectorizer
    tfidf_vectorizer = joblib.load('model/tfidifsecond.joblib')
    
    # Preprocess input text
    processed_text = preprocess_text(text)
    
    # Transform text into TF-IDF vector
    text_tfidf = tfidf_vectorizer.transform([processed_text])
    
    # Predict class
    predicted_class = model.predict(text_tfidf)[0]
    
    return predicted_class

# Example usage:
input_text = "This is an example of hate speech"
predicted_class = predict_hate_speech(input_text)
print("Predicted class:", predicted_class)
