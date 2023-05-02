from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

#LEMBRE-SE ->
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa o POST

#É preciso criar rotas que levem em conta as seguintes funcionalidades:
#Listar todos os produtos no template index.html
@app.route("/")
def listagem_produtos():
    return render_template('index.html', produtos=repositorio.retornar_produtos())

#Abrir um produto específico (carregando seus dados) no template cadastro.html
@app.route("/produto/<int:id>", methods=["GET"])
def exibir_produto(id):
    if id == 0: 
        id = repositorio.gerar_id()
        
    produto = repositorio.retornar_produto(id)
    produto['id'] = id
    return render_template('cadastro.html', **produto )

#Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro
#Dar função aos botões excluir e salvar no template cadastro.html
@app.route("/produto/<int:id>", methods=["POST"])
#Acima, indicamos que a rota anterior foi recriada com o método POST para enviar dados
def editar_produto(id):
    if "excluir" in request.form:
        #Aqui a requisição incluia o botão <excluir>
        repositorio.remover_produto(id)
        
    elif "salvar" in request.form:
        #Aqui estamos verificando que "salvar" está contido na requisição, ou seja, o usuário clicou no botão salvar do formulário
        produto = {} #Criando um dicionário vazio para conter os dados do produto que será salvo
        produto["nome"] = request.form["nome"] #colocamos no dicionário o conteúdo que veio do formulário
        produto["descricao"] = request.form["descricao"]
        produto["preco"] = request.form["preco"]
        produto["imagem"] = request.form["imagem"]
        
        #Definir se será SALVAR ou ATUALIZAR
        produtos = repositorio.retornar_produtos()
        
        #Testa se o id do produto está no dicionário
        if id in produtos.keys():
            repositorio.atualizar_produto(id, produto)
            #Caso exista o id, vamos chamar a função atualizar_produto
        else:
            repositorio.criar_produto(**produto)
            #caso a id não exista, vamos chamar a função criar_produto passando os dados do dicionário
            #repositorio.criar_produto(nome=produto['nome']), descricao=produto['descricao'], preco=produto['preco'], imagem=produto['imagem']
            
    return redirect(url_for('listagem_produtos'))

app.run(debug=True)