# official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY streamlit_app.py .
COPY fake_news_model.pkl .
COPY tfidf_vectorizer.pkl .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
