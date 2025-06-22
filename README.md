**🎬 Movie Recommendation System 🎬**

A **Machine Learning** based content filtering movie recommendation system that suggests the top 5 movies similar to a given title. It leverages movie metadata (genres, keywords, cast, overview, crew) to create a "tags" field, applies text processing (tokenization and stemming), vectorizes the tags with `CountVectorizer`, and computes cosine similarity to find the most similar films.

---

## 🚀 Features

* 🔍 **Input:** User selects or types a movie title from a searchable dropdown of \~5,000 movies
* 📊 **Processing:**

  * Combines metadata into a unified "tags" string per movie
  * Applies Porter Stemmer to normalize tokens
  * Vectorizes tag strings with `CountVectorizer` (max 5,000 features)
  * Computes pairwise cosine similarity
* 🎁 **Output:** Displays the top 5 recommended movies with titles and posters in a dark-themed, responsive Streamlit interface

---
⚙️ How It Works

Data Preparation (in the Jupyter notebook):

Load CSVs (tmdb_5000_movies.csv, tmdb_5000_credits.csv)

Parse and extract lists for genres, keywords, cast, crew

Combine overview, genres, keywords, cast, crew into a single tags string

Apply stemming with NLTK's Porter Stemmer

Save final DataFrame as movies.pkl

Vectorize tags with CountVectorizer → produce vectors array

Compute cosine similarity matrix → save as similarity.pkl

Recommendation (in app.py):

User selects a movie title

Lookup its index in movies.pkl

Retrieve similarity scores and sort descending

Fetch top 5 recs, use TMDB API to get poster URLs

Display in a horizontal Streamlit layout with styled CSS
