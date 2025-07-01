import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# App title
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detection App")
st.markdown("Detect whether a news article is **Real** or **Fake** using NLP and ML.")

# Input form
news_input = st.text_area("✏️ Paste your news article text here:", height=200)

# Prediction
if st.button("🔍 Predict"):
    if news_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vectorized_input = vectorizer.transform([news_input])
        prediction = model.predict(vectorized_input)[0]
        result = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
        st.success(f"**Prediction:** {result}")
