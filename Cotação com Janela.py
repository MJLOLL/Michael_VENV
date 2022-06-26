import requests
from tkinter import*


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto



# criar a janela principal
janela = Tk()

janela.title("Cotação atual da moeda") # titulo da janela
janela.geometry("300x250")

texto_orienacao = Label(janela, text='Clique aqui pata ver as cotações')
texto_orienacao.grid(column=0, row=0, padx=30, pady=30)

botao = Button(janela, text="clique aqui", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=20, pady=20)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

#texto_orienacao2 = Label(janela, text='Clique aqui pata ver as cotações')
#texto_orienacao2.grid(column=0, row=1)

janela.mainloop() # impede que a janela feche automaticamente