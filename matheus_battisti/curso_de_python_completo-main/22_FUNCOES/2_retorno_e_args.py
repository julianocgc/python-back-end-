# aula 1 - *args e **kwargs

def soma(*numeros):
    print(sum(numeros))

soma(1, 2, 3)

soma(10, 20, 30, 40, 50, 60)

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} -> {valor}")

mostrar_info(nome="Alice", idade=30, trabalhando=True)


def exemplo_misto(a, b, *args, teste="testando", **kwargs):
    print(f"a: {a} e b: {b}")
    print(f"Arbitrários: {args}")
    print(f"Padrão: {teste}")
    print(f"Nomeados:  {kwargs}")


exemplo_misto(1, 2, 4, 5, 7, 8, teste="Opa", nome="João", cidade="São Paulo")

# Aula 2-  retorno de valores
def quadrado(numero):
    return numero ** 2

quad_2 = quadrado(2)

print(f"O numero é {quad_2}")

# early return
def dividr(a, b):
    if b == 0:
        return "Divisão por zero!"
    return a / b

print(dividr(10, 0))
print(dividr(10, 2))

def return_multiplo(a, b):
    return a + b, a - b, a * b, a / b

print(return_multiplo(10, 5))

a, b, c, d = return_multiplo(10, 5)

print(a)

# aulas 3 - funcao sem retorno
def exibir_mensagem(mensagem):
    print(mensagem)

exibir_mensagem("Teste")

def salvar_log(txt):
    with open("log.txt", "a") as arquivo:
        arquivo.write(f"Texto do usuário: {txt}")

salvar_log("Meu log...")

# aula 4 - escipos de variaveis
variavel = "x"
outra_variavel = "z"

def escopo_local():
    global outra_variavel

    variavel_funcao = "y"
    print(variavel_funcao)
    print(variavel)
    # Erro -> variavel n global variavel = "y"
    print("FUNCAO: " + outra_variavel)

    outra_variavel = "o"

print("GLOBAL 1: " + outra_variavel)

escopo_local()

print(variavel)

print("GLOBAL 2: " + outra_variavel)

# Erro -> variavel fora do seu escopo: print(variavel_funcao)