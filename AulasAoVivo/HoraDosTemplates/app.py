#importa do flask a classe Flask para criação da webapp 
# e render template para renderizar os templates HTML
from flask import Flask, render_template

app = Flask(__name__)

frase = "Hoje meu time joga, que tristeza!"

produto = {
    "id":1,
    "nome":"Iphone 14 PRO ",
    "descricao":"Iphone 14, modelo PRO MAX, na cor vermelha",
    "preco":7800.00,
    "imagem":"https://upload.wikimedia.org/wikipedia/commons/3/37/Back_of_the_iPhone_14_Pro.jpg"
}

#define caminho para acessar/acionar o app
@app.route("/")#caminho local -> 127.0.0.1:5000 ip:porta
def deu_certo():
    #Com o render_template retorna o arquivo html
    #2o parametro envio do conteúdo para variável indicada no template
    return render_template("exemplo.html", frase = frase)

@app.route("/produto")
def exibe_produto():
    return render_template("produto.html", **produto)

@app.route("/produto_boot")
def exibe_produto_boot():
    return render_template("produto_bootstrap.html", **produto)

app.run(debug=True)