pessoa = {"Pessoa": "Jose", "Idade": 34, "Cursos": ["Ingles", "Portugues"]}
pessoa["Idade"] = 44
pessoa["Cursos"].append("Angular") #adicionando valor a uma chave
pessoa.pop("Idade") #lendo e removendo chave e valor do dicionario
pessoa.update({"Idade": 44, "Sexo": "M"}) #Adicionado chave e valores ao dicionario
print(pessoa)
del pessoa["Cursos"] #DELETA UM VALOR TBM
print(pessoa)
pessoa.clear() #limpando o dicionario
print("Mostrando dic")