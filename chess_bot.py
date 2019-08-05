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
        """ if board[i] == "P":
            print("♙", end="")
        elif board[i] == "R":
            print("♖", end="")
        elif board[i] == "N":
            print("♘", end="")
        elif board[i] == "B":
            print("♗", end="")
        elif board[i] == "Q":
            print("♕", end="")
        elif board[i] == "K":
            print("♔", end="")
        elif board[i] == "p":
            print("♟", end="")
        elif board[i] == "r":
            print("♜", end="")
        elif board[i] == "n":
            print("♞", end="")
        elif board[i] == "b":
            print("♝", end="")
        elif board[i] == "q":
            print("♛", end="")
        elif board[i] == "k":
            print("♚", end="")
        else:
            print(board[i], end="") """


    print()
    print("  ---------------")
    print("  A B C D E F G H")

def move_piece(board, move):
    board.push(chess.Move.from_uci(move))

def evaluate_position(board):
    pst = {
    'P': (  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
            5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
            1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
            0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
            0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
            0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
            0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
            0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0),
    'N': (  -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
            -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
            -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
            -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
            -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
            -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
            -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0),
    'B': (  -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
            -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
            -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
            -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
            -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
            -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
            -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0),
    'R': (  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
            0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
            -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
            -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
            -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
            -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
            -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
            0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0),
    'Q': ( -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
            -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
            -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
            -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
            0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
            -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
            -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0),
    'K': ( -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
            -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
            2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ,
            2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 )
    
    }

    pieces = str(board)
    score = 0
    i = 0
    for char in pieces:
        if char == "P":
            score += 10 + pst["P"][i]
            i += 1
        elif char == "N":
            score += 30 + pst["N"][i]
            i += 1
        elif char == "B":
            score += 30 + pst["B"][i]
            i += 1
        elif char == "R":
            score += 50 + pst["R"][i]
            i += 1
        elif char == "Q":
            score += 90 + pst["Q"][i]
            i += 1
        elif char == "K":
            score += 900 + pst["K"][i]
            i += 1
        elif char == "p":
            score -= 10 + pst["P"][63-i]
            i += 1
        elif char == "n":
            score -= 30 + pst["N"][63-i]
            i += 1
        elif char == "b":
            score -= 30 + pst["B"][63-i]
            i += 1
        elif char == "r":
            score -= 50 + pst["R"][63-i]
            i += 1
        elif char == "q":
            score -= 90 + pst["Q"][63-i]
            i += 1
        elif char == "k":
            score -= 900 + pst["K"][63-i]
            i += 1
        elif char == ".":
            i += 1

    return score

def traverse_tree(board, white, depth):
    best_score = 0
    legal_moves = list(board.legal_moves)
    count = 0

    for m in legal_moves:
        count += 1
        move_piece(board, str(m))
        if depth == 0:
            score = evaluate_position(board)
            if white and score > best_score:
                best_score = score
            elif not white and score < best_score:
                best_score = score
            board.pop()
        else:
            best_score = traverse_tree(board, white, depth-1)
            board.pop()

    return best_score

def best_move(board, white, depth):
    legal_moves = list(board.legal_moves)
    best_score = 0
    last_score = evaluate_position(board)
    move = str(legal_moves[0])
    count = 0


    for m in legal_moves:
        count += 1
        move_piece(board, str(m))
        if depth == 0:
            score = evaluate_position(board)
        else:
            score = traverse_tree(board, white, depth-1)

        if white and score > best_score:
            best_score = score
            move = str(board.peek())
        elif not white and score < best_score:
            best_score = score
            move = str(board.peek())
        board.pop()
        

    if best_score == last_score:
        print("Random Move")
        move = str(random.choice(legal_moves))
    
    print(move)
    
    return move

board = chess.Board()
white_score = 0

print("----------------------------------------------------")
print("Score: " + str(white_score))
print_board(board)

while board.is_checkmate:
    # User plays white
    """ while board.turn:
        white_move = input("Your Move: ")
        try:
            move_piece(board, white_move)
        except:
            print("Illegal Move! Try again") """
    
    print("White Move")
    white_move = best_move(board, True, 3)
    move_piece(board, white_move)

    white_score = evaluate_position(board)

    print("----------------------------------------------------")
    print("Score: " + str(white_score))
    print_board(board)
    
    #input()

    print("Black Move")
    black_move = best_move(board, False, 3)
    move_piece(board, black_move)
    
    white_score = evaluate_position(board)
    
    print("----------------------------------------------------")
    print("Score: " + str(white_score))
    print_board(board)

    #input()