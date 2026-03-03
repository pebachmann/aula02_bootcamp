#Exercícios

#Números de Ponto Flutuante (float)
#6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero1 = float(input("Digite um numero qualquer: "))
numero2 = float(input("Digite um numero qualquer: "))
soma= numero1 + numero2
print(f"A soma dos numeros inteiro é: {soma}")

#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero3 = float(input("Digite um numero qualquer: "))
numero4 = float(input("Digite um numero qualquer: "))
media= (numero1 + numero2) / 2
print(f"A media dos numeros é: {media}")

#8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero5 = float(input("Digite um numero qualquer: "))
numero6 = float(input("Digite um numero qualquer: "))
potencia = numero5 ** numero6
print(f"A potencia de {numero5} elevado a {numero6} é: {potencia}")

#9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
numeroC = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (numeroC * (9/5)) + 32
print(f"A temperatura {numeroC} em Celsius é {fahrenheit} graus Fahrenheit.")

#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
area = 3.16 * raio**2
print(f"A area do circulo de raio {raio} é {area}")
