import json
import requests
import pandas as pd
import numpy as np
import streamlit as st

def metadados(cod_agregado = None):
    # Requisição dos metadados do agregado
    url_metadados = f"https://servicodados.ibge.gov.br/api/v3/agregados/{cod_agregado}/metadados"

    resposta_metadados = requests.get(url_metadados)
    if resposta_metadados.status_code == 200:
        metadados = resposta_metadados.json()
        with st.expander("Metadados", expanded=True):
            st.markdown(f"URL: {url_metadados}")
            st.json(metadados)
    else: 
        st.markdown(f"Metadados não encontrados [:red[{resposta_metadados.status_code}]]")
        st.markdown(f"Comunicação por: {url_metadados}")

def variaveis(cod_agregado = None):
    # Requisição dos metadados do agregado
    url_metadados = f"https://servicodados.ibge.gov.br/api/v3/agregados/{cod_agregado}/metadados"

    resposta_metadados = requests.get(url_metadados)
    if resposta_metadados.status_code == 200:
        metadados = resposta_metadados.json()

        with st.expander("Variáveis", expanded=True):
            df = pd.DataFrame(metadados["variaveis"], dtype=str)
            df['id'] = df['id'].astype(str)

            # Capitalizar a primeira letra de cada nome de coluna
            df.columns = [col.upper() for col in df.columns]
            st.table(df.iloc[:, 0:2])
    else: 
        st.markdown(f"Variáveis não encontradas [:red[{resposta_metadados.status_code}]]")
        st.markdown(f"Comunicação por: {url_metadados}")

# Função de períodos:
def periodos(cod_agregado = None):
    # Requisição dos metadados do agregado
    url_metadados = f"https://servicodados.ibge.gov.br/api/v3/agregados/{cod_agregado}/metadados"

    resposta_metadados = requests.get(url_metadados)
    if resposta_metadados.status_code == 200:
        metadados = resposta_metadados.json()
        # Criando um array de períodos com base nos metadados
        periodos = np.arange(metadados['periodicidade']['inicio'], metadados['periodicidade']['fim'])
        if len(periodos) == 0:
            st.write(f"Dados disponíveis apenas no período: :green[{metadados['periodicidade']['inicio']}]")
            periodos_checl = {metadados['periodicidade']['inicio']: True}
        else: 
            with st.expander("Períodos:", expanded=True):
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

#----------------------------------------------------------------
#----------------------------------------------------------------
st.title("Dashboard de análise de dados IBGE:")
#----------------------------------------------------------------

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

#----------------------------------------------------------------
st.header("Informações", anchor="Seletor", divider=True)
seletor = st.multiselect(
    "Dados disponíveis:",
    ["Variáveis","Metadados","Períodos", "Folium - dados Geoespciais"]
)

for s in seletor:
    if s == "Metadados":
        metadados(cod_agregado=id_escolhido)
    elif s == "Variáveis":
        variaveis(cod_agregado=id_escolhido)
    elif s == "Períodos":
        periodos(cod_agregado=id_escolhido)



#url_view = "https://servicodados.ibge.gov.br/api/v3/agregados/706/variaveis?view=OLAP&localidades=BR"
#res_view = requests.get(url_view)
#view = res_view.json()
#st.write(view)

#url_view = "https://servicodados.ibge.gov.br/api/v3/agregados/706/variaveis?view=flat&localidades=BR"

