# Aula 1 - Condicionais aninhadas
idade = 22

if idade >= 18:
    print("Você é maior de idade")

    if idade >= 21:
        print("Você pode consumir bebida nos EUA")
    else:
        print("Você não pode consumir bebida nos EUA")
else:
    print("Você é menor de idade")


nota = 10

if nota >= 7:

    if nota == 10:
        print("Você tirou a nota máxima!")

    print("Você foi aprovado!")
else:
    print("VOcê está de recuperação")


lista = [1, 2, 3]

if len(lista) > 0:

    if 2 in lista:
        print("O num 2 está na lista")
        if True:
            print("Muito legal")
    else:
        print("O num 2 N esta na lista")

else:
    print("A lista está vazia")

# Aula 2 - Combinacao de condicoes e op. lógicos
idade = 23
renda = 900

if idade < 30 and renda < 1800:
    print("Vc pode participar do programa.")

usuario = 'teste1234'
senha = 'minhasenha'

if usuario == 'teste123' and senha == 'minhasenha':
    print("Vc logou no sistema")
else:
    print("Credenciais erradas")

x = 11
y = 20
z = 20

if (x < y or y < z) and x == 10:
    print("Condicao verdadeira")
else:
    print("deu errado")


if x < y or y < z and x == 10:
    print("Condicao verdadeira")
else:
    print("deu errado")

# aula 3 - operadores ternarios
idade = 20

resultado = "Maior de idade" if idade >= 18 else "Menor de idade"

print(resultado)

if idade >= 18:
    resultado = "Maior de idade"
else:
    resultado = "Menor de idade"

numero = 8

paridade = "É par" if numero % 2 == 0 else "Não é par"

print(paridade)

# VALOR SE O IF FOR TRUE if CONDICAO A SER AVALIADA else VALOR SE IF FOR FALSO


# Aula 4

def verifica_idade(idade):
    if idade < 18:
        return "Menor de idade"
    
    return "Maior de idade"

print(verifica_idade(16))
print(verifica_idade(26))

opcoes = {
    "vermelho": "Pare",
    "amarelo": "Atenção",
    "verde": "Siga"
}

cor = input("Digite uma cor (verde, vermelho ou amarelo)")

print(opcoes.get(cor, "Cor inválida"))

idade = 25
renda = 3000

if idade > 18:
    if renda > 2000:
        print("Elegível ao benefício")

if idade > 18 and renda > 2000:
    print("Elegível ao benefício")