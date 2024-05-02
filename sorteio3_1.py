'''
Desenvolvido por: Karython Gomes
Data: 12/04/2024

Descrição: O sistema recebe o nome dos canditatos e realiza o sorteio,
            escolhendo aleatoriamente alguem da lista. Nesta versão já esta includo
            uma contgem regressiva, a lista de todos os sorteados e é possivel sortear
            mais de um nome com a mesma lista
            

Versão: 3.1

- Adicionando contagem

Sugestão:
        - para a proxima versão que já está em produção, será adicionado a interface usando flet
'''

import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input(str("Digite os nomes a serem sorteados: "))
    if nome:
        lista_nomes.append(nome)
    else:
        break
    
while True:
    if lista_nomes:
        os.system("cls")
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)
        
        contagem = 5
        
        while contagem >=0:
            os.system("cls")
            print(f"Sorteando em {contagem}...")
            time.sleep(1)
            contagem -=1
            os.system("cls") 
            
        print(f"O escolhido foi: {escolhido}")
            
        
        opcao = input(str("Deseja sortear outro nome? S/N\n| - S para (sim)\n| - N para (não)\n"))
        os.system("cls")
        
        if opcao != "s":
            break
    else:
        print("Não há nomes para serem sorteados")
print("Programa encerrado!")
print(f"Os sorteados foram: {lista_sorteados}")
print(f"Lista de participantes {lista_nomes}")
