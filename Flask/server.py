from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Função para ler dados do arquivo JSON
def read_json_file():
    with open('dados.json', 'r') as file:
        return json.load(file)

# Função para escrever dados no arquivo JSON
def write_json_file(data):
    with open('dados.json', 'w') as file:
        json.dump(data, file, indent=4)

# Rota para apresentação
@app.route('/', methods=['GET'])
def home():
    data = "<h1> Bem vindos a minha API</h1>"
    return data

# Rota para obter todos os dados
@app.route('/dados', methods=['GET'])
def get_dados():
    data = read_json_file()
    return jsonify(data)

# Rota para selecionar um dado específico usando POST
@app.route('/dados', methods=['POST'])
def get_dado():
    data = read_json_file()
    request_data = request.get_json()
    id = request_data.get('id')
    dado = next((item for item in data if item['id'] == id), None)
    if dado:
        return jsonify(dado)
    else:
        return jsonify({'error': 'Dado não encontrado'}), 404

# Rota para atualizar um dado específico usando PATCH
@app.route('/dados', methods=['PATCH'])
def update_dado():
    data = read_json_file()
    request_data = request.get_json()
    id = request_data.get('id')
    new_data = request_data.get('new_data')
    for item in data:
        if item['id'] == id:
            item.update(new_data)
            write_json_file(data)
            return jsonify(item)
    return jsonify({'error': 'Dado não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)