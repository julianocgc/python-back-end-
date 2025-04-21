# aula 1 - finally
# finally precisa do try, mas nao precisa do except
try:
    arquivo = open("arquivo2.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo nao existe")
finally:
    try:
        arquivo.close()
        print("Fechou o arquivo")
    except NameError:
        print("O arquivo nunca fui aberto..")

try:
    resultado = 10/0
except ZeroDivisionError as e:
    print("Divisao por zero...")
    print(f"Msg de erro: {e}")
finally:
    print("A operação foi concluida!")

# aula 2 - tipos comuns de erros
pessoa = {"nome": "Aline", "idade": 30}

try:
    print(pessoa["profissao"])
except KeyError as e:
    print("Chave inexistente!")
    print(e)

try:
    soma = "abc" + 5
except TypeError as e:
    print("Tipos inválidos para a operação")
    print(e)


#  aula 3 - multiplas excecoes
# try:
#     numero = int(input("Digite um numero"))
#     divisao = 10 / numero
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro: {e}")


try:
    numero = int(input("Digite um numero"))
    divisao = 10 / numero
except ValueError:
    print(f"Erro: Você não digitou um numero")
except ZeroDivisionError:
    print(f"Erro: Divisao por 0 nao é aceita")