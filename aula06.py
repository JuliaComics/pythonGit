import os 
os.system("cls")

#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF) 
#SWITCH CASE -> (match case) escolha caso (a partir da versao 3.10)

#match valor: 

#linguagem = 100 

#  match linguagem: 

#      case "python":
#          print ("E facil")
#      case "java":
#          print("Muito codigo, Python faz com linhas menores")
#      case "c#":
#         print("Massa")
#     case "js":
#          print("Sou do back")
#     case "html":
#         print("Kauan nao dorme")
#     case 10:
#         print("Entrou aqui")
#     case _: 
#          print("Entrou aqui")


# dia = 0 

# dia = int(input("Digite um número entre 1 e 7: "))
# match dia:

#     case 1:
#         print("Segunda")
#     case 2:
#         print("Terca")
#     case 3:
#         print("Quarta")
#     case 4:
#         print("Quinta")
#     case 5:
#         print("Sexta")
#     case 6:
#         print("Sabado")
#     case 7:
#         print("Domingo")
#     case _: 
#         print("Nenhum dia da semana")

# ATIVIDADE 2  
# Escreva um programa de venda de celular com match case em que: 
# O usuário escolhe um celular e um estado (SP, RJ, MG, etc) 
# O programa retorna o valor do celular, valor do frete e valor total 

# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")]

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

import random
print("Digite 0 para pedra, 1 para papel e 2 para tesoura")
usuario = int(input("Digite sua jogada:  "))
maquina = random.randint(0,2)

pedra = 0 
papel = 1
tesoura = 2 

match usuario: 
    case _ if usuario ==0 and maquina ==1:
        print("A maquina escolheu papel e VOCE PERDEU")
    case _ if usuario ==1 and maquina ==0: 
        print("A maquina escolheu pedra e VOCE GANHOU")
    case _ if usuario ==2 and maquina ==1:
        print("A maquina escolheu papel e VOCE GANHOU")
    case _ if usuario ==1 and maquina  ==2:
        print("A maquina escolheu tesoura e VOCE PERDEU")
    case _ if usuario ==0 and maquina ==2:
        print("A maquina escolheu tesoura e VOCE GANHOU")
    case _ if usuario ==2 and maquina ==0: 
        print("A maquina escolheu pedra e VOCE PERDEU")
    case _ if usuario ==0 and maquina ==0: 
        print("A maquina escolheu pedra resultando em EMPATE")
    case _ if usuario ==1 and maquina ==1:
        print("A maquina escolheu papel resultando em EMPATE")
    case _ if usuario ==2 and maquina ==2: 
        print("A maquina escolheu tesoura resultando em EMPATE")