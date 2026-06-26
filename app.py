import streamlit as st
import pickle
from difflib import get_close_matches

# Load pickle files
movies = pickle.load(open("movies.pkl", "rb"))
vector = pickle.load(open("vector.pkl", "rb"))
knn = pickle.load(open("knn.pkl", "rb"))

# Recommendation Function
def recommend(movie):
    try:
        movie_list = movies['title'].tolist()
        match = get_close_matches(movie, movie_list, n=1, cutoff=0.6)
        if not match:
            return None, []
        movie = match[0]
        movie_index = movies[movies['title'] == movie].index[0]
        movie_vector = vector[movie_index].reshape(1, -1)
        _, indices = knn.kneighbors(movie_vector)
        indices = indices.flatten()
        recommendations = []
        for i in range(1, len(indices)):
            recommendations.append(movies.iloc[indices[i]].title)
        return movie, recommendations
    except IndexError:
        return None, []


# Streamlit 
st.set_page_config(page_title="Movie Recommendation System")
st.title("Movie Recommendation System")
movie_name = st.text_input("Enter Movie Name")
if st.button("Recommend"):
    movie, recommendations = recommend(movie_name)
    if movie is None:
        st.error("Movie not found in the dataset.")
    else:
        st.success(f"Recommendations for '{movie}'")
        for rec in recommendations:
            st.write(f"{rec}")