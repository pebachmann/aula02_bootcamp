#Exercícios 4

# Booleanos (bool)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
resultado_or = valor1 or valor2
print("Resultado do OR lógico, ", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resultado_not = not valor1
print("Resultado valor inverso ao lógico 01: ", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))
igual = (num1 == num2)
print("Resultado igualdade: ", igual)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num3 = int(input("Digite um numero inteiro: "))
num4 = int(input("Digite um numero inteiro: "))
diferentes = (num3 != num4)
print("Resultado diferença: ", diferentes)
