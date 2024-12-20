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
import math

PI = math.pi
raio = float(input("Qual o raio do círculo: "))

area_circulo = PI * math.pow(raio,2)

print(f"A área do circulo de raio {raio} é {area_circulo:.2f}")

