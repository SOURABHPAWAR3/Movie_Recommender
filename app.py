from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for all routes

# Load your movie data and similarity matrix
movies = pd.read_csv('data/movie_data.csv')
similarity = np.loadtxt('data/similarity_matrix.csv', delimiter=',')

@app.route('/')
def home():
    return "🎬 Movie Recommendation API is running!"

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get movie name from query parameter
    movie_name = request.args.get('movie')

    if not movie_name:
        return jsonify({'error': 'No movie provided'}), 400

    # Check if movie exists in the dataset
    if movie_name not in movies['title'].values:
        return jsonify({'error': 'Movie not found'}), 404

    # Get index of movie
    idx = movies[movies['title'] == movie_name].index[0]

    # Get similarity scores and top 5 recommendations
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommendations = [movies.iloc[i[0]].title for i in scores]

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
