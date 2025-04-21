# Receber um texto
# E determinar quantas: palavras, caracteres e linhas o texto tem

def analisar_texto(texto):
    # contar linhas
    linhas = texto.splitlines()
    numero_linhas = len(linhas)

    # contar palavras
    palavras = texto.split()
    numeros_palavras = len(palavras)

    # contar caracteres
    numero_caracteres = len(texto)

    return numero_linhas, numeros_palavras, numero_caracteres

def main():
    print("Bem-vindo ao Analisador de Textos!")
    print("Digite o seu texto abaixo, e para finalizar pressione Enter duas vezes")

    # Entrada de texto
    texto = ""
    while True:
        linha = input()
        # Condição de encerramento
        if linha == "":
            break
        texto += linha + "\n"

    linhas, palavras, caracteres = analisar_texto(texto)

    print("Resultado análise:")
    print(f"Número de linhas: {linhas}")
    print(f"Número de palavras: {palavras}")
    print(f"Número de caracteres: {caracteres}")

if __name__ == "__main__":
    main()