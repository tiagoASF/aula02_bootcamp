# INT
#1- Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# valor1 = int(input("Informe o primeiro valor: "))
# valor2 = int(input("Informe o segundo valor: "))
# soma = valor1 + valor2
# print(f"A soma de {valor1} e {valor2} é {soma}")

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# DIVIDENDO = 5
# valor_usuario = float(input("Informe um valor: "))
# resto_divisao = valor_usuario % DIVIDENDO
# print(f"O resto da divisão entre {valor_usuario} e {DIVIDENDO} é {resto_divisao:.0f}")

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# valor1 = float(input("Informe o primeiro valor: "))
# valor2 = float(input("Informe o segundo valor: "))
# resultado_multiplicacao = valor1 * valor2
# print(f"O resultado da multiplicação é {resultado_multiplicacao}")

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# valor1 = float(input("Informe o primeiro valor: "))
# valor2 = float(input("Informe o segundo valor: "))
# resultado = valor1 // valor2
# print(f"O resultado da divisão inteira de {valor1} por {valor2} é {resultado}")

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# import math

# valor = float(input("Informe o valor desejado: "))
# resultado = math.sqrt(valor)
# print(f"A raiz quadrada de {valor} é {resultado:.2f}")

#PONTO FLUTUANTE
#6 - Escreva um programa que receba dois números flutuantes e realize sua adição.

# valor1 = float(input("Informe o primeiro valor: "))
# valor2 = float(input("Informe o segundo valor: "))

# resultado = valor1 + valor2

# print(f"A soma entre {valor1} e {valor2} é {resultado:.2f}")


# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# valor1 = float(input("Informe o primeiro valor: "))
# valor2 = float(input("Informe o segundo valor: "))
# media = (valor1 + valor2) / 2

# print(f"A média entre {valor1} e {valor2} é {media:.2f}")

# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# import math

# base = float(input("Informe a base da potenciação: "))
# expoente = float(input("Agora forneça o exponte: "))

# resultado = math.pow(base, expoente)

# print(f"O resultado é {resultado}")

# 9 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temperatura_c = float(input("Informe a temperatura em Celcius: "))
# temperatura_f = (temperatura_c * 1.8) + 32

# print(f"{temperatura_c}oC em Fahreheint é {temperatura_f}")

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math

# PI = math.pi
# raio = float(input("Qual o raio do círculo: "))

# area_circulo = PI * math.pow(raio,2)

# print(f"A área do circulo de raio {raio} é {area_circulo:.2f}")

#Strings (str)
# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# palavra = input("Informe o nome a ser convertido: ").strip().lower()
# print(palavra.upper())

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome_completo = input("Informe o seu nome completo: ").strip()
# nome_tratado = nome_completo.lower()
# print(nome_tratado)

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Insira uma frase: ")
# frase_tratado = frase.strip()
# print(frase_tratado)

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_string = input("Informe a data no formato dd/mm/aaaa: ")
# dia, mes, ano = data_string.split("/")
# print(f"Dia:{dia}, Mês:{mes}, Ano:{ano}")


# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.
# texto1 = input("Parte 1: ").strip()
# texto2 = input("Parte 2: ").strip()
# texto_final = texto1 + texto2
# print("Texto concatenado: ", texto_final)

#Booleanos (bool)
# 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = True
# valor2 = False
# resultado = valor1 and valor2
# print(resultado)


# 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# valor1 = False
# valor2 = True
# resultado_final = valor1 or valor2
# print(resultado_final)  


# 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor1 = True
# resultado = not valor1
# print(resultado)

# 19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# x = 1
# y = 30
# resultado_bool = (x == y)
# print(resultado_bool)


# 20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# x = 1
# y = 30
# resultado_bool = (x != y)
# print(resultado_bool)


# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     t_celcius = float(input("Informe a temperatura em Celcius: "))
#     t_farenheit = (t_celcius * 9/5) + 32
#     print(f"{t_celcius}oC equivalem a {t_farenheit}oF")
# except ValueError as e: 
#     print("O valor de temperatura deve ser numérico")


# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
# palavra = input("Informe a palavra ou frase: ").strip()

# if isinstance(palavra, str):
#     palavra_tratada = palavra.replace(" ", "").lower()
#     if palavra_tratada == palavra_tratada[::-1]:
#         print(f"{palavra.upper()} é um palindromo")
#     else:
#         print(f"{palavra.upper()} não é um palindromo")
# else:
#     print("Você deve digitar uma frase ou palavra!")


# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# try:
#     valor1 = float(input("Informe o primeiro valor: "))
# except ValueError as e:
#     print("O valor digitado não é numérico")

# try:
#     valor2 = float(input("Informe o segundo valor: "))
# except ValueError as e:
#     print("O valor digitado não é numérico")

# try:
#     operacao = input("Qual operação(+, -, *, /) deseja realizar: ").strip()
# except TypeError as e:
#     print("O valor digitado não é uma string válida")

# if operacao == "+":
#     print(f"A soma entre {valor1} e {valor2} é {valor1 + valor2}")
# elif operacao == "-":
#     print(f"A subtração de {valor1} por {valor2} é {valor1 - valor2}")
# elif operacao == "*":
#     print(f"A multiplicação  entre {valor1} e {valor2} é {valor1 * valor2}")
# elif operacao == "/":
#     try:
#         print(f"A divisão de {valor1} por {valor2} é {valor1 / valor2}")
#     except ZeroDivisionError as e:
#         print("A divisão por zero não é válida")
    
# else:
#     print(f"{operacao} não é uma operação válida")




# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".


try:
    valor = int(input("Informe o valor inteiro desejado: "))
    positivo_negativo = "positivo"
    par_impar = "par"

    if valor % 2 != 0:
        par_impar = "ímpar"

    if valor < 0:
        positivo_negativo = "negativo"
    elif valor == 0:
        positivo_negativo = "zero"
    
    print(f"O valor {valor} é {positivo_negativo} e {par_impar}")
except ValueError as e:
    print("O valor informado deve ser numérico")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
