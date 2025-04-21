# aula 1 - regex
import re

texto = "O número 422 está aqui."

resultado = re.search(r"\d+", texto)

print(resultado.group())

frase = "Python é muito legal!"

nova_frase = re.sub(r"legal", "massa", frase)

print(nova_frase)


# aula 2 - como funciona a regex

texto = "123 abc 456 abc 789 abc def jip kew"

print(re.findall(r"abc", texto))

print(re.findall(r"[a-e]+", texto))

# Python -> python => nao encontra

# PyThoN

texto = "Python é muito bom, python é muito legal, PyThOn é demais!"

print(re.findall(r"python", texto, re.IGNORECASE))

# aula 3 - sintaxe de metacaracteres
texto = "abcdefghij abcdef 123"

print(re.findall(r"a.c", texto))
print(re.findall(r"d.f", texto))

# aALGUMACOISAf
# aALGUMACOISAc

print(re.findall(r"\d*", texto))

print(re.findall(r"\d+", texto))

print(re.findall(r"[abc]", texto))
print(re.findall(r"[123]", texto))
print(re.findall(r"[1-3]", texto))
print(re.findall(r"[a-e]", texto))

# aula 4 - ancoras

# no comeco ou final do texto = ancora

texto = "Python é poderoso"

print(bool(re.match(r"^Python", texto)))

print(bool(re.match(r"^poderoso", texto)))

# ^ comeco
# $ no final

print(bool(re.search(r"Python$", texto)))

print(bool(re.search(r"poderoso$", texto)))

print(bool(re.match(r"^Python é poderoso$", texto)))

print(bool(re.match(r"^Python é$", texto)))