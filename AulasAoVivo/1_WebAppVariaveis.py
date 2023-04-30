#Criação de dicionário com duas chaves e retornar os dados pela rota
dicionario = {
    "nome":"nome",
    "nascimento":"nascimento"
}

#importar Flask
from flask import Flask

#criar a aplicação Web
app = Flask(__name__)

#rota aciona uma função que retorna um dicionário
@app.route("/teste")
def mostra_dicionario():
    return "teste"

@app.route("/")

def dados_usuarios():
    return f"<b>O usuario {dicionario['nome']} nasceu em {dicionario['nascimento']}</b>"

#Executa a aplicação
app.run(debug=True)

