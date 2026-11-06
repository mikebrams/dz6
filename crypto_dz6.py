from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

crypto = {
    'bitcoin': 'BTC',
    'pax-gold': 'PAXG',
    'tether-gold': 'XAUT',
    'ethereum': 'ETH',
    'zcash': 'ZEC',
    'binancecoin': 'BNB',
    'monero': 'XMR',
    'bitcoin-cash': 'BCH',
    'bittensor': 'TAO',
    'quant-network': 'QNT',
    'solana': 'SOL',
    'hyperliquid': 'HYPE',
}


def get_rate():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto.keys()),
        "vs_currencies": "usd",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()


root = Tk()
root.title('Курсы популярных криптовалют')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w2 = w // 4
h2 = h // 3
root.geometry(f'300x350+{w2}+{h2}')

base_l = Label(text='Базовая криптовалюта')  # Заголовок выпадающего списка
base_l.pack()

crypto_list = ttk.Combobox(values=list(crypto.keys()))  # Выпадающий список криптовалют
crypto_list.pack()

target_l = Label(text='Целевая валюта')
target_l.pack()

target_USD = Label(text='USD')
target_USD.pack()

target_field = Label(text=f'1 {'---'} = {' ' * 7}.00 USD', height=3, width=12)  # Поле для вывода текущего курса
target_USD.pack()

refresh_label = Label(text=f'Дата и время обновления: {'--.--.----'} {'--:--:--'}')
refresh_label.pack()

refresh_btn = Button(text='Обновить курсы', command=get_rate)
refresh_btn.pack()

root.mainloop()


data_json = {'binancecoin': {'usd': 697.07},
 'bitcoin': {'usd': 75825},
 'bitcoin-cash': {'usd': 267.75},
 'bittensor': {'usd': 226.54},
 'ethereum': {'usd': 2238.24},
 'hyperliquid': {'usd': 79.12},
 'monero': {'usd': 621.68},
 'pax-gold': {'usd': 4022.12},
 'quant-network': {'usd': 191.71},
 'solana': {'usd': 91.14},
 'tether-gold': {'usd': 4017.67},
 'zcash': {'usd': 1370.73}}