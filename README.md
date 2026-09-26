# Phishing Website Detection Using Machine Learning

## 📌 Project Overview

Phishing Website Detection Using Machine Learning is a web-based system that helps identify whether a given website URL is potentially a phishing website or a legitimate website.

The system extracts important features from the URL and uses a Machine Learning model to classify the website.

## 🎯 Objectives

- Detect potentially phishing websites.
- Classify URLs as Phishing or Legitimate.
- Use Machine Learning for automated URL classification.
- Provide a simple and user-friendly web interface.

## ⚙️ Features

- URL validation
- Phishing website detection
- Legitimate website detection
- Machine Learning based prediction
- Simple and user-friendly interface
- Web-based application

## 🛠️ Technologies Used

- Python
- Flask
- Machine Learning
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS

## 🤖 Machine Learning Model

The project uses a Random Forest Classifier for classification.

The model analyzes URL-based features such as:

- URL length
- Number of dots
- Number of hyphens
- Number of @ symbols
- Number of slashes
- Number of question marks
- Number of equal signs
- Number of percentage symbols
- Number of underscores

## 📊 Model Performance

The model achieved approximately **95.84% accuracy** on the held-out test dataset.

This result represents performance on the project's test split and does not guarantee the same accuracy on real-world websites.

## 🔄 How It Works

1. User enters a website URL.
2. The system validates the URL.
3. URL features are extracted.
4. The trained Machine Learning model analyzes the features.
5. The system displays the prediction:
   - Phishing Website
   - Legitimate Website

## 📁 Project Files

- `app.py` – Flask web application
- `feature_extraction.py` – Extracts URL features
- `train_model.py` – Trains the Machine Learning model
- `phishing_model.pkl` – Trained Random Forest model
- `dataset_small.csv` – Dataset used for training
- `requirements.txt` – Python dependencies
- `templates/index.html` – Web interface

## 🌐 Live Project

https://phishing-website-detection-zxto.onrender.com

## 🚀 Future Scope

- Improve detection using additional URL and domain features.
- Add larger and more diverse datasets.
- Explore advanced Machine Learning and Deep Learning models.
- Add browser extension support.
- Improve real-world detection performance.

## 📚 Project Type

B.Tech Computer Technology Final Year Project

## 👩‍💻 Author

Divya Girase
