import tkinter as tk

class TicTacToe:
    def __init__(self):
        #self.window = tk.Tk()
        #self.window.title("Tic-Tac-Toe")
        #self.window.geometry("200x200")
        self.activePlayer = "X"

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
        if self.activePlayer == 'X':
            x = int(input("X: "))
            y = int(input("Y: "))
            self.board[x][y] = 'X'
            for i in range(3):
                print(self.board[i])
            self.activePlayer = 'O'
        else:
            self.minmax(self.board)
            

    def runGame(self):
        self.createGameBoard()
        while True:
            self.update_board()
        #self.window.mainloop()
        
    
    def minmax(self, board):

        if (self.is_over(board)):
            return self.calculate_score(board)
        
        scores = []
        moves = []

        available_moves = self.get_available_moves(board)

        for move in available_moves:
            possible_board = self.get_new_state(move, board)
            scores.append(self.minmax(possible_board))
            moves.append(move)

        if self.activePlayer == 'X':
            max_score_index = scores.index(max(scores))
            choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            choice = moves[min_score_index]
            return scores[min_score_index]
    
    def is_over(self, board):
        #check rows
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == 'X':
                    count += 1
                if count == 3:
                    return True
                    
        #check columns
        for j in range(3):
            count = 0
            for i in range(3):
                if board[i][j] == 'X':
                    count += 1
                if count == 3:
                    return True
                    
        #check first diagonal
        count = 0
        for i in range(3):
            if board[i][i] == 'X':
                count += 1
            if count == 3:
                return True
                
        #check second diagonal   
        count = 0
        for i in range(3):
            if board[i][i] == 'X':
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
                
    def calculate_score(self, board):
        if self.activePlayer == 'X':
            return 10
        elif self.activePlayer == 'O':
            return -10
        else:
            return 0
    
    def get_available_moves(self, board):
        avalaible_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    avalaible_moves.append([i, j])
        return avalaible_moves

    def get_new_state(self, move, board):
        board[move[0]][move[1]] = 'O'
        return board

        
            

        



def main():
    game = TicTacToe()
    game.runGame()
    

if __name__ == '__main__':
    main()