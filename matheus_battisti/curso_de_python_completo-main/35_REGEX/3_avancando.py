# aula 1 - backreferences
import re

texto = "A palavra foo foo se se repete"

padrao = r"(\b\w+\b)\s+\1"

print(re.findall(padrao, texto))

texto = "1212 é um número valido"

padrao = r"(\d+)\1"

print(bool(re.search(padrao, texto)))

texto = "foo foo bar foo"

novo_texto = re.sub(r"(\b\w+\b)\s+\1", "", texto)

print(novo_texto)

# aula 2 - compilacao de regex

padrao = re.compile(r"\d{4}-\d{2}-\d{2}")

texto = "Data: 2021-09-10"

print(padrao.search(texto).group())

texto2 = "Data de ontem: 2021-09-09"
texto3 = "Data de amanhã: 2021-09-11"

print(padrao.search(texto2).group())
print(padrao.search(texto3).group())

padrao = re.compile(r"python", re.IGNORECASE)

texto4 = "Python"
texto5 = "PytHon"

print(bool(padrao.search(texto4)))
print(bool(padrao.search(texto5)))

# aula 3 - aplicacoes praticas

email = "usuario@gmail.com"

padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"

print(bool(re.match(padrao_email, email)))

email2 = "usuario2gmail.com"

print(bool(re.match(padrao_email, email2)))

cep = "88333-370"

padrao_cep = r"^\d{5}-\d{3}$"

print(bool(re.match(padrao_cep, cep)))

cep2 = "88888-23"

print(bool(re.match(padrao_cep, cep2)))

url = "https://google.com"

padrao_url = r"^https://[\w\.-]+$"

print(bool(re.match(padrao_url, url)))

url2 = "https://teste"

print(bool(re.match(padrao_url, url2)))

# aula 4 - substituicao

texto = "A senha é 1234"

novo_texto = re.sub(r"\d", "X", texto)

print(novo_texto)

texto = "O preço é R$ 100,00"

novo_texto = re.sub(r"(\d+),(\d+)", r"\1.\2", texto)

print(novo_texto)

texto = "Este     texto espaços       desnecessários"

novo_texto = re.sub(r"\s+", " ", texto)

print(novo_texto)