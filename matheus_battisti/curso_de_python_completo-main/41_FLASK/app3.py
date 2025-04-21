from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)


# aula 1- heranca de template
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# aula 2 - componentes
@app.route("/teste")
def teste():
    return render_template("teste.html")

# aula 3 - form
@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        # aula 4 - processando forms

        # 1 - resgata variaveis
        nome = request.form.get("nome")
        email = request.form.get("email")
        msg = request.form.get("mensagem")

        # 2 - trata / valida os dados

        # 2.5 - se algo der errado, volta uma msg para o usuario

        # 3 - faz o processo final (email, redirecionar pag., salvar banco)
        return render_template("resultado.html", nome=nome, email=email, msg=msg)



    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)