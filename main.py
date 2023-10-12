import random

board = [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-------")
        
def player_move():
    while True:
        display_board(board)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("That cell is already occupide. Try again.")
            
            
def check_win(baord, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(2)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False


def check_draw(board):
    for row in board:
        if " " in row:
            return False
        return True
    
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return -1
    if check_draw(board):
        return 0
    
    
    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score
    
    
def playe_game():
    current_player = "X"
    while True:
        if current_player == "X":
            player_move()
        else:
            best_move = None
            best_score = -float("inf")
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "O"
                        score = minimax(board, 0, False)
                        board[row][col] = " "
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
            if best_move:
                row, col = best_move
                board[row][col] = "O"
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    playe_game()