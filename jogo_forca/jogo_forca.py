'''
Desenvolvido por: Karython Gomes
Data: 01/05/2024

Descrição: o sistema armazena algumas palavras a sua escolha, estas serão sorteadas aleatoriamente
            após ser sorteada, o usuario tentará adivinhar qual palavra está escondida. O sistema esta
            setado com 6 tentativas, poderá ser alterado o numero de tentativas.

Sugestão: 
        - criar um menu com temas, e cada tema possui palavras associadas ao tema
        - criar uma base de dados com as palavras definidas

'''
import random

def escolher_palavra():
    palavras = ['python', 'programação', 'developer', 'tecnologia',
                'computador', 'algoritmo', 'openai', 'inteligencia',
                'software', 'programas']
    
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    
    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'

        print("Palavra:", palavra_escondida)
        print("Letras erradas:", letras_erradas)
        print("Tentativas restantes:", tentativas)

        if palavra_escondida == palavra:
            print("Parabéns! Você venceu!")
            break
        elif tentativas ==0:
            print("Você perdeu! A palavra era:", palavra)
            break

        letra_usuario = input("Digite uma letra: ").lower()

        if letra_usuario in palavra:
            print("Letra correta!")
            letras_corretas.append(letra_usuario)
        else:
            print("Letra errada!")
            letras_erradas.append(letra_usuario)
            tentativas -= 1


if __name__ == "__main__":
    print("Bem-vindo ao Jogo da Forca do Programador!")
    jogar_forca()
