from Menu import (
    Menu,
)



def run():
    """Запуск программы"""

    menu = Menu()
    running = True

    while running:
        menu.clear_screen()
        menu.show_menu()

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice.isdigit():
            running = menu.main_menu(int(choice))
        else:
            print("❌ Пожалуйста, введите число от 1 до 4")
            input("Нажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    run()