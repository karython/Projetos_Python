'''

Desenvolvido por: Karython gomes
Data: 28/03/2024
Versão: 1.0
Descrição: Esta aplicação faz o consumo de uma API de tempo
            e permite verificar a situação climatica das cidades.
            
Proxima versão: escrever a previsão em um arquivo txt

'''

from credenciais import key
import requests


def obter_previsao_tempo(cidade, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def exibir_previsao_tempo(previsao):
    
    if previsao.get('cod') == 200:
        clima = previsao["weather"][0]["description"]
        temperatura = previsao["main"]["temp"]
        umidade = previsao["main"]["humidity"]
        print(f"Condição: {clima}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        
    else:
        print("Cidade não encontrada.")

#TODO - Automatizar o processo, escrevendo as previsões em arquivos        
'''
def formatar_saida(previsao):
    texto_formatado = f"Condição do tempo: {previsao['clima']}\n"
    texto_formatado += f"Temperatura: {previsao['temperatura']}°C\n"
    texto_formatado += f"Umidade: {previsao['umidade']}%"
    
    return formatar_saida
    
      caminho_diretorio = r'C:\\Users\\Gomes\\Desktop\\pythonVscode\\previsao\\previsao.txt'
    if not os.path.exists(caminho_diretorio):
        os.makedirs(caminho_diretorio)
    
    caminho_arquivo = os.path.join(caminho_diretorio, 'previsao.txt')


    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(formatar_saida(previsao))    
    return caminho_arquivo

''' 

        
def main():
    cidade = input("Digite o nome da cidade para verificar a previsão do tempo: ")
    api_key = key
    previsao = obter_previsao_tempo(cidade, api_key)
    exibir_previsao_tempo(previsao)
  
    

if __name__ == "__main__":
    
    main()