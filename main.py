def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if board[i] == [player] * 3:
            return True
        if [board[j][i] for j in range(3)] == [player] * 3:
            return True
    if [board[i][i] for i in range(3)] == [player] * 3:
        return True
    if [board[i][2-i] for i in range(3)] == [player] * 3:
        return True
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Invalid move! Try again.")
            continue

        if check_win(board, player):
            print(f"Player {player} wins!")
            break

        if all(all(cell != ' ' for cell in row) for row in board):
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

# Example usage
tic_tac_toe()




































