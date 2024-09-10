nome = input("Informe seu nome: ")
end = input("informe seu endereço: ")
idade = input("Informe sua idade: ")

print(nome, end, idade)

#1ª forma de concentração
print("\Olá ",nome, "seu endereço é",end," sua idade é", idade)

#2ª forma de concatenação
print("\Olá {} seu endereço é {} e sua idade é {}".format(nome, end, idade))

#3ª forma de concatenação - f string
print(f"Bem vindo {nome}, você mora na {end} e tem {idade} anos")