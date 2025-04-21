# Aula 1 f strings
nome = "Matheus"
idade = 33

# f-string converte numero para texto
print(f"Meu nome é {nome} e eu tenho {idade} anos")
print("Meu nome é " + nome + " e eu tenho " + str(idade) + " anos")

a = 5
b = 10

print(f"A soma de {a} e {b} é igual a { a + b }")

valor = 12.9892754

print(f"O valor arredondado é {valor:.2f}")

# aula 2 format
print("Meu nome é {} e eu tenho {} anos".format("Aline", 23))

valor = 1.2345

print("O valor formato é {:.3f}".format(valor))


print("Ordem de parametros invertida {1} e {0}".format("primeiro", "segundo"))

# aula 3 strings multilinha
texto = """Este é meu
texto
com multinha"""

print(texto)

texto2 = '''Este
é também
multilinha'''

print(texto2)

"""
    Função teste
    Não aceita parâmetros
    E retorna o valor 1
"""
# Meu comentário
def teste():
    return 1


nome = "Matheus"

frase = f"""Meu nome é
{nome}
tudo bem?"""

print(frase)

texto_com_escape = """
QUalquer coisa
\n\n
pulou linha"""

print(texto_com_escape)

# Aula 4 caracteres especiais
texto = "Testando \n Caracteres \n Especiais"

print(texto)

aspas = "E quero \"colocar\" aspas"

aspas2 = 'E quero "colocar" aspas'

print(aspas)

caminho_de_uma_pasta = r"C:\Users\Matheus\Teste.txt"

print(caminho_de_uma_pasta)