#1 solicitar ao usuario que digite seu nome

nome_usuario = input("Digite o seu nome: ")
if nome_usuario.isdigit():
    print("Voce digitou o nome errado")
    exit()

if len(nome_usuario) == 0:
    print("Voce nao digitou o nome")
    exit()

if nome_usuario.isspace():
    print("Voce digitou apenas espacos")
    exit()

#2 Solicitar ao usuario que digite o valor do seu salario
#  Conversão da entrada para numero de ponto flutuante

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")


#3 solicitar ao usuario que digite o valor do bonus
#  Converter a entrada para um numero de ponto flutuante

try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

#4 calcule o valor do bonus final
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

#5 imprima o calculo do valor final
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")