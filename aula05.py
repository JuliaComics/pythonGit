#ATIVIDADE 
#1- Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante. (and or)
#2- Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor

#Atividade 1 - Jeito 1 
# l = input("Digite uma letra: ")
# if l == "a" or l =="e" or l =="i" or l=="o" or "u"
#     print("É VOGAL")
# else: 
#     print("É CONSOANTE")

#Jeito 2
# numero1= float(input("Digite um numero: "))
# numero2= (input("Digite outro numero: "))

# if numero1>numero2: 
#     print("O {numero1} é maior do que {numero2} ")

#AGORA SIM É AULA 5 

import os
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

# nota1= float(input("Digite sua primeira nota: "))
# nota2= (input("Digite sua segunda nota: "))

# media= (nota1+nota2)/2 

# if media >5 
#     print("Aluno reprovado")
# if media =5 
#     print("Aluno em recuperação")
# if media =6 
#     print("Aluno em recuperação")
# if media =7 
#     print("Aluno em recuperação")
# if media =7 
#     print("Aluno aprovado")

peso= int(input("Digite seu peso: "))
altura= (input("Digite sua altura: "))

imc = peso / (altura*altura)
print("Seu imc é: ", imc)

if imc < 17: 
    print("Você está muito abaixo do peso")