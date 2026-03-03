#Exercícios 3

#Strings (str)
#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
letras = str(input("Digite uma string: "))
letras2 = letras.upper()
print(f"Texto em maiusculo: {letras2}")

#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = str(input("Qual o seu nome:"))
nome2 = nome.upper()
print(f"Seu nome em maiusculo é: {nome2}")


#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input("Insira uma frase: "))
frase2 = frase.strip()
print(f"Sua frase sem espaços em branco é: {frase2}")

#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input("Digite uma data no formato dd/mm/aaaa: "))
data_separada = data.split("/")
print(f"A sua data separada é: {data_separada}")

#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str1 = str(input("Digite uma string: "))
str2 = str(input("Digite outra string: "))
concat = str1 + "." + str2
print(f"Sua frase concatenada é: {concat}")