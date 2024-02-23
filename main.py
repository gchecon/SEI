import config as cf
import streamlit as st
import os


def listar_subdiretorios(diretorio_base):
    """Retorna uma lista com todos os subdiretórios dentro do diretório base."""
    subdiretorios_inner = [d for d in os.listdir(diretorio_base) if os.path.isdir(os.path.join(diretorio_base, d))]
    return subdiretorios_inner

def listar_arquivos(diretorio_inner):
    """Retorna uma lista com todos os arquivos dentro do diretório especificado."""
    arquivos_inner = [f for f in os.listdir(diretorio_inner) if os.path.isfile(os.path.join(diretorio_inner, f))]
    return arquivos_inner


if __name__ == '__main__':

    # Lista todos os subdiretórios dentro do diretório base
    subdiretorios = listar_subdiretorios(cf.DIR_BASE)

    st.set_page_config(page_title='Pendências SEI', layout='wide', page_icon=':page_with_curl:')

    option = st.sidebar.selectbox('Escolha uma opção:', subdiretorios)

    # Lista todos os arquivos no diretório escolhido
    caminho_completo = os.path.join(cf.DIR_BASE, option)
    arquivos = listar_arquivos(caminho_completo)
    st.write("Arquivos no diretório escolhido:")
    for arquivo in arquivos:
        st.write(arquivo)
