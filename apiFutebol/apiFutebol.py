import requests
import pandas as pd
import os
from credenciais import fut_key


key = fut_key

headers = {"Authorization": f"Bearer {key}"}
base_url = 'https://api.api-futebol.com.br/v1/'

def obter_tabela (campeonato_id):
    url = f"{base_url}campeonatos/{campeonato_id}/tabela"
    resposta = requests.get(url, headers=headers)
    dados = resposta.json()
    return dados


df = pd.DataFrame(obter_tabela(campeonato_id=10))

df['time'] = df['time'].apply(lambda x: x['nome_popular'])
df_tabela = df[['posicao', 'time', 'jogos', 'saldo_gols', 'vitorias','derrotas' ]]

print(df_tabela)