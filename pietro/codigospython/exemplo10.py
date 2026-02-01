nota = float(input("Digite sua nota: "))

if nota >= 7.0:
    print("Aprovado(a)")
if nota < 7.0 and nota >= 4.0:
    print("Tem direito a exame.")
if nota < 4:
    print("Reprovado")