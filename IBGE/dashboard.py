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
            st.table(df.iloc[:, 0:3])
    else: 
        st.markdown(f"Variáveis não encontradas [:red[{resposta_metadados.status_code}]]")
        st.markdown(f"Comunicação por: {url_metadados}")

def documentacao():
    documentacao = {
    "id": "Identificador do agregado",

    "nome": "Nome do agregado",

    "URL": "Página do Agregado no portal do SIDRA",

    "pesquisa": "Pesquisa a que pertence o agregado",

    "assunto": "Assunto informado pelo agregado",

    "periodicidade": {"frequencia":"Frequência na qual são coletados os dados do agregado. Caso a frequência seja mensal, o formato do período seguirá o padrão YYYYMM, no qual YYYY refere-se ao ano e MM ao mês", "inicio":"Período inicial da coleta dos dados", "fim":"Último período coletado"},

    "nivelTerritorial": {"Administrativo":"Quando o agregado abranger divisão político-administrativa do Brasil. Pode assumir os seguintes valores: N1 (Brasil), N2 (Região), N3 (Unidade da Federação), N8 (Mesorregião), N9 (Microrregião), N7 (Região metropolitana), N6 (Município), N10 (Distrito), N11 (Subdistrito), N102 (Bairro), N15 (Aglomeração urbana), N14 (Região Integrada de Desenvolvimento), N13 (Região metropolitana e subdivisão)", "Especial":"Quando o agregado abranger divisão de natureza especial. Pode assumir os seguintes valores: N17 (Aglomerado subnormal), N23 (Arranjo populacional), N101 (País do Mercosul, Bolívia e Chile), N104 (Argentina), N105 (Uruguai), N106 (Paraguai), N107 (Departamento - Paraguai), N108 (Departamento - Uruguai), N109 (Província), N111 (Unidade Federativa do Mercosul, Bolívia e Chile), N123 (Bioma), N124 (Corpo d'água), N125 (Terra indígena), N126 (Unidade de Conservação Ambiental), N127 (Núcleo de desertificação), N128 (Praia), N129 (Territórios da cidadania), N131 (Amazônia Legal), N132 (Semiárido), N133 (Semiárido de Unidade da Federação), N134 (Amazônia Legal de Unidade da Federação)", "IBGE":"Quando o agregado abranger divisão específica do IBGE. Pode assumir os seguintes valores: N18 (Área de Ponderação), N19 (Área de Ponderação Recalculada), N20 (Área de Divulgação da Amostra para Aglomerados Subnormais), N21 (Total dos municípios das capitais da Grande Região), N22 (Total dos municípios das capitais), N103 (Total das áreas - POF), N110 (Total das áreas - PME), N122 (Grande Região - PIMES), N130 (Capital / Não Capital de Unidade da Federação), N1100 (Brasil, sem especificação de Unidade da Federação), N1101 (Ignorado), N1102 (Estrangeiro), N1103 (Total), N1104 (Unidade da Federação, sem especificação de Município), N1105 (Área de influência - PNSB)"},

    "variaveis": {"id":"Identificador da variável", "nome":"Nome da variável", "unidade":"Unidade da variável", "sumarizacao":"Informa qual dimensões podem ser sumarizadas - Por exemplo, se você somar os resultados das variáveis referentes às Unidades da Federação, obterá o resultado do Brasil. Da mesma forma, se você somar resultados das variáveis referentes aos meses do ano, obterá o resultado do respectivo ano. Valores possíveis são nivelTerritorial e periodo"},
    "classificacoes": {"id":"Identificador da classificação", "nome":"Nome da classificação",
    "sumarização": ["Equivalente a propriedade variaveis.sumarização, exceto pelo fato que esta refere-se à soma das categorias",{"status":"nforma se a categoria Total, obtida neste caso a partir da soma das demais categorias, pode ser usada para retornar o valor de, pelo menos, uma variável", "excecao":"Informa os identificadores das variáveis para as quais não são considerados a categoria Total. Na prática, significa que você deve especificar uma categoria que não seja a (categoria) Total para obter o valor da variável"}], "categorias": {"id":"Identificador da categoria", "nome":"Nome da categoria", "unidade":"Unidade da categoria. Pode assumir valor null", "nivel":"As categorias podem estar agrupadas hierarquicamente, assim como as regiões do Brasil - Brasil -> Grandes regiões -> Unidades da Federação (estados) -> Mesorregiões -> Microrregiões -> Municípios - ou logicamente - Por exemplo, agregado 1713 -, para fins de organização. Nesse caso, a propriedade nivel informa o nível hierárquico em que se encontra a categoria, sendo o primeiro nível 0, o segundo 1, e assim sucessivamente"}}
    }
    with st.expander("Documentação:", expanded=True):
        st.write(documentacao)

# Função de períodos:
def periodos(cod_agregado = None):
    # Requisição dos metadados do agregado
    url_metadados = f"https://servicodados.ibge.gov.br/api/v3/agregados/{cod_agregado}/periodos/"
    

    resposta_metadados = requests.get(url_metadados)
    if resposta_metadados.status_code == 200:
        periodos = resposta_metadados.json()
        if len(periodos) == 1:
            with st.expander("Períodos:", expanded=True):
                st.write(f"Dados disponíveis apenas no período: :green[{periodos[0]['id']}]")
        else: 
            with st.expander("Períodos:", expanded=False):
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
                        checked = st.checkbox(f"{periodo['id']}", value=select_all)
                        periodos_checks.update({periodo['id']: checked})

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
    ["Variáveis Disponíveis","Metadados","Períodos", "Documentação"]
)

for s in seletor:
    if s == "Documentação":
        documentacao()
    if s == "Metadados":
        metadados(cod_agregado=id_escolhido)
    elif s == "Variáveis Disponíveis":
        variaveis(cod_agregado=id_escolhido)
    elif s == "Períodos":
        periodos(cod_agregado=id_escolhido)
    elif s == "Folium":
        st.write("Folium - dados Geoespciais")



#url_view = f"https://servicodados.ibge.gov.br/api/v3/agregados/{id_escolhido}/periodos/all/variaveis?view=OLAP&localidades=BR"

#url_view = "https://servicodados.ibge.gov.br/api/v3/agregados/706/variaveis?view=OLAP&localidades=BR"
#res_view = requests.get(url_view)
#view = res_view.json()
#st.write(view)

#url_view = "https://servicodados.ibge.gov.br/api/v3/agregados/706/variaveis?view=flat&localidades=BR"

