# Aula 1 - teoria o flask

# Aula 2 - instalacao do flask
from flask import Flask, jsonify

app = Flask(__name__)

# rota login -> site.com/login

@app.route("/")
def home():
    return "Bem-vindo ao seu primeiro app de Flask 2"

# aula 3 - estrutura de pastas

# aula 4 - rotas

@app.route("/api/data")
def api_data():
    data = {"nome": "Flask", "versao": "3.1"}
    return jsonify(data)

@app.route("/user/<username>")
def user_profile(username):
    return f"Perfl do usuario: {username}"


if __name__ == "__main__":
    app.run(debug=True)