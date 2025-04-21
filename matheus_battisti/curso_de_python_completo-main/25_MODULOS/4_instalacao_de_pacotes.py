# 1 - instalando pacotes
import requests

response = requests.get("https://api.github.com")

print("Status da req. ", response.status_code)
print("Cabeçalhos: ", response.headers)

# 2 - pypi
from rich.console import Console

console = Console()

console.print("[bold magenta]Olá Mundo[/bold magenta]")

console.print("[green]Testando[/green] [underline]Testando underline[/underline]")