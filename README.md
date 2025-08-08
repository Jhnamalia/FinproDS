📱 Final Project: App Sentiment Analysis Dashboard
Welcome to my Final Project as a Data Analyst, created as part of a full-stack Data Science Bootcamp. This interactive Streamlit dashboard analyzes user sentiment from Google Play Store app reviews and uses machine learning to predict sentiment from review text.

🔗 Live App: https://finalprojectds.streamlit.app

📌 Project Summary
Dataset: Google Play Store App Reviews (cleaned & preprocessed)
Size: 100,000+ app reviews with ratings, sentiment labels, and app metadata
Objective: Analyze sentiment patterns and build a sentiment classification model
Tools: Google Colab, VS Code, Streamlit, Plotly, Scikit-learn, Random Forest

🤖 Machine Learning Assets
Due to size limits on GitHub and Streamlit Cloud, model files are hosted on Google Drive:

rf_sentiment_model.pkl
📎 [Download](https://drive.google.com/file/d/1xJn2KEJ3VNt4ij9aoge45ZEtBrA-3ODQ/view?usp=drive_link)

tfidf_vectorizer.pkl
📎 [Download](https://drive.google.com/file/d/1xRFKwhVHVbMIPIAlGTO1COKwmhjJgnLY/view?usp=drive_link)

The app uses gdown to download these files at runtime.

📊 Dashboard Features
- 📈 Exploratory Data Analysis (EDA)
  - Sentiment distribution
  - Rating comparisons across app types (Free vs Paid)
  - Category-level trends and installs

- 🔍 Sentiment Prediction
  - Enter review text and get predicted sentiment
  - Based on trained Random Forest model (TF-IDF + metadata)

- ☁️ WordCloud Visualization
Top keywords per sentiment category
Cleaned with custom stopwords
