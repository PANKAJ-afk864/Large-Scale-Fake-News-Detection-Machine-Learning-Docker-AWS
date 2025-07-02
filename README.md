#  Fake News Detection using Machine Learning, Streamlit, Docker & AWS

This project is a full-stack fake news classification system using machine learning and deployed on the cloud. It allows users to input a news article and instantly get a prediction whether it's **FAKE** or **REAL** — all through a web interface powered by **Streamlit**, containerized with **Docker**, and hosted on an **AWS EC2 instance**.

---

## 🚀 Live Demo

🌐 **Hosted on EC2:**  
 [http://13.60.31.230:8501](http://13.60.31.230:8501)

---

##  Features

-  Detects Fake vs Real news using Logistic Regression
-  Trained on Kaggle Fake & True news datasets
-  TF-IDF text vectorization
-  Clean UI built with Streamlit
-  Dockerized for easy deployment
-  Hosted on AWS EC2 with public IP access

---

##  Tech Stack

| Layer        | Tools / Tech Used                  |
|--------------|------------------------------------|
| Machine Learning | Scikit-learn, Pandas, Numpy         
| Web UI       | Streamlit                          |
| Vectorizer   | TF-IDF (scikit-learn)              |
| Container    | Docker                             |
| Deployment   | AWS EC2 Ubuntu Instance            |

---

## Project Structure

├── streamlit_app.py # Streamlit frontend
├── fake_news_model.pkl # Trained ML model
├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
├── requirements.txt # Python dependencies
├── Dockerfile # Docker config for deployment
└── README.md # This file

## Screenshot
![App Screenshot]![](Screenshot.png)

## How to Run Locally (Without Docker)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py

## Model Performance

| Metric    | Score   |
| --------- | ------- |
| Accuracy  | 98.7%  |
| Precision | 98.5%  |
| Recall    | 98.9%  |

## Connect With Me
👤 Pankaj Kumar Singh
🔗 https://github.com/PANKAJ-afk864
