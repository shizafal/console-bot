from commands import show_help, handle_course, handle_note, handle_game

def main():
    print("=== Консольный мульти-бот ===")
    print("Введите 'help' для списка команд.")

    while True:
        command = input("\n> ").strip().lower()

        if command == "exit":
            print("До свидания!")
            break
        elif command == "help":
            show_help()
        elif command == "course":
            handle_course()
        elif command == "note":
            handle_note()
        elif command == "game":
            handle_game()
        else:
            print("Команда не найдена. Введите 'help'.")

if __name__ == "__main__":
    main()
