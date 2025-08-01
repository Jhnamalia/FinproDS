import streamlit as st 
import joblib
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# --- Setup halaman ---
st.set_page_config(page_title="Sentiment Predictor", layout="centered")
st.title("📱 Google Play Review Sentiment Classifier")
st.markdown("Masukkan review aplikasi, dan model akan memprediksi sentimennya:")

# --- Download stopwords ---
nltk.download('stopwords')

# --- Load model & vectorizer ---
model = joblib.load('rf_sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# --- Setup stopwords ---
custom_stopwords = set(stopwords.words('english')).union(ENGLISH_STOP_WORDS)
additional_words = {
    'app', 'game', 'update', 'phone', 'time', 'work', 'please',
    'thing', 'lot', 'account', 'feature', 'version', 'open', 'device',
    'google', 'level', 'day', 'option'
}
words_to_keep = {'just', 'fine', 'okay', 'bit', 'not', 'no', 'issue'}
safe_stopwords = (custom_stopwords.union(additional_words)).difference(words_to_keep)

# --- Preprocessing function ---
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in safe_stopwords]
    return ' '.join(tokens)

# --- Predict function ---
def predict_sentiment(text):
    cleaned_text = preprocess_text(text)
    vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized)[0]
    label_map = {0: 'Negative 😞', 1: 'Neutral 😐', 2: 'Positive 😊'}
    return label_map[prediction]

emoji_map = {
    'Negative 😞': "Sentimen negatif, pengguna kemungkinan tidak puas.",
    'Neutral 😐': "Sentimen netral, pengguna biasa saja.",
    'Positive 😊': "Sentimen positif, pengguna senang atau puas."
}

# --- Input pengguna ---
user_input = st.text_area("✍️ Tulis review di sini...", height=150)

# --- Prediksi ---
if st.button("🔍 Prediksi Sentimen"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        result = predict_sentiment(user_input)
        st.success(f"Hasil Prediksi: **{result}**")
        st.markdown(f"📝 _{emoji_map[result]}_")

# --- Contoh review ---
with st.expander("📋 Contoh review yang bisa dicoba"):
    st.markdown("""
    - "I love this app! It's so helpful and easy to use."
    - "It does what it says. Nothing more, nothing less."
    - "This app is terrible, full of bugs and ads."
    """)

# --- Informasi model ---
with st.expander("🔍 Tentang Model"):
    st.markdown("""
    - **Algoritma:** Random Forest Classifier
    - **Fitur teks:** TF-IDF (1000 fitur)
    - **Stopwords:** Kombinasi NLTK, sklearn, dan tambahan manual
    - **Kelas:** Negative (0), Neutral (1), Positive (2)
    """)

st.markdown("---")
st.markdown("👨‍💻 *Model ini dibangun untuk membantu menganalisis ulasan aplikasi Google Play Store secara otomatis.*")
