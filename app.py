import pandas as pd
import requests
import streamlit as st
import pickle

st.title("movie recommendation system")


from dotenv import load_dotenv
import os

load_dotenv()

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}",
        "accept": "application/json"
    }
    # Your request code here

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Safely get 'poster_path'
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "No poster available for this movie."
    else:
        return f"Error: {response.status_code} - {response.reason}"


def recommend(movie):
    recommened_movies=[]
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]#fecth the array of distances of that movie
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]#gets a sorted array of distances along with their orginal indx
    posters=[]
    for i in movies_list:#returns index
        movie_id=movies.iloc[i[0]].movie_id
        recommened_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommened_movies,posters

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

import streamlit as st


if st.button("Recommend"):
    names,poster=recommend(selected_movie)
    import streamlit as st

    col1, col2, col3,col4,col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
