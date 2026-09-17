"""Модуль с обработчиками команд"""

from api import get_rate
from notes import handle_note
from game import handle_game

def show_help():
    print("--- Доступные команды ---")
    print("- help - список команд")
    print("- exit - выход")
    print("- course - курс валют")
    print("- note - заметки")
    print("- game - игра")

def handle_course():
    code = input("Введите код валюты:").strip().upper()
    rate = get_rate(code)

    if rate is None:
        print(f"Валюта '{code}' не найдена или произошла ошибка.")
        return

    amount_input = input(f"Введите количество {code} валюты:").strip()

    try:
        amount = float(amount_input)
    except ValueError:
        print("Ошибка! Введите число.")
        return

    result = amount * rate
    print(f"{amount} {code} = {round(result, 2)} RUB")

if __name__ == "__main__":
    print("Это модуль команд. Запустите main.py для работы бота.")