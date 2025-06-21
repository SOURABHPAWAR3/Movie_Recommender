# 🎬 Movie Recommender

A smart movie recommendation system that helps you discover similar movies based on what you already like — built with Python, React, Flask, and Machine Learning.

💡 **"Type in a movie title, get 5 intelligent recommendations in a blink!"**

---

## ✨ Features

✅ Content-based movie recommendation using cosine similarity  
✅ Simple and elegant React frontend with real-time movie search  
✅ Python + Flask backend API serving fast recommendations  
✅ Local dataset — no external API required  
✅ Easily extendable to include posters, genres, ratings & more

---

## 🚀 How It Works

1. Enter a movie title (e.g., **Toy Story (1995)**)
2. The backend locates the movie index from `movie_data.csv`
3. It fetches similar movies using a precomputed **cosine similarity matrix**
4. Top 5 most similar movie titles are returned and shown in the UI

---

## ⚙️ Tech Stack

| Layer     | Technology            |
|-----------|------------------------|
| Frontend  | Vite + React.js        |
| Backend   | Flask (Python)         |
| ML Engine | Cosine Similarity (Scikit-learn) |
| Data      | CSV files (MovieLens small dataset) |

---


