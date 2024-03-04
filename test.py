def choose_move(board, isMaximizingPlayer):
        if isMaximizingPlayer:
            x = int(input("X:"))
            y = int(input("Y:"))
            move = [x, y]
            return move
        else:
            return [0,1]

def get_new_state(move, board, isMaximizingPlayer):
        
        if isMaximizingPlayer:
            board[move[0]][move[1]] = 'X'
        else:
            board[move[0]][move[1]] = 'O'
        
        return board

board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]

move = choose_move(board, True)
board = get_new_state(move, board, True)
print(board)
move = choose_move(board, False)
board = get_new_state(move, board, False)
print(board)