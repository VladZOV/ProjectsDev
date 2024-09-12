def create_board() -> list[list[str]]:  # двумерный список представляющий доску
    return [[' ' for j in range(3)] for i in range(3)]


def print_board(board) -> list[list[str]]:  # добавляю разделения на доске
    for row in board:
        print('|'.join(row))


def is_valid_move(board: list[list[str]], row: int, col: int) -> bool:  # проверяю правильность хода

    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


def make_move(board: [list[list[str]]], row: int, col: int, player: str) -> bool: # реализация хода
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    else:
        print("Неверный ввод, повторите")
    return False


def check_win(board: list[list[str]], player: str) -> bool:  # проверяю ряды, столбцы и диагонали
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # верхний ряд
        [(1, 0), (1, 1), (1, 2)],  # средний ряд
        [(2, 0), (2, 1), (2, 2)],  # нижний ряд
        [(0, 0), (1, 0), (2, 0)],  # левый столбец
        [(0, 1), (1, 1), (2, 1)],  # средний столбец
        [(0, 2), (1, 2), (2, 2)],  # правый столбец
        [(0, 0), (1, 1), (2, 2)],  # диагональ слева направо
        [(0, 2), (1, 1), (2, 0)]  # диагональ справа налево
    ]

    for combination in win_combinations:
        if all(board[row][col] == player for row, col in combination):
            return True
    return False


def is_board_full(board: list[list[str]]) -> bool:  # проверка на заполнение доски

    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True


def play_game() -> None: # запуск игры
    board = create_board()
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Игрок {players[current_player]} введи номер строки (0-2): "))
        col = int(input(f"Игрок {players[current_player]} введи номер столбца (0-2): "))

        if make_move(board, row, col, players[current_player]):
            if check_win(board, players[current_player]):
                print_board(board)
                print(f"Игрок {players[current_player]} победил!")
                break
            if is_board_full(board):
                print_board(board)
                print("Ничья!")
                break
            current_player = (current_player + 1) % 2


play_game()