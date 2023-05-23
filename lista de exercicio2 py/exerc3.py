maca = int(input("Quantas maças foram compradas? "))

if maca < 12:
    print("O valor da compra foi:",maca * 1.30, "reais")

elif maca >= 12:
    print("O valor da compra foi:",maca * 1, "reais")