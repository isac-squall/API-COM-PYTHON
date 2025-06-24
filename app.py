# como pegar dados de cotação de varias moedas  

import requests
from tkinter import *


link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(link)

cotacao = requisicao.json()

print(cotacao)  

janela = Tk()

janela.title("Cotação de moedas")
# Reduzindo o tamanho da janela
janela.geometry("400x300")  # Largura x Altura em pixels
janela.resizable(False, False)  # Impede redimensionamento

# Título principal
titulo = Label(janela, text="COTAÇÕES ATUAIS", font=("Arial", 16, "bold"))
titulo.grid(column=0, row=0, pady=10)

# Organizando as cotações de forma mais legível
row = 1
for moeda, dados in cotacao.items():
    # Nome da moeda
    nome_moeda = Label(janela, text=f"{moeda}:", font=("Arial", 12, "bold"))
    nome_moeda.grid(column=0, row=row, sticky="w", padx=20, pady=5)
    
    # Valor da cotação
    valor = dados.get('bid', 'N/A')
    texto_valor = Label(janela, text=f"R$ {valor}", font=("Arial", 11))
    texto_valor.grid(column=1, row=row, sticky="w", padx=10, pady=5)
    
    row += 1

# Adicionando padding geral
janela.configure(padx=20, pady=20)


janela.mainloop()









