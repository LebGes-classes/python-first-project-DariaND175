import random


class Maze:
    def __init__(self, level: int = 1) -> None:
        """Инициализатор класса.

        Args:
            level: Уровень в лабиринте
        """

        self.__size = 5 + level
        self.__level = level
        self.__maze = self.generate_maze()
        self.__player_position = [0, 0]
        self.__moves_count = 0

    def set_level(self, level):
        if 1 <= level <= 30:
            self.__level = level
            self.__size = 5 + level
            self.__maze = self.generate_maze()
            self.__player_position = [0, 0]
            self.__moves_count = 0
        else:
            raise ValueError('Введите уровень от 1 до 30')

    def get_size(self) -> int:
        """Геттер для размера лабиринта.

        Returns:
                size: Размер лабиринта
        """

        return self.__size

    def get_level(self) -> int:
        """Геттер для уровня лабиринта.

        Returns:
                level: Уровень лабиринта
        """

        return self.__level

    def get_maze(self) -> list:
        """Геттер для лабиринта.

        Returns:
                maze: Вывод лабиринта
        """

        return [row[:] for row in self.__maze]

    def generate_maze(self) -> list:
        """Генерирует простой лабиринт

        Returns:
            maze: Вывод итогового лабиринта
        """

        maze = []

        for y in range(self.__size):
            row = []
            for x in range(self.__size):
                if x == 0 and y == 0:
                    row.append('⬜')
                elif x == self.__size - 1 and y == self.__size - 1:
                    row.append('⬜')
                elif random.random() < 0.7:
                    row.append('⬜')
                else:
                    row.append('🧱')
            maze.append(row)

        self._create_guaranteed_path(maze)
        return maze

    def _create_guaranteed_path(self, maze):
        """Создает гарантированный путь от начала до конца"""

        for x in range(1, self.__size):
            maze[0][x] = '⬜'

        for y in range(1, self.__size):
            maze[y][self.__size - 1] = '⬜'

    def level_up(self) -> bool:
        """Повышает уровень

        Returns:
                булево значение
        """

        if self.__level >= 30:
            print('Достигнут максимальный уровень')
            return False
        else:
            self.set_level(self.__level + 1)
            print(f'Переход на уровень {self.__level}!')
            return True

    def level_down(self) -> bool:
        """Понижает уровень

        Returns:
                булево значение
        """

        if self.__level <= 1:
            print('Достигнут минимальный уровень')
            return False
        else:
            self.set_level(self.__level - 1)
            print(f'Возврат на уровень {self.__level}!')
            return True

    def print_maze(self) -> None:
        """Выводит лабиринт с игроком"""

        border_length = self.__size * 2
        print('┌' + '─' * border_length + '┐')

        for y in range(self.__size):
            print('│', end='')

            for x in range(self.__size):
                if [x, y] == self.__player_position:
                    print('🎅', end='')
                elif x == self.__size - 1 and y == self.__size - 1:
                    print('🎄', end='')
                else:
                    print(self.__maze[y][x], end='')

            print('│')

        print('└' + '─' * border_length + '┘')
        print(f"Уровень: {self.__level} | Ходов: {self.__moves_count}")

    def move_player(self, direction: str) -> bool:
        """Двигает игрока по лабиринту

        Returns:
              булево значение
        """

        x, y = self.__player_position

        if direction == 'w' and y > 0:
            new_x, new_y = x, y - 1
        elif direction == 's' and y < self.__size - 1:
            new_x, new_y = x, y + 1
        elif direction == 'a' and x > 0:
            new_x, new_y = x - 1, y
        elif direction == 'd' and x < self.__size - 1:
            new_x, new_y = x + 1, y
        else:
            return False

        if self.__maze[new_y][new_x] == '⬜':
            self.__player_position = [new_x, new_y]
            self.__moves_count += 1

            if new_x == self.__size - 1 and new_y == self.__size - 1:
                return True

        return False

    def reset_position(self) -> None:
        """Сбрасывает позицию игрока """

        self.__player_position = [0, 0]
        self.__moves_count = 0

    def win_in_game(self) -> bool:
        """Проверяет, достиг ли игрок выхода
        Returns:
            сравнение с клеткой выхода
        """

        x, y = self.__player_position
        return x == self.__size - 1 and y == self.__size - 1


