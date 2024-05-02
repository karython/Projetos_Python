# Projeto: Consulta de Tabela de Campeonato de Futebol

Este é um projeto em Python que utiliza a API do [API Futebol](https://www.api-futebol.com.br/) para consultar e exibir a tabela de um campeonato de futebol.

## Funcionalidades
- Consulta e exibição da tabela de um campeonato de futebol específico.
- Utiliza a biblioteca `requests` para fazer solicitações HTTP à API do API Futebol.
- Utiliza a biblioteca `pandas` para manipulação e apresentação dos dados da tabela em formato tabular.

## Pré-requisitos
- É necessário ter uma chave de API válida do API Futebol. Você pode obtê-la em [API Futebol](https://www.api-futebol.com.br/).
- Certifique-se de ter as bibliotecas `requests` e `pandas` instaladas. Você pode instalá-las usando pip:
  ```bash
  pip install requests pandas
  ```

## Como usar
1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/consulta-tabela-campeonato.git
   ```

2. No arquivo `credenciais.py`, substitua `fut_key` pela sua chave de API do API Futebol.

3. Execute o script `consulta_tabela.py`:
   ```bash
   python consulta_tabela.py
   ```

4. O script irá consultar a tabela do campeonato especificado e exibirá os dados formatados em formato tabular.

## Exemplo de Saída
```
   posicao            time  jogos  saldo_gols  vitorias  derrotas
0        1         Flamengo     10           8         6         0
1        2        Palmeiras     10           5         6         1
2        3       Fluminense     10           3         5         1
3        4       Bragantino     10           5         4         1
4        5           Santos     10           4         3         1
...
```

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato
Para qualquer dúvida ou sugestão, entre em contato com o autor:

Nome: Seu Nome  
Email: karython.unai@gmail.com
```

Este README.md fornece uma visão geral do projeto, explicando suas funcionalidades, requisitos, como usá-lo e informações de contato.
