def funcaoA():
    print("Função do Pacote Principal")

from .subpacote.moduloB import funcaoB

def funcaoModuloA():
    print("Funcao do Pacote Principal que Executa Sub Pacote")
    funcaoB()

def funcaoSuperior():
    print("Vim do modulo b")