import streamlit as st

def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Seleciona uma opçao',
        ['Inicio', 'Generos','Atores/Atrizes','Filmes','Avaliaçoes']
    )

    if menu_option == 'Inicio':
        st.write('Inicio')

    if menu_option == 'Generos':
        st.write('Inicio')

    if menu_option == 'Atores/Atrizes':
        st.write('Lista de atores/Atrizes')

    if menu_option == 'Filmes':
        st.write('Lista de Filmes')

    if menu_option == 'Avaliaçoes':
        st.write('Lista de avaliaçoes')
              
if __name__=='__main__':
    main()