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
        if self.activePlayer == "X":
            self.activePlayer = "O"
        else:
            self.activePlayer = "X"

    
    def runGame(self):
        self.createGameBoard()
        self.window.mainloop()



def main():
    game = TicTacToe()
    game.runGame()
    

if __name__ == '__main__':
    main()