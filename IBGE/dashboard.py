import json
import requests
import pandas as pd
import numpy as np
import streamlit as st


# Função de períodos:
def periodos(metadados):
    # Criando um array de períodos com base nos metadados
    periodos = np.arange(metadados['periodicidade']['inicio'], metadados['periodicidade']['fim'])
    if len(periodos) == 0:
        st.write(f"Dados disponíveis apenas no período: :green[{metadados['periodicidade']['inicio']}]")
        periodos_checl = {metadados['periodicidade']['inicio']: True}
    else: 
        with st.expander("Períodos:"):
            periodos_checks = {}

            # Estado inicial para selecionar/desselecionar todos
            select_all = st.checkbox(":gray[Selecionar Tudo]:", value=True)

            # Criando 4 colunas
            cols = st.columns(4)

            # Adicionando checkboxes nas colunas de forma sequencial
            for i, periodo in enumerate(periodos):
                col_index = i % 4  # Determina a posição de forma horizontal
                with cols[col_index]:
                    # Adiciona o checkbox à coluna correspondente, controlado pelo estado do select_all
                    checked = st.checkbox(f"{periodo}", value=select_all)
                    periodos_checks.update({periodo: checked})





# título do dashboard
st.title("Dashboard de análise de dados IBGE:")

# Requisição dos dados
ibge = "https://servicodados.ibge.gov.br/api/v3/agregados"
resposta = requests.get(ibge)

# Dicionário contendo os principais assuntos:
dicionario = {}
temas = resposta.json()
for i, item  in enumerate(temas):
    text = json.dumps(item)
    dic = json.loads(text)
    dicionario[i] = dic

# Exposição dos identificadores dos dados contidos nos endpoints da API
st.header("Identificadores dos dados agregados  IBGE", anchor="identificadores", divider=True)

# Identifica as opções de assunto de consulta
options = [dicionario[key]["nome"] for key in dicionario.keys()]
# Cria um SelecBox com os assuntos
assunto = st.selectbox(f"Assunto que deseja pesquisar: :green[{len(options)}]", options)
# Encontra o index do assunto selecionado e usa isso para alimentar o select de agregados
id_assunto = options.index(assunto)

indexes = [] # Lista para indexar o agregado ao seu código IBGE
options_agr = [] # Lista para o select box
for i, item in enumerate(dicionario[id_assunto]["agregados"]):
    nome = item["nome"]
    id = item["id"]
    indexes.append(id)
    options_agr.append(f"{id} - {nome}")

elemento = f":green[{len(options_agr)}]"
agregados = st.selectbox(f"Datasets disponíveis para obtenção de dados: [{elemento}]", options_agr)
id_escolhido = agregados.split(" - ")[0]

st.subheader("Metadados")
# Requisição dos metadados do agregado
url_metadados = f"https://servicodados.ibge.gov.br/api/v3/agregados/{id_escolhido}/metadados"
resposta_metadados = requests.get(url_metadados)
if resposta_metadados.status_code == 200:
    metadados = resposta_metadados.json()
    st.write(metadados['nome'])

    if metadados['periodicidade']['frequencia'] == 'anual':
        periodos(metadados)

    with st.expander("Metadados"):
        st.write(metadados)
        st.markdown(f"URL: {url_metadados}")
else: 
    elemento = f""
    st.markdown(f"Metadados não encontrados [:red[{resposta_metadados.status_code}]]")
    st.markdown(f"Tentativa de comunicação por: {url_metadados}")


