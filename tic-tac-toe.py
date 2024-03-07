import copy

import tkinter as tk


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("200x200")
        self.choice = []

    def create_game_board(self):

        self.buttons = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]

        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        label = tk.Label(text="test")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                                                self.window, 
                                                height=5, width=10, 
                                                command=lambda x=i, y=j: self.button_handling(x, y))
                self.buttons[i][j].grid(row=i, column=j)

    # TODO Graphics
    def button_handling(self, x, y):
        move = [x, y]
        return move

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="X")

    def runGame(self):
        self.create_game_board()
        isMaximizingPlayer = True
        while not self.is_over(self.board):
            self.window.mainloop()
            move = self.choose_move(self.board, isMaximizingPlayer)
            self.board = self.get_new_state(move, self.board, isMaximizingPlayer)
            isMaximizingPlayer = self.change_player(isMaximizingPlayer)

    def minmax(self, board, isMaximizingPlayer):

        if self.is_over(board):
            return self.calculate_score(board)

        if isMaximizingPlayer:
            scores = []
            moves = []
            available_moves = self.get_available_moves(board)
            for move in available_moves:
                possible_board = self.get_new_state(move, board, True)
                moves.append(move)
                scores.append(self.minmax(possible_board, False))
            max_score_index = scores.index(max(scores))
            self.choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            scores = []
            moves = []
            available_moves = self.get_available_moves(board)
            for move in available_moves:
                possible_board = self.get_new_state(move, board, False)
                moves.append(move)
                scores.append(self.minmax(possible_board, True))
            min_score_index = scores.index(min(scores))
            self.choice = moves[min_score_index]
            return scores[min_score_index]

    def calculate_score(self, board):

        player_max = 'X'
        player_min = 'O'

        # check rows
        for i in range(3):
            count_max = 0
            count_min = 0
            for j in range(3):
                if board[i][j] == player_max:
                    count_max += 1
                if board[i][j] == player_min:
                    count_min += 1
                if count_max == 3:
                    return 10
                if count_min == 3:
                    return -10

        # check columns
        for j in range(3):
            count_max = 0
            count_min = 0
            for i in range(3):
                if board[i][j] == player_max:
                    count_max += 1
                if board[i][j] == player_min:
                    count_min += 1
                if count_max == 3:
                    return 10
                if count_min == 3:
                    return -10

        # check first diagonal
        count_max = 0
        count_min = 0
        for i in range(3):
            if board[i][i] == player_max:
                count_max += 1
            if board[i][i] == player_min:
                count_min += 1
            if count_max == 3:
                return 10
            if count_min == 3:
                return -10

        # check second diagonal
        count_max = 0
        count_min = 0
        for i in range(3):
            if board[i][2 - i] == player_max:
                count_max += 1
            if board[i][2 - i] == player_min:
                count_min += 1
            if count_max == 3:
                return 10
            if count_min == 3:
                return -10

        # check for draw
        return 0


    def is_over(self, board):
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    count += 1
                if count == 9:
                    return True

    def get_available_moves(self, board):
        available_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    available_moves.append([i, j])
        return available_moves

    def get_new_state(self, move, board, isMaximizingPlayer):
        board_copy = copy.deepcopy(board)
        if isMaximizingPlayer:
            board_copy[move[0]][move[1]] = 'X'
        else:
            board_copy[move[0]][move[1]] = 'O'

        return board_copy

    def choose_move(self, board, isMaximizingPlayer):
        if isMaximizingPlayer:

            return move
        else:
            self.minmax(board, isMaximizingPlayer)
            return self.choice

    def change_player(self, isMaximizingPlayer):
        if isMaximizingPlayer:
            return False
        else:
            return True


def main():
    game = TicTacToe()
    game.runGame()


if __name__ == '__main__':
    main()
