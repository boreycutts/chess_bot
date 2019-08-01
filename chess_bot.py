import chess
import chess.svg
import random

def print_board(board):
    board = str(board)
    print()
    for i in range(len(board)):
        if (i)%16 == 0:
            print(str(int((112 - i)/16 + 1)) + "|", end="")
        print(board[i], end="")

    print()
    print("  ---------------")
    print("  A B C D E F G H")

def move_piece(board, move):
    board.push(chess.Move.from_uci(move))
        


board = chess.Board()

while board.is_checkmate:
    while board.turn:
        white_move = input("Your Move: ")
        try:
            move_piece(board, white_move)
        except:
            print("Illegal Move! Try again")
    
    black_move = random.choice(list(board.legal_moves))
    move_piece(board, str(black_move))
    print_board(board)