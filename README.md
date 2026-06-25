# Movie-Recommendation-System

This is a Content-Based Movie Recommendation System built using Python, Pandas, and Scikit-learn. It recommends movies based on the similarity of their genres and plot overviews by converting text into numerical vectors using CountVectorizer and finding the closest matches with K-Nearest Neighbors (KNN) using Cosine Similarity.

## Features

- Content-based movie recommendations
- Data preprocessing using Pandas (handling missing values and combining text features)
- CountVectorizer for text vectorization
- KNN with Cosine Similarity
- Approximate title matching using `difflib` to handle spelling mistakes
- Interactive command-line interface

## Workflow

1. Load the movie dataset.
2. Create a **tags** feature by combining genre and overview.
3. Convert the text into vectors using **CountVectorizer**.
4. Train a **KNN** model with **Cosine Similarity**.
5. Take a movie name as input and find the closest match (if needed).
6. Recommend and display similar movies.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
