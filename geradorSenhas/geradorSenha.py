import random
import string

def gerar_senha(comprimento=12, incluir_maiuscula=True, incluir_miniscula=True,
                incluir_numeros=True, incluir_caracteres=True):
    caracteres = ''
    if incluir_maiuscula:
        caracteres += string.ascii_uppercase

    if incluir_miniscula:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracteres:
        caracteres += string.punctuation

    if not caracteres:
        return ValueError("Pelo menos um tipo de caractere deve ser selecionado")
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de senhas aleatorias")
    comprimento = int(input('Digite o comprimento da senha (padrão 12): ') or 12)
    incluir_maiuscula = input("Incluir maiuscula? (s/n, padrão 's'): ").lower() != 'n'
    incluir_minuscula = input("Incluir minuscula? (s/n, padrão 's'): ").lower() != 'n'
    incluir_numeros = input("Incluir numeros? (s/n, padrão 's'): ").lower != 'n'
    incluir_caractere = input("Incluir caracteres especiais? (s/n, padrão 's'): ").lower != 'n'

    senha = gerar_senha(comprimento, incluir_maiuscula, incluir_minuscula,
                         incluir_numeros, incluir_caractere)
    print(f"Senha gerada foi: {senha}")

if __name__ == "__main__":
    main()