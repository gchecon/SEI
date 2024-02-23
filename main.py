import config as cf
import streamlit as st
from datetime import datetime
import os


def listar_subdiretorios(diretorio_base):
    """Retorna uma lista com todos os subdiretórios dentro do diretório base."""
    subdiretorios_inner = [d for d in os.listdir(diretorio_base) if os.path.isdir(os.path.join(diretorio_base, d))]
    return subdiretorios_inner


def listar_arquivos(diretorio_inner):
    """Retorna uma lista com todos os arquivos dentro do diretório especificado."""
    arquivos_inner = [f for f in os.listdir(diretorio_inner) if os.path.isfile(os.path.join(diretorio_inner, f))]
    return arquivos_inner


def adicionar_prefixo_data_hora(diretorio, arquivos_inner):
    """Adiciona um prefixo com a data e hora de criação a cada arquivo no diretório."""
    for arquivo_inner in arquivos_inner:
        caminho_arquivo = os.path.join(diretorio, arquivo_inner)
        # Obter o timestamp de criação do arquivo e converter para data/hora
        timestamp_criacao = os.path.getctime(caminho_arquivo)
        data_hora_criacao = datetime.fromtimestamp(timestamp_criacao)
        prefixo = data_hora_criacao.strftime('%Y%m%d_%H%M%S%f')[:-3]  # Remove os últimos 3 dígitos para milissegundos

        # Verificar se o arquivo já tem o prefixo
        if not arquivo_inner.startswith(prefixo):
            novo_nome = f"{prefixo}_{arquivo_inner}"
            novo_caminho = os.path.join(diretorio, novo_nome)
            os.rename(caminho_arquivo, novo_caminho)


if __name__ == '__main__':

    # Lista todos os subdiretórios dentro do diretório base
    subdiretorios = listar_subdiretorios(cf.DIR_BASE)

    st.set_page_config(page_title='Pendências SEI', layout='wide', page_icon=':page_with_curl:')

    option = st.sidebar.selectbox('Escolha uma opção:', subdiretorios)

    if st.sidebar.button('Renomear Arquivos'):
        dir_completo = os.path.join(cf.DIR_BASE, option)
        arquivos = listar_arquivos(dir_completo)
        adicionar_prefixo_data_hora(dir_completo, arquivos)
        st.success("Arquivos renomeados com sucesso!")
        arquivos_atualizados = listar_arquivos(dir_completo)

    # Lista todos os arquivos no diretório escolhido
    caminho_completo = os.path.join(cf.DIR_BASE, option)
    arquivos = listar_arquivos(caminho_completo)
    st.write("Arquivos no diretório escolhido:")
    for arquivo in arquivos:
        st.write(arquivo)
