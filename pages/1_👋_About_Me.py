import streamlit as st
import base64

with open("jihan_amalia.jpg", "rb") as img_file:
    img_bytes = img_file.read()
    img_base64 = base64.b64encode(img_bytes).decode()

profile_img_html = f"""
<div style="display: flex; justify-content: flex-end; margin-top: -40px;">
    <img src="data:image/jpeg;base64,{img_base64}" 
        alt="Profile Picture"
        style="width: 300px; height: 300px; object-fit: cover; border-radius: 50%; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
</div>
"""

col1, col2 = st.columns([2, 1])

with col2:
    st.markdown(profile_img_html, unsafe_allow_html=True)

with col1:
    st.markdown("<h2>👋 Hello, I’m <span style='color:#6C63FF;'>Jihan!</span></h2>", unsafe_allow_html=True)
    st.write("🌍 Based in **Jakarta, Indonesia**")
    st.write("🎓 Currently joining a **6-month Full Stack Data Science Bootcamp** with [dibimbing.id](https://dibimbing.id)")
    st.markdown("---")
    st.markdown("### 🧠 **Final Project Summary**")
    st.write("""
    ✅ Built machine learning to predict sentiment from user reviews.  
    ✅ Analyzed **40,414 reviews** from Google Play Store using customer segmentation & NLP.  
    ✅ Visualized insights and patterns in user behavior.
    """)
    st.markdown("📊 Dataset Source: [Kaggle - Google Play Store Apps](https://www.kaggle.com/lava18/google-play-store-apps)")
    st.markdown("📎 Project Slide Deck: [Google Slides](https://drive.google.com/file/d/15vKzdTrFNF9q3VB-NaBoReRg0uXaJ9kj/view?usp=sharing)")
    st.markdown("---")
    st.markdown("### 📬 **Contact Me**")
    st.write("""
    ✉️ Email: jihan.amalia02@gmail.com  
    🔗 [LinkedIn](https://www.linkedin.com/in/jihanamalia/) | [GitHub](https://github.com/Jhnamalia)
    """)
