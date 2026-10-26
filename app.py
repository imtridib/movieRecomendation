import os
import pickle
import streamlit as st
import requests
import pandas as pd

# Set TMDB_API_KEY in your environment; never hard-code API credentials.
API_KEY = os.getenv("TMDB_API_KEY", "")


def fetch_poster(movie_id):
    if not API_KEY:
        return "https://via.placeholder.com/500x750?text=Set+TMDB_API_KEY"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    try:
        response = requests.get(
            url,
            params={"api_key": API_KEY, "language": "en-US"},
            timeout=10,
        )
        response.raise_for_status()
        poster_path = response.json().get("poster_path")
    except requests.RequestException:
        return "https://via.placeholder.com/500x750?text=Poster+Unavailable"

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    if movie not in movies["title"].values:
        return [], []

    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        enumerate(similarity[index]), reverse=True, key=lambda item: item[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []
    for item in distances[1:6]:
        movie_id = movies.iloc[item[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[item[0]].title)

    return recommended_movie_names, recommended_movie_posters


st.header("🎬 Movie Recommender System")

with open("movie_dict.pkl", "rb") as movie_file:
    movies_dict = pickle.load(movie_file)
movies = pd.DataFrame(movies_dict)

with open("similarity.pkl", "rb") as similarity_file:
    similarity = pickle.load(similarity_file)

if not API_KEY:
    st.info(
        "Set the TMDB_API_KEY environment variable to load real movie posters. "
        "Recommendations can still be generated, but poster images will use placeholders."
    )

movie_list = movies["title"].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)
    if names:
        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.text(name)
                st.image(poster)
