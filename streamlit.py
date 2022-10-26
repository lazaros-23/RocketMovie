from pandas_datareader import Options
from requests import options
import streamlit as st
import pandas as pd
import numpy as np
import random

st.markdown(" # **RocketMovie** Next Big Movie Prediction")
st.markdown("<h3 style='text-align: center; color: black;'>Helps Directors make better decision with Machine Learning. 🤖  </h2>", unsafe_allow_html=True)

@st.cache
def get_actors():
    df = pd.read_csv('actor_dataset.csv', sep=';')
    actors = list(set(df['actor_1']))
    return actors
def get_genre():
    df = pd.read_csv('movie_dataset.csv',sep =';')
    df['genre'] = df['genres'].apply(lambda x: x.replace(' ', "").split('|')[0])
    return list(set(df['genre']))

actors = get_actors()
genre = get_genre()

st.multiselect('Choose Genre', options=genre)
st.multiselect('Choose up to 10 actors with the right order', options=actors)
budget = st.slider('Production Budget (In Millions)', min_value=10, max_value=1000, value=40, step=1)
st.date_input('Release Date?')

if st.button('predict'):
    revenue = budget *random.uniform(0.5, 2)
    st.markdown(f' ## The Estimated Gross World Wide Revenue will be **{round(revenue,2)} Millions**')