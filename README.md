# Spotify Music Recommendation System

This project was developed as part of the **Machine Learning I (ADSP 31017 IP09)** course at the University of Chicago, Winter Quarter 2025. It explores clustering, popularity prediction, and recommendation system development using audio and textual features from Spotify tracks.

## 🎯 Objective
To develop a machine learning-based system that:
1. Clusters songs by audio characteristics
2. Predicts a song’s popularity
3. Recommends similar songs using content-based filtering

## 📚 Dataset
- **Source**: [Kaggle - Top 10,000 Spotify Songs (1960–Now)](https://www.kaggle.com/datasets/joebeachcapital/top-10000-spotify-songs-1960-now/)
- Includes metadata, audio features (e.g., tempo, energy), and popularity scores.

## 📁 Project Structure

Spotify_Recommendation_System/ ├── data/ │ └── top_10000_1960-now.csv ├── docs/ │ └── Team Presentation.pdf └── notebooks/ ├── Data Cleaning.ipynb ├── RecommendationSystem_v2.ipynb ├── Song Clustering.ipynb └── Team6_Spotify_prediction.ipynb


## 🧠 Methodology

### 1. Song Clustering
- Applied **K-Means Clustering** to group songs by audio features.
- Evaluated cluster quality by balance and separation.

### 2. Popularity Prediction
- Converted popularity scores into binary labels (≥50 = popular).
- Models used:
  - Logistic Regression
  - Random Forest
  - XGBoost, LightGBM, Gradient Boosting
  - SVM
- Best model: **LightGBM**, with high recall but modest precision.

### 3. Recommendation System
- Used **cosine similarity** for content-based filtering:
  - **Audio features** (65% weight)
  - **Lyrics embedding** (25% weight, BERT-based)
  - **Artist information** (10% weight)
- Preprocessing included feature scaling, embedding (TF-IDF, Word2Vec, BERT), and normalization.

## 📊 Evaluation
- Recommendation quality assessed by:
  - Balanced similarity distribution (avoiding over-concentration)
  - Qualitative checks on song recommendations
- Classification models evaluated using precision, recall, F1, and ROC-AUC.

## 💡 Business Value
- Helps Spotify predict hits and personalize user experience
- Supports marketing for emerging artists
- Drives user engagement and satisfaction

## 📄 References
- Course: ADSP 31017 IP09 Machine Learning I
- University of Chicago Physical Sciences Division
"""
