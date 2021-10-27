from string import Template

nome, idade = "Ana", 30

print("Nome: %s Idade: %d %r %r" % (nome, idade, True, False))
print("Nome: {} Idade: {}".format(nome, idade))
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome =nome, idade = idade))