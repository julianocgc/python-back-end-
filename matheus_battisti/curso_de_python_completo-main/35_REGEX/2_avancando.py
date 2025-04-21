# aula 1 -  conjuntos
import re

texto = "Hoje é dia 20 de Janeiro de 2024"

print(re.findall(r"\d+", texto))

texto = "Python_3 é incrível!"

print(re.findall(r"\w+", texto))

texto = "Texto com espaços e \n quebras de \n linha"

print(re.findall(r"\s", texto))

texto = "abc 123 xyz"

print(re.findall(r"[a-c1-3]+", texto))


# aula 2 - quantificadores

print(re.findall(r"a*", "aaabaaca"))

print(re.findall(r"a+", "aaabaaca"))

print(re.findall(r"a?", "aaabaaca"))

print(re.findall(r"a{2,3}", "aaabaaca"))

# aula 3 - metodos de re

texto = "Python é uma boa linguagem"

resultado = re.search(r"boa", texto)

print(resultado.group())

resultado2 = re.search(r"boa2", texto)

print(resultado2)

resultado3 = re.match(r"Python", texto)

print(bool(resultado3))

resultado4 = re.match(r"boa", texto)

print(bool(resultado4))

novo_texto = re.sub(r"boa", "ótima", texto)

print(novo_texto)

resultado5 = re.findall(r"a", texto)

print(resultado5)

# aula 4 - grupos

texto = "Data: 25/10/2024"

resultados = re.search(r"(\d{2})/(\d{2})/(\d{4})", texto)

print(resultados.group(3))

texto = "Telefone: (48) 99999-0506"

resultados = re.search(r"\((?P<ddd>\d{2})\) (?P<num>\d{5}-\d{4})", texto)

print(resultados.group("ddd"))

print(resultados.group("num"))