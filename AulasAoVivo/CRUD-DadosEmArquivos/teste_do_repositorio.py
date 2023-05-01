import repositorio

#Teste a função retornar_produtos(), que retorna um dicionário de dicionários com todos os produtos
print(repositorio.retornar_produtos())

#Teste a função retornar_produto(id), que recebe um id e retorna um único dicionário contendo os detalhes do produto
print(repositorio.retornar_produto(1))

#Teste a função remover_produto(id), que recebe um id e remove um produtos do dicionário de dicionários
#repositorio.remover_produto()
#print(repositorio.retornar_produto())

#Teste a função alterar_produto(id, dados_produto), que recebe um id e um dicionário contendo dados do produto para então atualizar o produto no dicionário de dicionários
alterado = {
    "nome": "nome",
    "descricao":"descricao",
    "preco":0.0,
    "imagem":"imagem.jpg"
}
repositorio.atualizar_produto(2, alterado )

#Teste a função criar_produto(nome, descricao, preco, imagem), que recebe um nome, uma descricao, um preco e uma imagem e adiciona o produto no dicionario de dicionario com um novo id
repositorio.criar_produto(alterado)
#opções aceitas na passagem de parâmetro:
#repositorio.criar_produto(nome="nome", descricao="descricao", preco=0.0, imagem="imagem.jpg")
#ou ainda:
#repositorio.criar_produto("nome", "descricao", 0.0, "imagem.jpg")

#Experimente a função gerar_id(), que retornar um novo id a partir dos ids já cadastrados no dicionário de dicionários