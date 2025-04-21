# Aula 1 - operadores

# OPERACOES COM OPERADORES LOGICOS RESULTAM EM BOOLEANOS (TRUE OU FALSE)

a = 5
b = 10

print(a == b)
print(a != b)

# > -> maior que
# < -> menor que
print(a > b)
print(b > a)
print(a < b)

c = 10
d = 11

print(b >= c)
print(b > c)

# >= ou <= TB VALIDA A IGUALDADE ENTRE OS VALORES

print(a <= d)

# nao vai levar a gente para lugar nenum
print("maçã" > "banana")

# isso aqui abaixo é ok
print(len("maçã") > len("banana"))

# Aula 2 - continuando operadores
x = 10
y = 25

print(x != y)

z = 20

# Avaliar toda a operacao, para entender qual o booleano será retornado
print(x < y < z)

# Comparar tipos de dados diferentes
valor = "5"
x = 5

print(valor == x)

print(int(valor) == x)

# gera um erro: print(valor > x)

# Aula 3 - operadores lógicos
idade = 17

print(idade > 18 and idade < 30)

print(idade < 18 or idade > 65)

# and => precisa dos dois lados como true
# or => precisa de um dos lados como true

print(not True)

# idosa == false
# not idosa

a = 10
b = 5
c = 6
d = 7

print(a > b or c == d)
print(not a > b or c == d)