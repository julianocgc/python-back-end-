# aula 1 - excecoes personalizadas
class UsuarioNaoEncontradorError(Exception):
    pass

try:
    if 1 == 1:
        raise UsuarioNaoEncontradorError("Usuário não encontrado no sistema...")
except UsuarioNaoEncontradorError as e:
    print(f"Erro: {e}")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Saldo insuficiente. Você tentou sacar R${valor} e só R${saldo} na conta")

try:
    saldo = 50
    valor = 100

    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
except SaldoInsuficienteError as e:
    print(e)

# aula 2 - raise
try:
    idade = -1

    if idade < 0:
        raise ValueError("Idade nao pode ser negativa...")
except ValueError as e:
    print(e)

class ConfiguracaoInvalidaError(Exception):
    pass

try:
    configuracao = {"chave_ip": "127.0.0.1"}

    if "chave_ip" not in configuracao:
        raise ConfiguracaoInvalidaError("O IP não está configurado.")
except ConfiguracaoInvalidaError as e:
    print(e)


# aula 3 - encadeamento de excecoes
try:
    try:
        raise ValueError("Erro inicial...")
    except ValueError as e:
        raise KeyError("Erro secundário...") from e
except KeyError as e:
    print(f"Erro final: {e}")

    print(f"Causa original: {e.__cause__}")

def carregar_dados():
    raise FileNotFoundError("Arquivo nao encontrado!")

try:
    try:
        carregar_dados()
    except FileNotFoundError as e:
        raise RuntimeError("Erro ao Carregar os Dados que Vieram do Arquivo") from e
except RuntimeError as e:
    print(f"Causa do erro: {e.__cause__}")
    print(f"Erro final: {e}")