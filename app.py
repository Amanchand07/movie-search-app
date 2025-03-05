import streamlit as st
import requests


API_KEY = "YOUR_OMDB_API_KEY"
BASE_URL = "http://www.omdbapi.com/"


def fetch_movies(query):
    params = {"s": query, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data.get("Search", [])  


def fetch_movie_details(imdb_id):
    params = {"i": imdb_id, "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.json()


st.title("🎬 Movie Search App")
st.write("Search for movies using the OMDb API.")


query = st.text_input("Enter movie title:", "")

if query:
    movies = fetch_movies(query)
    
    if movies:
        for movie in movies:
            col1, col2 = st.columns([1, 3])
            
            
            with col1:
                st.image(movie.get("Poster", ""), width=120)
            
            
            with col2:
                st.subheader(movie["Title"])
                st.write(f"Year: {movie['Year']}")
                
                if st.button(f"More about {movie['Title']}", key=movie["imdbID"]):
                    movie_details = fetch_movie_details(movie["imdbID"])
                    st.subheader(movie_details["Title"])
                    st.write(f"**Year:** {movie_details['Year']}")
                    st.write(f"**Genre:** {movie_details['Genre']}")
                    st.write(f"**Director:** {movie_details['Director']}")
                    st.write(f"**Actors:** {movie_details['Actors']}")
                    st.write(f"**Plot:** {movie_details['Plot']}")
                    st.write(f"**IMDB Rating:** {movie_details['imdbRating']}")
                    st.image(movie_details["Poster"], width=200)

    else:
        st.write("No movies found. Try another search term.")
