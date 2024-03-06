def print_board(board):
    """
    Функция для вывода игрового поля в консоль с номерами строк и столбцов.
    """
    print("  1 2 3")
    for i, row in enumerate(board, start=1):
        print(f"{i} {'|'.join(row)}")
        if i < 3:
            print("  -----")


def check_win(board):
    """
    Функция для проверки победы.
    Проверяет строки, столбцы и диагонали на предмет одинаковых символов.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False


def check_draw(board):
    """
    Функция для проверки ничьей.
    Проверяет, есть ли на поле свободные клетки.
    """
    for row in board:
        if ' ' in row:
            return False
    return True


def game():
    """
    Основная функция игры.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Игрок {current_player}, сделайте свой ход (введите сроку[1-3] и столбец[1-3]):")
        move = input().split()
        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            print("Такой ход недопустим, введите 2 цифры (номер строки и номер столбца) через пробел")
            continue
        row, col = int(move[0]) - 1, int(move[1]) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Выход за границы поля! Поле ограничено 3 ячейками по вертикали и горизонтали. Повторите попытку!")
            continue
        if board[row][col] != ' ':
            print("Данное поле уже занято! Сделайте другой ход! ")
            continue
        board[row][col] = current_player
        if check_win(board):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    game()