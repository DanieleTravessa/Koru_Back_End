import sqlite3 

conexao = sqlite3.connect('harry_potter.db')

#Criando os dados que vou manipular no banco
nome = "Harry Potter"
raca = "Humano"
casa = "Grifinória"
altura = 1.80
nascimento = "31/07/1980"
imagem = ""

#Inserir dados no banco
cursor = conexao.cursor()
sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) VALUES (?, ?, ?, ?, ?, ?)"

cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))

personagem_id = cursor.lastrowid
conexao.commit()
print(f"O último código inserido foi: {personagem_id}")

#print("Personagem de código 2")
#cursor = conexao.cursor()
#sql_select_unico = "SELECT * FROM personagens Where id_personagem = ?"
#cursor.execute(sql_select_unico, (2, ))
#print(cursor.fetchone())

