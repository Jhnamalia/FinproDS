import streamlit as st

st.set_page_config(
    page_title="Uncovering Sentiment Patterns in Google Play Store",
    page_icon="📱",
    layout="wide"
)

# Halaman utama
st.title("📱Uncovering Sentiment Patterns in Google Play Store")
st.header('Data Science Final Project')
st.markdown("---")

st.markdown("""
Selamat datang di aplikasi **Analisis Sentimen**!  
Aplikasi ini dirancang untuk menganalisis ulasan pengguna terhadap aplikasi di Google Play Store.

### 📂 Navigasi Halaman:
- **📊 EDA & Visualisasi**: Eksplorasi data, distribusi rating, install, kategori, dan hubungan dengan sentimen pengguna.
- **🔍 Prediksi Sentimen**: Coba input review dan lihat prediksi sentimennya.
- **☁️ WordCloud**: Lihat visualisasi kata-kata dominan dari review berdasarkan sentimen.

---
Silakan pilih halaman di sidebar kiri untuk mulai eksplorasi 📈.
""")
