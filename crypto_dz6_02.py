from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from datetime import datetime


def target_field_update(event=None):
    item = crypto_list.get()
    base = crypto[item]
    if crypto_base:
        try:
            rate = crypto_base[base]['usd']
            target_field.config(text=f'{item} = {rate:>10.2f} USD')
        except KeyError:
            target_field.config(text=f'{'___'} = {'_' * 7}.00 USD')
            mb.showerror('Ошибка', f'Валюта {item} отсутствует в ответе API')
    else:
        target_field.config(text='Ошибка при загрузке курсов криптовалют')


def refresh_rates():
    global crypto_base
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto.values()),
        "vs_currencies": "usd",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        crypto_base = response.json()
        print(crypto_base)

        now = datetime.now()
        refresh_label.config(text=f'Курсы обновлены:   {now.strftime("%d.%m.%Y")}   {now.strftime("%H:%M:%S")}')

    except Exception as e:
        mb.showerror('Ошибка', f'Ошибка загрузки курсов {e}')
        target_field.config(text='Ошибка при загрузке курсов криптовалют')
        refresh_label.config(text='Курсы обновлены:   --.--.----   --:--:--')


crypto = {
    'Bitcoin (BTC)': 'bitcoin',
    'Binancecoin (BNB)': 'binancecoin',
    'Bitcoin-cash (BCH)': 'bitcoin-cash',
    'Bittensor (TAO)': 'bittensor',
    'Ethereum (ETH)': 'ethereum',
    'Hyperliquid (HYPE)': 'hyperliquid',
    'Monero (XMR)': 'monero',
    'Pax-gold (PAXG)': 'pax-gold',
    'Quant-network (QNT)': 'quant-network',
    'Solana (SOL)': 'solana',
    'Tether-gold (XAUT)': 'tether-gold',
    'Zcash (ZEC)': 'zcash'
}

crypto_base = {}

root = Tk()
root.title('Курсы популярных криптовалют')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w2 = w // 4
h2 = h // 3
root.geometry(f'350x350+{w2}+{h2}')

frame1 = Frame(bg='lightgray', height=10)
frame1.pack(padx=10, pady=4, fill='both')
base_l = Label(frame1, text='Список популярных криптовалют', font=('Verdana', 10),
               bg='lightgray')  # Заголовок выпадающего списка
base_l.pack(padx=10, pady=(10, 5), fill='both')
crypto_list = ttk.Combobox(frame1, values=list(crypto.keys()), state='readonly')  # Выпадающий список криптовалют
crypto_list.current(0)
crypto_list.pack(padx=10, pady=(5, 10), fill='both')
crypto_list.bind('<<ComboboxSelected>>', target_field_update)

frame2 = Frame(bg='lightgray', height=250)
frame2.pack(padx=10, pady=4, fill='both')
target_l = Label(frame2, text='Целевая валюта', bg='lightgray', font=('Verdana', 10))
target_l.pack(padx=10, pady=(10, 5), fill='both')
target_USD = Label(frame2, text='USD', bg='lightgray', font=('Verdana', 10))
target_USD.pack(padx=10, pady=(5, 10), fill='both')

frame3 = Frame(bg='lightgray', height=10)
frame3.pack(padx=10, pady=4, fill='both')
refresh_btn = Button(frame3, text='Обновить курсы для списка криптовалют', command=refresh_rates, bg='lightgray',
                     font=('Verdana', 10))
refresh_btn.pack(padx=10, pady=(10, 5), fill='both')
target_field = Label(frame3, text='Загрузка... ', font=('Verdana', 10), height=3,
                     bg='WhiteSmoke')  # Поле для вывода текущего курса
target_field.pack(padx=10, pady=(5, 10), fill='both')

refresh_label = Label(text='Загрузка... ', fg='DimGray')
refresh_label.pack(pady=2)

auto_label = Label()
# auto_label = Label(text=f'Обновление через:   {'--'} сек.', fg='DimGray')
auto_label.pack(pady=2)


refresh_rates()
target_field_update()

root.mainloop()
