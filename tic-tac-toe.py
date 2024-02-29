import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("200x200")
        self.activePlayer = "X"

    def createGameBoard(self):
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
        
        label = tk.Label(text = "test")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                                                self.window, 
                                                height=5, width=10, 
                                                command = lambda x = i, y = j : self.buttonHandling(x,y))
                self.buttons[i][j].grid(row = i, column = j)
    
    def buttonHandling(self, x, y):
        self.buttons[x][y].configure(text = f"{self.activePlayer}")
        self.board[x][y] = self.activePlayer
        if self.activePlayer == "X":
            self.activePlayer = "O"
        else:
            self.activePlayer = "X"
        

    
    def runGame(self):
        self.createGameBoard()
        self.window.mainloop()
        
    
    def minmax(self, game):

        if (self.is_over(game)):
            return 10
        scores = []
        moves = []

        available_moves = self.get_available_moves()

        for move in available_moves:
            possible_game = self.get_new_state(move)
            scores.append(self.minmax(possible_game))
            moves.append(move)

        if self.activePlayer == 'X':
            max_score_index = scores.index(max(scores))
            choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            choice = moves[min_score_index]
            return scores[min_score_index]
    
    def is_over(game):
        #check rows
        for i in range(3):
            count = 0
            for j in range(3):
                if game[i][j] == 'X':
                    count += 1
                if count == 3:
                    print("ROWS")
                    return True
                    
        #check columns
        for j in range(3):
            count = 0
            for i in range(3):
                if game[i][j] == 'X':
                    count += 1
                if count == 3:
                    print("COLUMNS")
                    return True
                    
        #check first diagonal
        count = 0
        for i in range(3):
            if game[i][i] == 'X':
                count += 1
            if count == 3:
                print("DIAGONAL")
                return True
                
        #check second diagonal   
        count = 0
        for i in range(3):
            if game[i][i] == 'X':
                count += 1
            if count == 3:
                print("ANTI")
                return True
                
        #check for draw
        count = 0
        for i in range(3):
            for j in range(3):
                if game[i][j] != 0:
                    count += 1
                if count == 9:
                    print("Draw")
                    return True
                
            
            

        



def main():
    game = TicTacToe()
    game.runGame()
    

if __name__ == '__main__':
    main()