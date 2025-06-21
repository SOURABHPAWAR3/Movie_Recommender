# test.py

from src.recommender import recommend

movie = "Toy Story (1995)"
print(f"\n🎬 Recommendations for '{movie}':")
recommendations = recommend(movie)
for i, title in enumerate(recommendations, 1):
    print(f"{i}. {title}")
