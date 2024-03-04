import tkinter as tk

class TicTacToe:
    def __init__(self):
        #self.window = tk.Tk()
        #self.window.title("Tic-Tac-Toe")
        #self.window.geometry("200x200")
        self.choice = []

    def createGameBoard(self):
        """
        self.buttons = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
        """
        self.board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
        """
        label = tk.Label(text = "test")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                                                self.window, 
                                                height=5, width=10, 
                                                command = lambda x = i, y = j : self.buttonHandling(x,y))
                self.buttons[i][j].grid(row = i, column = j)
        """
    """
    def buttonHandling(self, x, y):
        self.buttons[x][y].configure(text = f"{self.activePlayer}")
        self.board[x][y] = self.activePlayer
        if self.activePlayer == "X":
            self.activePlayer = "O"
        else:
            self.activePlayer = "X"
    """


    def update_board(self):
        for i in range(3):
                print(self.board[i])
                
        
            

    def runGame(self):
        self.createGameBoard()
        isMaximizingPlayer = True
        while not self.is_over(self.board, isMaximizingPlayer):
            self.update_board()
            move = self.choose_move(self.board, isMaximizingPlayer)
            self.board = self.get_new_state(move, self.board, isMaximizingPlayer)
            isMaximizingPlayer = self.change_player(isMaximizingPlayer)
            


        #self.window.mainloop()
        
    
    def minmax(self, board, isMaximizingPlayer):

        if (self.is_over(board, isMaximizingPlayer)):
            return self.calculate_score(board, isMaximizingPlayer)
        
        if isMaximizingPlayer:
            scores = []
            moves = []
            available_moves = self.get_available_moves(board)
            for move in available_moves:
                possible_board = self.get_new_state(move, board, False)
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
                possible_board = self.get_new_state(move, board, True)
                moves.append(move)
                scores.append(self.minmax(possible_board, True))
            min_score_index = scores.index(min(scores))
            self.choice = moves[min_score_index]
            return scores[min_score_index]
        
        
    
    def is_over(self, board, isMaximizingPlayer):

        if isMaximizingPlayer:
            player = 'X'
        else:
            player = 'O'

        #check rows
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == player:
                    count += 1
                if count == 3:
                    return True
                    
        #check columns
        for j in range(3):
            count = 0
            for i in range(3):
                if board[i][j] == player:
                    count += 1
                if count == 3:
                    return True
                    
        #check first diagonal
        count = 0
        for i in range(3):
            if board[i][i] == player:
                count += 1
            if count == 3:
                return True
                
        #check second diagonal   
        count = 0
        for i in range(3):
            if board[i][i] == player:
                count += 1
            if count == 3:
                return True
                
        #check for draw
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    count += 1
                if count == 9:
                    return True
        
        return False
                
    def calculate_score(self, board, isMaximizingPlayer):
        if isMaximizingPlayer:
            return 10
        else:
            return -10
        
    
    def get_available_moves(self, board):
        avalaible_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    avalaible_moves.append([i, j])
        return avalaible_moves

    def get_new_state(self, move, board, isMaximizingPlayer):
        
        if isMaximizingPlayer:
            board[move[0]][move[1]] = 'X'
        else:
            board[move[0]][move[1]] = 'O'
        
        return board

    def choose_move(self, board, isMaximizingPlayer):
        if isMaximizingPlayer:
            x = int(input("X:"))
            y = int(input("Y:"))
            move = [x, y]
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