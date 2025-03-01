# como pegar dados de cotação de varias moedas  

import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(link)

cotacao = requisicao.json()

print(cotacao)  










