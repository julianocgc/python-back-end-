# aula 1 - o que sao pacotes
from pacote_exemplo import modulo1, modulo2

modulo1.funcaoa()
modulo2.funcaob()

# aula 2 - estruturação de pacotes
from pacote_principal import moduloA

from pacote_principal.subpacote import moduloB

moduloA.funcaoA()

moduloA.funcaoModuloA()

moduloB.funcaoB()