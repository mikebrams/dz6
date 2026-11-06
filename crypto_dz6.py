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

print(", ".join(crypto.values()))

def get_rate():
    url = "https://api.2coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto.keys()),
        "vs_currencies": "usd",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        base = crypto_list.get()
        print(base)

    except Exception as e:
        mb.showerror('Ошибка!', f'Ошибка загрузки курсов {e}')
        target_field.config(text=f'{'___'} = {'_' * 7}.00 USD')

root = Tk()
root.title('Курсы популярных криптовалют')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w2 = w // 4
h2 = h // 3
root.geometry(f'350x350+{w2}+{h2}')

frame1 = Frame(bg='lightgray', height=10)
frame1.pack(padx=10, pady=4, fill='both')
base_l = Label(frame1, text='Список популярных криптовалют', font=('Verdana', 10), bg='lightgray')  # Заголовок выпадающего списка
base_l.pack(padx=10, pady=(10, 5), fill='both')
crypto_list = ttk.Combobox(frame1, values=list(crypto.keys()), state='readonly', background='Cornsilk', takefocus=True)  # Выпадающий список криптовалют
crypto_list.current(0)
crypto_list.pack(padx=10, pady=(5, 10), fill='both')


frame2 = Frame(bg='lightgray', height=250)
frame2.pack(padx=10, pady=4, fill='both')
target_l = Label(frame2, text='Целевая валюта', bg='lightgray', font=('Verdana', 10))
target_l.pack(padx=10, pady=(10, 5), fill='both')
target_USD = Label(frame2, text='USD', bg='lightgray', font=('Verdana', 10))
target_USD.pack(padx=10, pady=(5, 10), fill='both')

frame3 = Frame(bg='lightgray', height=10)
frame3.pack(padx=10, pady=4, fill='both')
refresh_btn = Button(frame3, text='Обновить курсы для списка криптовалют', command=get_rate, bg='lightgray', font=('Verdana', 10))
refresh_btn.pack(padx=10, pady=(10, 5), fill='both')
target_field = Label(frame3, text=f'{'___'} = {'_' * 7}.00 USD', font=('Verdana', 10), height=3, bg='Cornsilk')  # Поле для вывода текущего курса
target_field.pack(padx=10, pady=(5, 10), fill='both')

refresh_label = Label(text=f'Курсы обновлены:   {'--.--.----'}   {'--:--:--'}')
refresh_label.pack(pady=5)



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