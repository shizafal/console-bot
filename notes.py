"""Модуль для работы с заметками"""

import json

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Файл заметок повреждён. Создаю новый.")
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def add_notes(notes):
    note = input("Введите текст заметки:")
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена!")

def show_notes(notes): 
    if not notes:
        print("Заметок нет.")
        return False
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
    return True

def delete_notes(notes):
    if not show_notes(notes):
        return
    num = input("Введите номер для удаления: ")
    if not num.isdigit():
        print("Ошибка! Введите число.")
        return
    index = int(num) - 1
    if 0 <= index < len(notes):
        deleted = notes.pop(index)
        save_notes(notes)
        print(f"Заметка {deleted} удалена.")
    else:
        print("Заметка с таким номером не найдена.")


def handle_note():

    notes = load_notes()

    while True:
        print("--- Добро пожаловать в заметки ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку")
        print("4. Назад")

        choice = input("Введите номер действия:")

        if choice == "1":
            add_notes(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            delete_notes(notes)
        elif choice == "4":
            print("Выход из заметок!")
            break
        else:
            print("Неверный выбор. Введите 1-4.")

if __name__ == "__main__":
    print("Это модуль заметок. Запустите main.py для работы бота.")
    