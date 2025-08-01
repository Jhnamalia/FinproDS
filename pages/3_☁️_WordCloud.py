import streamlit as st
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/reviews.csv')

st.title("☁️ WordCloud Review Aplikasi")
st.markdown("Visualisasi kata-kata yang paling sering muncul dalam ulasan pengguna berdasarkan sentimen (positif, netral, negatif).")

# Urutkan sentimen agar konsisten
sentiment_order = ['Positive', 'Neutral', 'Negative']
sentiment_options = [s for s in sentiment_order if s in df['sentiment'].unique()]
selected_sentiment = st.selectbox("📌 Pilih Sentimen:", sentiment_options)

# Filter data
filtered_df = df[df['sentiment'] == selected_sentiment]

# Gabungkan dan bersihkan teks
all_text = " ".join(filtered_df['translated_review'].astype(str).str.lower())
stopwords = set(STOPWORDS)
wordcloud = WordCloud(
    width=800, height=400, background_color='white', colormap='viridis',
    stopwords=stopwords, max_words=200
).generate(all_text)

# Layout tampilan
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📌 Insight Awal")
    if selected_sentiment == "Positive":
        st.markdown("- Banyak kata positif seperti 'easy', 'great', 'love', dan 'helpful'.")
    elif selected_sentiment == "Neutral":
        st.markdown("- Kata-kata cenderung informatif seperti 'app', 'use', atau 'work'.")
    else:
        st.markdown("- Sering muncul kata negatif seperti 'bad', 'crash', 'problem', dan 'slow'.")

with col2:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

st.caption("🔍 WordCloud ini menggunakan hasil *translated reviews*, sehingga kata-kata ditampilkan dalam Bahasa Inggris.")
