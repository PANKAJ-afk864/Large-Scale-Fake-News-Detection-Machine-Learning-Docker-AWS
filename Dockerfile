# official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY app/ ./app/
COPY fake_news_model.pkl .
COPY tfidf_vectorizer.pkl .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
