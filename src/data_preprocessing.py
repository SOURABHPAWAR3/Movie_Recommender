import pandas as pd
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def preprocess_movie_data(path="data/ml-latest-small/movies.csv"):
    """
    Load and preprocess the movies dataset.
    - Replaces '|' with space in genres to create 'tags'
    - Normalizes text (lowercase, clean chars)
    - Drops NaNs and duplicates
    """
    try:
        movies = pd.read_csv(path)
        logging.info("🎬 Movies dataset loaded successfully.")

        # Replace '|' with space and normalize tags
        movies['tags'] = (
            movies['genres']
            .str.replace('|', ' ', regex=False)
            .str.lower()
            .str.replace(r'[^a-z\s]', '', regex=True)
        )

        # Select necessary columns
        movie_data = movies[['movieId', 'title', 'tags']]
        movie_data.dropna(subset=['tags'], inplace=True)
        movie_data.drop_duplicates(subset=['movieId'], inplace=True)

        logging.info("✅ Preprocessing completed. Sample:")
        logging.info("\n%s", movie_data.head())

        return movie_data

    except Exception as e:
        logging.error("❌ Error during preprocessing: %s", e)
        return pd.DataFrame()


def compute_similarity_matrix(movie_data):
    """
    Vectorize 'tags' using CountVectorizer and compute cosine similarity.
    Returns the vector matrix and similarity matrix.
    """
    try:
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(movie_data['tags']).toarray()
        similarity = cosine_similarity(vectors)
        logging.info("📊 Vectorization and similarity matrix computed. Shape: %s", similarity.shape)
        return vectors, similarity
    except Exception as e:
        logging.error("❌ Error in vectorization/similarity computation: %s", e)
        return None, None


def save_outputs(movie_data, similarity_matrix, movie_data_path="data/movie_data.csv", similarity_path="data/similarity_matrix.csv"):
    """
    Save the preprocessed movie data and similarity matrix to CSV.
    """
    try:
        movie_data.to_csv(movie_data_path, index=False)
        pd.DataFrame(similarity_matrix).to_csv(similarity_path, index=False)
        logging.info("💾 Outputs saved to %s and %s", movie_data_path, similarity_path)
    except Exception as e:
        logging.error("❌ Error saving outputs: %s", e)


if __name__ == "__main__":
    # Full pipeline
    movie_df = preprocess_movie_data()

    if not movie_df.empty:
        vectors, similarity_matrix = compute_similarity_matrix(movie_df)
        if similarity_matrix is not None:
            save_outputs(movie_df, similarity_matrix)
