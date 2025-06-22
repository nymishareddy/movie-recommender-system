import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB Poster API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=468f187460b095bde8c7b2224551cd31&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', "")

# Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_titles = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_titles, recommended_posters

# Page config
st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
        }
        .stButton>button {
            background-color: #e50914;
            color: white;
            border: none;
            padding: 10px 24px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #bf0810;
        }
        .css-1cpxqw2 {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown('<h1 style="text-align:center; color:white;">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)
st.markdown("### ")

# Movie select
st.markdown("<h4 style='color:white;'>Search for a movie you like:</h4>", unsafe_allow_html=True)
selected_movie = st.selectbox('', movies['title'].values)


# Recommend button
if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"<h5 style='color:white;text-align:center'>{names[i]}</h6>", unsafe_allow_html=True)
            st.image(posters[i])
