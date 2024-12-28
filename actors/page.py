import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [ 
    {
        'id': 1,
        'name': 'Leonardo di caprio'
    },
    {
        'id': 2,
        'name': 'The Rock'
    },
    {
        'id': 3,
        'name': 'Stallone'
    },
]

def show_actors():
    st.write('Lista de Ator/Atriz:')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/atriz "{name}" cadastrado com sucesso!')