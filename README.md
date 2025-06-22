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
