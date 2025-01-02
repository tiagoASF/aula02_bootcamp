# Desafio - Refatorar o projeto da aula anterior evitando Bugs!
# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.
import sys

try:
    nome_usuario = input("Informe o seu nome: ").strip().lower()
    #Verifica se nomoe está vazio
    if (len(nome_usuario) == 0):
        raise ValueError("É necessário digitar um nome")
    #Verifica se há números no nome
    elif any(char.isdigit() for char in nome_usuario):
        raise ValueError("O nome não deve conter números")
    else:
        print(f"VALIDAÇÃO OK! {nome_usuario} é um nome válido")
except ValueError as e:
    print(e)
    sys.exit(1)
    
try:        
    salario = float(input("Agora informe o seu salário mensal: "))
    if (salario <= 0):
        print("O salário informado deve ser maior que ou igual a zero.")
except ValueError:
    print("O salário deve ter valor numérico válido. Digite apenas números.")
    sys.exit(1)

try:
    percentual_bonus = float(input("Qual o percentual do seu bônus anual: "))
    if (percentual_bonus < 0):
        print("O bônus deve ser maior ou igual a zero.")
except ValueError:
    print("O bônus deve ter valor numérico válido. Digite apenas números.")
    sys.exit(1)


kpi = 1000 + (salario * percentual_bonus) / 100
print(f"Olá {nome_usuario.capitalize()}! O valor total do seu bônus foi R$ {kpi:.2f}")