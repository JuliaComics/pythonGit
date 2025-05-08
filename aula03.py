import os 
os.system("color 05")

#Continuação Input com Int e Float
#(Uso do Input com número)
#int() -> converte para inteiro
#float() -> converte para n quebrado

# numero = 10
# numero2 = input("digite um número: ")
# print("o tipo de número é,", type(numero2))
# soma = numero + int(numero2) 
# print(f"soma de {numero} + {numero2}  = ", soma)


#exemplo2
# num1 = input("digite um numero: ")
# soma = float(num1) + 15
# print("A Soma de ",num1, "+", "15", "=", soma)

#exemplo3
# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)

#ATIVIDADE UM - MULTIPLICACAO
# numero1 = float(input("Digite um numero: "))
# numero2 = float(input("Digite outro numero: "))
# multiplicacao = (numero1) * (numero2)
# print("A multicacao entre os numeros e ", "numero2", "*", "=", multiplicacao)

#ATIVIDADE DOIS - ANTECESSOR
# numero1 = float(input("Digite um numero: "))
# subtracao = (numero1) - (1)
# soma = (numero1) + (1)
# print("Seu antecessor e:  ", "numero1", "-", "1", "=", subtracao)
# print("Seu sucessor e: ", "numero1", "+", "1", "=", soma)

#ATIVIDADE TRES - ANO NASCIMENTO
# numero = int(input("Digite seu ano de nascimento: "))
# subtracao = (2025) - (numero)
# print(f"Você tem {subtracao} anos")

#SEGUNDA ATIVIDADE 
produto1 = float(input("Digite o preco do primeiro produto: "))
produto2 = float(input("Digite o preco do segundo produto: "))
desconto1 = 0.10 * produto1 
desconto2 = 0.25 * produto2 
print("O preco do primeiro produto com 10% de desconto é de", round(produto1-desconto1),"reias" )
print("O preco do segundo produto com 25% de desconto é de", round(produto2-desconto2), "reais")
total = (produto1-desconto1) + (produto2-desconto2)
print(f"O total a pagar por ambos os produtos é {total}", "reais")
