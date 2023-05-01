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

produtos = {
    1: {        
        "nome": "Iphone 14 PRO ",
        "descricao": "Iphone 14, modelo PRO MAX, na cor vermelha",
        "preco": 7800.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    2: {
        "nome": "Samsung Galaxy S21",
        "descricao": "Samsung Galaxy S21, modelo com 5G, na cor preta",
        "preco": 5500.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    3: {
        "nome": "MacBook Pro",
        "descricao": "MacBook Pro 16 polegadas, processador M1 Max, na cor prata",
        "preco": 15999.00,
        "imagem": "https://placehold.co/600x400.png"
    },
    4: {
        "nome": "Sony PlayStation 5",
        "descricao": "Console Sony PlayStation 5, com controle DualSense, na cor branca",
        "preco": 4499.00,
        "imagem":"https://placehold.co/600x400.png"
    },
    5: {
        "nome": "Amazon Echo Dot",
        "descricao": "Caixa de Som inteligente Amazon Echo Dot, com assistente virtual Alexa, na cor azul",
        "preco": 349.00,
        "imagem":"https://placehold.co/600x400.png"
    },
    6: {
        "nome": "Nvidia GeForce RTX 3080",
        "descricao": "Placa de vídeo Nvidia GeForce RTX 3080, 10GB GDDR6X, na cor preta",
        "preco": 7299.00,
        "imagem":"https://placehold.co/600x400.png"
    }
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

@app.route("/produtos")
def exibe_produtos():
    return render_template("produtos_bootstrap.html", produtos=produtos)

app.run(debug=True)