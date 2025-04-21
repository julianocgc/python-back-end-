# aula 1 - introducao do modulo

# criar uma funcao
# @funcao

# decorators são reutilizaveis

def meu_decorador(funcao):
    def wrapper():
        print("Iniciando função...")
        funcao()
        print("Terminando funcao...")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Executando a função principal!")

minha_funcao()

# aula 2  - funcoes como objetos de primeira classe

# funcao em variavel
def saudacao():
    return "Ola mundo!"

cumprimento = saudacao

print(cumprimento())

# funcao como argumento
def executar_funcao(func):
    print("alguma coisa...")
    print(func())

executar_funcao(saudacao)

# retornar funcao dentro de funcao
def criar_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador

multiplicador = criar_multiplicador(3)

print(multiplicador(10))
print(multiplicador(15))
print(multiplicador(20))


# aula 3 - decorators simples

def log_decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando a funçao: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Função: {func.__name__} executada com sucesso.")
        return resultado
    return wrapper

@log_decorador
def soma(a, b):
    return a + b

@log_decorador
def multiplicacao(a, b, c):
    return a * b * c


print(soma(4, 5))
print(multiplicacao(4, 5, 6))


def validar_positivo(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("O número deve ser positivo.")
        return func(x)
    return wrapper

@validar_positivo
def calcular_raiz_quadrada(x):
    return x ** .5

print(calcular_raiz_quadrada(10))
# print(calcular_raiz_quadrada(-10)) -> dispara o erro


# aula 4- aninhando funcoes
def externa():
    mensagem = "Olá Mundo!"
    def interna():
        print(f"A mensagem é: {mensagem}")
    return interna

func = externa()

func()