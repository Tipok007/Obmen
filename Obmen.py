from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_b_label_2(event):
    code = b_combobox_2.get()
    name = cur[code]
    b_label_2.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    b_code_2 = b_combobox_2.get()

    if t_code and b_code and b_code_2:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()  # Проверяем, не произошла ли ошибка HTTP

            data = response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс для {b_name}: {exchange_rate:.2f} {t_name} за 1 {b_name}")

            if t_code in data['rates']:
                exchange_rate_2 = data['rates'][t_code]
                t_name = cur[t_code]
                b_name_2 = cur[b_code_2]
                mb.showinfo("Курс обмена", f"Курс для {b_name_2}: {exchange_rate_2:.2f} {t_name} за 1 {b_name_2}")

        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")  # Создание графического интерфейса


cur = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"
}

window = Tk()
window.title("Курс обмена валюты ")
window.geometry("360x450")

# Выбор первой базовой валюты
Label(text="Первая базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

# Выбор второй базовой валюты
Label(text="Вторая базовая валюта").pack(padx=10, pady=10)
b_combobox_2 = ttk.Combobox(values=list(cur.keys()))
b_combobox_2.pack(padx=10, pady=10)
b_combobox_2.bind("<<ComboboxSelected>>", update_b_label_2)
b_label_2 = ttk.Label()
b_label_2.pack(padx=10, pady=10)

# Выбор целевой валюты
Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()