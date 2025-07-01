from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# FastAPI instance
app = FastAPI()

# Request body structure
class NewsRequest(BaseModel):
    text: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Fake News Detection API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict_news(news: NewsRequest):
    vectorized_text = vectorizer.transform([news.text])
    prediction = model.predict(vectorized_text)[0]
    result = "Real News" if prediction == 1 else "Fake News"
    return {"prediction": result}
