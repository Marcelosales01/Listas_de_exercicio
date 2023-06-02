import random

temas = {
    "comida": ["abacate","feijoada","pastel"],
    "animal": ["coruja","hiena","lagarto"],
    "país": ["irlanda","brasil","hungria"],
    "objeto": ["garfo","escada","martelo"],
    "celebridade": ["ronaldo","neymar","naldo"]
}

def forca():
    tema = random.choice(list(temas.keys()))
    palavra = random.choice(temas[tema])
    letras_adivinhadas = []
    tentativas = 6

    print("Bem vindo ao jogo da forca!")
    print("O tema é: " + tema)

    while tentativas > 0:
        palavra_adivinhada = ""
        for letra in palavra:
            if letra in letras_adivinhadas:
                palavra_adivinhada += letra
            else:
                palavra_adivinhada +="_"

        print("Palavra: " + palavra_adivinhada)
        print("Ainda restam: " + str(tentativas) + " tentativas")

        if palavra_adivinhada == palavra:
            print("Você acertou! A palavra é:" + palavra)
            return
        
        def boneco_forca(tentativas):
            partes_corpo = ['O','|','/','\\','/','\\']
            for chute_letra in range(len(partes_corpo)):
                if chute_letra < tentativas:
                    print(partes_corpo[chute_letra], end=' ')
                else:
                    print(' ', end=' ')
            print()

    
        chute_letra = input("Digite uma letra: ")

        if chute_letra in letras_adivinhadas:
            print("Denovo? Você ja tentou essa letra.")
            continue
        print()

        letras_adivinhadas.append(chute_letra)

        if chute_letra not in palavra:
            tentativas -= 1
            print("Não possui essa letra.")

        print("")

    print("Perdeu :( . A palavra era: " + palavra)

    boneco_forca(tentativas)

forca()


