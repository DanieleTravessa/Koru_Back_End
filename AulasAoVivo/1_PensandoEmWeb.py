#importando o Flask
from flask import Flask

#variável (objeto) que representa aplicação web
app = Flask(__name__)

#cria uma rota para acessar o servidor
@app.route("/") 

#Acessado a rota, a função a seguir é executada e traz como retorno a frase "Deu Certo!"
def exibir_mensagem(): 
    return "Deu certo!"

#Executa a aplicação web que foi crada a partir do flask
app.run(debug=True)