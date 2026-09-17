"""Модуль для игры «Угадай число»"""

import random

def handle_game():
    secret = random.randint(1, 100)
    attempts = 0
    
    print("Я загадал число от 1 до 100. Угадай!")
    
    while True:
        digit = input("Введите ваш ответ: ").strip()
        
        if not digit.isdigit():
            print("Ошибка! Введите число.")
            continue
        
        answer = int(digit)
        attempts += 1
        
        if answer < secret:
            print("Загаданное число больше!")
        elif answer > secret:
            print("Загаданное число меньше!")
        else:
            print(f"Поздравляю! Ты угадал за {attempts} попыток!")
            break

if __name__ == "__main__":
    print("Это модуль игры. Запустите main.py для работы бота.")