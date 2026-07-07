import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-"*5)

def check_winner(b, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[pos] == player for pos in combo) for combo in wins)

def is_draw():
    return " " not in board

def minimax(b, depth, is_max):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, depth+1, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, depth+1, True))
                b[i] = " "
        return best

def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

print("Tic-Tac-Toe")
print("You are X")
print("AI is O")

while True:
    print_board()

    try:
        move = int(input("Enter position (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number.")
        continue

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    if check_winner(board, "X"):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner(board, "O"):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break
