# 1 - importacao absoluta
from pacote_principal import moduloA

moduloA.funcaoA()

from pacote_principal.subpacote import moduloB

moduloB.funcaoB()

# 2 - importacao relativa

from pacote_principal.subpacote import moduloC

moduloC.funcaoC()