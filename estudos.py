import streamlit as st
import queries as q
import pandas as pd


st.title('Orçamento')

with st.container(border=True):
    st.title('Utilização Orçamentária')

    linha1 = st.columns(2)
    linha2 = st.columns(2)

    queries = [
        'SELECT "Sistema", "Custo_OS" FROM "Custo_Sistemas" WHERE "Ano_Pagto" = 2024',
        'SELECT sistema, custo_os FROM custo_sistemas___dsis_custo_de_sistemas WHERE ano_pagto = 2024',
        'SELECT "dcf_orçado", dcf_executado FROM "pagamentos_dti_orçamento" WHERE ano = 2024',
        'SELECT contrato, valor FROM pagamentos_dti_pagamentos WHERE ano = \'2024\''
    ]

    colunas = linha1 + linha2
    print(f'Tipo Linha: {type(linha1)} com {len(linha1)}\nTipo Coluna: {type(colunas)} com {len(colunas)}')

    for coluna, query in zip(colunas, queries):
        data = q.query_data(query)
        coluna.dataframe(data)
