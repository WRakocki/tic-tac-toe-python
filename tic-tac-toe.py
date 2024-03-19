import copy
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("450x490")
        self.create_game_board()
        self.create_gui()
        self.choice = []
        self.is_maximizing_player = True

    def create_game_board(self):

        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def create_gui(self):

        self.buttons = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=('normal', 20), width=8, height=4,
                                               command=lambda x=i, y=j: self.make_move(x, y))
                self.buttons[i][j].grid(row=i, column=j)

    def update_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    symbol = ""
                else:
                    symbol = self.board[i][j]
                self.buttons[i][j].config(text=symbol)

    def make_move(self, x, y):
        if self.board[x][y] == 0 and not self.is_over(self.board):
            self.board[x][y] = 'X'
            self.update_board()
            self.is_maximizing_player = False

        if not self.is_maximizing_player and not self.is_over(self.board):
            move = self.choose_move(self.board, False)
            self.board = self.get_new_state(move, self.board, False)
            self.update_board()
            self.is_maximizing_player = True

        if self.is_over(self.board):
            winner = self.calculate_score(self.board)
            if winner == 10:
                if messagebox.askquestion("GAME OVER", "YOU WIN!\nRESTART?") == 'yes':
                    self.window.destroy()
                    main()
                else:
                    exit()
            elif winner == -10:
                if messagebox.askquestion("GAME OVER", "YOU LOSE!\nRESTART?") == 'yes':
                    self.window.destroy()
                    main()
                else:
                    exit()
            else:
                if messagebox.askquestion("GAME OVER", "DRAW!\nRESTART?") == 'yes':
                    self.window.destroy()
                    main()
                else:
                    exit()

    def run_game(self):
        self.window.mainloop()

    def minmax(self, board, is_maximizing_player):

        if self.is_over(board):
            return self.calculate_score(board)

        if is_maximizing_player:
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

    def is_over(self, board):
        if self.calculate_score(board) == 10:
            return True
        elif self.calculate_score(board) == -10:
            return True
        else:
            # Check for draw
            count = 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] != 0:
                        count += 1
                    if count == 9:
                        return True
        return False

    def choose_move(self, board, is_maximizing_player):
        self.minmax(board, is_maximizing_player)
        return self.choice

    @staticmethod
    def get_available_moves(board):
        available_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    available_moves.append([i, j])
        return available_moves

    @staticmethod
    def get_new_state(move, board, is_maximizing_player):
        board_copy = copy.deepcopy(board)
        if is_maximizing_player:
            board_copy[move[0]][move[1]] = 'X'
        else:
            board_copy[move[0]][move[1]] = 'O'

        return board_copy

    @staticmethod
    def calculate_score(board):

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


def main():
    window = tk.Tk()
    game = TicTacToe(window)
    game.run_game()


if __name__ == '__main__':
    main()
