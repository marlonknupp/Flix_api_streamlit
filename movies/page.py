import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [ 
    {
        'id': 1,
        'name': 'Harry Potter 2'
    },
    {
        'id': 2,
        'name': 'O vingador do futuro'
    },
    {
        'id': 3,
        'name': 'Os fantamas se divertem'
    },
]

def show_movies():
    st.write('Lista de Filmes:')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )