from ..moduloA import funcaoSuperior

# from ..subpacote.moduloB import funcaoB
from .moduloB import funcaoB


def funcaoC():
    print("MOD C")
    funcaoSuperior()

def funcaoD():
    funcaoB