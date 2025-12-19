from maze import (
    Maze,
)


class Menu:
    """Класс для работы пользовательского меню."""

    def __init__(self):
        self.maze = Maze()

    def clear_screen(self):
        """Очищает экран"""

        print('\n' * 30)

    def show_menu(self):
        """Вывод пользовательского меню."""

        print(f"""
            {'=' * 40}
            НОВОГОДНИЙ ЛАБИРИНТ 🎅
            {'=' * 40}
            Уровень: {self.maze.get_level()}
            Размер: {self.maze.get_size()}x{self.maze.get_size()}
            {'=' * 40}

            Выберите действие:
            1. 🎁 НАЧАТЬ ИГРУ
            2. 🪄 УМЕНЬШИТЬ УРОВЕНЬ
            3. 🎉 УВЕЛИЧИТЬ УРОВЕНЬ
            4. ☃️ ВЫЙТИ ИЗ ПРОГРАММЫ
            {'=' * 40}
        """)

    def main_menu(self, choice):
        """Обрабатывает выбор меню"""

        if choice == 1:
            self.play_game()

            return True
        elif choice == 2:
            if self.maze.level_down():
                print(f"Текущий уровень: {self.maze.get_level()}")
            input("\nНажмите Enter чтобы продолжить...")

            return True
        elif choice == 3:
            if self.maze.level_up():
                print(f"Текущий уровень: {self.maze.get_level()}")

            input("\nНажмите Enter чтобы продолжить...")

            return True
        elif choice == 4:
            print("\n🎄 Счастливого Нового Года! 🎄")

            return False
        else:
            print("\n❌ Неверный выбор!")

            input("Нажмите Enter чтобы продолжить...")

            return True

    def play_game(self):
        """Запускает игру"""

        self.clear_screen()

        print("=" * 40)
        print("НОВОГОДНИЙ ЛАБИРИНТ".center(40))
        print("=" * 40)
        print("Цель: дойти от 🎅 до 🎄".center(40))
        print("=" * 40)
        print("Управление:")
        print("  W - Вверх")
        print("  A - Влево")
        print("  S - Вниз")
        print("  D - Вправо")
        print("  E - Выход в меню")
        print("=" * 40)
        input("Нажмите Enter чтобы начать...")

        self.maze.reset_position()

        game_active = True
        game_won = False

        while game_active and not game_won:
            self.clear_screen()
            self.maze.print_maze()

            if self.maze.win_in_game():
                print("\n" + "=" * 40)
                print("🎉 ПОЗДРАВЛЯЕМ! ВЫ НАШЛИ ВЫХОД! 🎉".center(40))
                print("=" * 40)
                print(f"Ходов сделано: {self.maze._Maze__moves_count}".center(40))

                if self.maze.get_level() < 30:
                    print("\n" + "-" * 40)

                    answer = input("Хотите перейти на следующий уровень? (y/n): ").lower()

                    if answer == 'y':
                        self.maze.level_up()
                        self.maze.reset_position()

                        continue

                game_won = True

                input("\nНажмите Enter чтобы вернуться в меню...")

                continue

            print("\n" + "-" * 40)

            command = input("Ваш ход (W/A/S/D) или E для выхода: ").lower()

            if command == 'e':

                print("\nВозвращаемся в главное меню...")

                input("Нажмите Enter...")

                game_active = False
            elif command in ['w', 'a', 's', 'd']:
                self.maze.move_player(command)
            else:
                print("❌ Неверная команда! Используйте W, A, S, D или E")

                input("Нажмите Enter чтобы продолжить...")


