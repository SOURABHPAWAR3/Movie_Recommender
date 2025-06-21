# src/recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load processed data
movie_data = pd.read_csv("data/movie_data.csv")
similarity = pd.read_csv("data/similarity_matrix.csv").values

def recommend(movie_title, top_n=5):
    if movie_title not in movie_data['title'].values:
        return f"❌ Movie '{movie_title}' not found in dataset."

    index = movie_data[movie_data['title'] == movie_title].index[0]
    distances = similarity[index]

    # Get indices of top N most similar movies (excluding the movie itself)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:top_n+1]

    recommended_titles = [movie_data.iloc[i[0]].title for i in movie_list]
    return recommended_titles
