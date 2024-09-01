import json
import requests
import pandas as pd
import streamlit as st

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
    
    with st.expander("Visualizar"):
        st.write(metadados)
        st.markdown(f"URL: {url_metadados}")
else: 
    elemento = f""
    st.markdown(f"Metadados não encontrados [:red[{resposta_metadados.status_code}]]")
    st.markdown(f"Tentativa de comunicação por: {url_metadados}")


