# Aprendizado de APIs em Python
Com a ajuda do Chat GPT destaquei os principais objetivos de uma trilha de estudos para aprendizados de acesso, requests e logins em API a partir de python. A priori, irei seguir fazendo análises dos dados encontrados e desenvolvendo habilidades dos tópicos contidos na trilha descrita abaixo: 

## 1. Introdução às APIs e Requests

**Objetivo:** Entender o que são APIs, como funcionam, e aprender a fazer requisições básicas.

- **Principais Comandos:**
  - `requests.get()`: Faz uma requisição GET para um URL.
  - `response.status_code`: Verifica o status da resposta.
  - `response.json()`: Converte a resposta para JSON.
  - `response.text`: Pega o conteúdo da resposta como texto.

- **Bibliotecas Úteis:**
  - `requests`: Biblioteca principal para fazer requisições HTTP.

- **Teoria:**
  - APIs (Application Programming Interfaces) permitem que diferentes sistemas se comuniquem.
  - Tipos de requisições: GET, POST, PUT, DELETE, etc.
  - Códigos de status HTTP (200, 404, 500, etc.).

- **Projeto Prático:**
  1. Fazer a requisição de um conjunto de dados da API do IBGE.
---

## 2. Manipulação de Dados de APIs

**Objetivo:** Aprender a manipular e extrair informações úteis das respostas das APIs.

- **Principais Comandos:**
  - `response.headers`: Obtém os cabeçalhos da resposta.
  - Manipulação de JSON com `json.loads()` e `json.dumps()`.
  - Tratamento de exceções com `try-except`.

- **Bibliotecas Úteis:**
  - `json`: Para trabalhar com dados JSON.
  - `requests`: Continuação.

- **Teoria:**
  - Estruturas de dados JSON e como navegar por elas.
  - Importância dos cabeçalhos HTTP (e.g., autenticação, tipo de conteúdo).

- **Exercício/Desafio Prático:**
    1. Fazer a requisição de um conjunto de dados da API do IBGE, estruturar eles utilizando dataframe pandas e aplicar algumas análises descritivas ao conjunto de forma que seja possível identificar um conjunto que seja interessante para fazer uma análise mais a fundo.
    2. Após decidir o conjunto de dados, elaborar dashboards de aprensatação dos dados e análises utilizando a biblioteca StreamLit do python.

---

## Nível 3: Autenticação e Segurança

**Objetivo:** Aprender a usar métodos de autenticação em APIs, como API keys e tokens.

- **Principais Comandos:**
  - Passagem de headers personalizados usando `requests.get(url, headers={...})`.
  - Autenticação básica e com Bearer Token.

- **Bibliotecas Úteis:**
  - `requests`: Para autenticação com headers.
  - `dotenv`: Para gerenciar variáveis de ambiente (segurança das credenciais).

- **Teoria:**
  - Métodos de autenticação em APIs (API Keys, OAuth, JWT).
  - Práticas seguras para armazenamento de credenciais (e.g., variáveis de ambiente).

- **Exercício/Desafio Prático:**
  - Consuma uma API que exija autenticação (como GitHub API, Spotify ou Youtube), listando seus repositórios públicos e seus detalhes.

---

## Nível 4: Consumo de APIs RESTful e SOAP

**Objetivo:** Compreender e consumir APIs RESTful e SOAP, entendendo suas diferenças.

- **Principais Comandos:**
  - `requests.post()`, `requests.put()`, `requests.delete()`.
  - Manipulação de payloads JSON para envio de dados.

- **Bibliotecas Úteis:**
  - `requests`: Continuação.
  - `zeep`: Para consumo de APIs SOAP.

- **Teoria:**
  - Diferenças entre REST (leve, usa JSON) e SOAP (mais pesado, usa XML).
  - Operações CRUD em APIs RESTful.

- **Exercício/Desafio Prático:**
  - Construa um cliente simples para consumir uma API RESTful de tarefas (como uma To-Do list), permitindo adicionar, listar e deletar tarefas.

---

## Nível 5: Criação de APIs com Flask

**Objetivo:** Aprender a criar APIs simples usando Flask para entender o que acontece "do outro lado".

- **Principais Comandos:**
  - Rotas com `@app.route()`.
  - Métodos de requisição (`GET`, `POST`).
  - Retorno de dados em JSON com `jsonify()`.

- **Bibliotecas Úteis:**
  - `Flask`: Para criar APIs.
  - `flask_restful`: Para simplificar a criação de APIs REST.

- **Teoria:**
  - Estrutura básica de uma API com Flask.
  - Criação de rotas e manipulação de dados enviados pelo cliente.

- **Exercício/Desafio Prático:**
  - Crie uma API básica de cadastro de usuários com operações de GET e POST para listar e adicionar usuários.

---

## Nível 6: Consumo e Criação de APIs Avançadas

**Objetivo:** Entender conceitos avançados como paginação, filtros, e rate limiting em consumo, além de desenvolver APIs mais robustas.

- **Principais Comandos:**
  - Manipulação de query parameters (`params`).
  - Uso de `flask_jwt_extended` para autenticação em APIs Flask.

- **Bibliotecas Úteis:**
  - `requests`: Para manipular parâmetros avançados.
  - `Flask`: Continuação.
  - `flask_jwt_extended`: Para adicionar autenticação JWT em APIs Flask.

- **Teoria:**
  - Como lidar com grandes volumes de dados (paginação, filtros).
  - Implementação de segurança em APIs desenvolvidas.

- **Exercício/Desafio Prático:**
  - Construa uma API com Flask que permita operações CRUD em um banco de dados, utilizando autenticação JWT para proteger as rotas.