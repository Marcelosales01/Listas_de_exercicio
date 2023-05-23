nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 6:
    print("Aprovado, sua media foi:", media)

elif media < 6:
    print("Reprovado, sua media foi:", media)