#importa do flask a classe Flask para criação da webapp 
# e render template para renderizar os templates HTML
from flask import Flask, render_template

app = Flask(__name__)

frase = "Hoje meu time joga, que tristeza!"

#define caminho para acessar/acionar o app
@app.route("/")#caminho local -> 127.0.0.1:5000 ip:porta
def deu_certo():
    #Com o render_template retorna o arquivo html
    #2o parametro envio do conteúdo para variável indicada no template
    return render_template("exemplo.html", frase = frase)

app.run(debug=True)