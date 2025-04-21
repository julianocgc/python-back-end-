# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Escreva um programa que receba a idade de uma pessoa e exiba uma mensagem indicando se
# ela é criança (menor de 13 anos), adolescente (13 a 17 anos) ou adulta (18 anos ou mais) usando
# estruturas if-elif-else.
# Descrição: O programa deve capturar a idade, usar condicionais para determinar a faixa etária e
# exibir a mensagem correspondente.

# Exercício 2:
# Enunciado: Crie um programa que solicite ao usuário uma senha e verifique se ela atende aos
# seguintes critérios: tem pelo menos 8 caracteres, contém pelo menos um número e uma letra. Use
# condicionais e operadores lógicos.
# Descrição: O programa deve validar a senha com base nos critérios, exibindo mensagens para cada
# caso (válido ou inválido).
# isdigit = é numero
# isalpha = é letra

# Exercício 3:
# Enunciado: Desenvolva um sistema de classificação de notas. O programa deve receber uma nota e
# exibir "Aprovado com distinção" para notas maiores ou iguais a 9, "Aprovado" para notas entre 7
# e 8.9, e "Reprovado" para notas abaixo de 7. Utilize operadores ternários.
# Descrição: O programa deve classificar e exibir o status de aprovação com base na nota fornecida,
# usando lógica simplificada.

# Exercício 4:
# Enunciado: Escreva um programa que receba um número e determine se ele é positivo, negativo ou
# zero. Evite condicionais aninhadas, utilizando estratégias de simplificação.
# Descrição: O programa deve usar condicionais claras e eficientes para determinar e exibir o
# estado do número.

# Exercício 5:
# Enunciado: Implemente um programa que filtre números pares de uma lista e categorize os números
# pares como "pequenos" (menores que 10) ou "grandes" (10 ou maiores). Use condicionais e boas
# práticas de codificação.
# Descrição: O programa deve iterar pela lista, usar condicionais para categorizar os números pares,
# e exibir as categorias.

# Ex 1
idade = 6

if idade < 13:
    print("Você é uma criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")


# Ex 2
senha = 'test123'

tem_8_caracteres = len(senha) >= 8

tem_numero = any(char.isdigit() for char in senha)

tem_letra = any(char.isalpha() for char in senha)

if tem_8_caracteres and tem_numero and tem_letra:
    print("Senha forte!")
else:
    print("Senha fraca")

# Ex 3
nota = 9

status = (
    "Aprovado com distinção" if nota >= 9 else
    "Aprovado" if nota >= 7 else
    "Reprovado"
)

print(status)

# Ex 4
numero = 0

if numero > 0:
    print("Numero positivo")
elif numero < 0:
    print("Numero negativo")
else:
    print("Zero")


# Ex 5
numeros = [3, 12, 7, 5, 8, 11, 90, 4]

pares = [num for num in numeros if num % 2 == 0]

print(pares)

categorias = [
    "Pequeno" if num < 10 else "Grande" for num in pares
]

print(categorias)