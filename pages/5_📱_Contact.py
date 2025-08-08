import streamlit as st

# --- Setup halaman ---
st.set_page_config(page_title="Contact", layout="centered")

st.markdown("## 🤝 Let's Connect!")
st.markdown(
    """
    I'm always open to collaboration, feedback, or just a friendly chat.  
    Feel free to reach out through any of the platforms below:
    """
)

# --- Kontak Utama ---
st.markdown("### 🔗 Social & Contact Info")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        🔹 [**LinkedIn**](https://www.linkedin.com/in/jihanamalia/)  
        [![LinkedIn Badge](https://img.shields.io/badge/-Jihan_Amalia-blue?logo=linkedin&style=flat)](https://www.linkedin.com/in/jihanamalia/)

        🐙 [**GitHub**](https://github.com/Jhnamalia)  
        [![GitHub Badge](https://img.shields.io/badge/-Jhnamalia-181717?logo=github&style=flat)](https://github.com/Jhnamalia)
        """
    )

with col2:
    st.markdown(
        """
        📱 [**WhatsApp**](https://wa.me/6282217802091)  
        Klik untuk langsung menghubungi via WhatsApp
        """
    )

# --- Email ---
st.markdown("### 📧 Email")
st.markdown("📩 **[jihan.amalia02@gmail.com](mailto:jihan.amalia02@gmail.com)**")

# --- Footer ---
st.markdown("---")
st.info("Looking forward to hearing from you! 😊")