import tkinter as tk
import random
from tkinter import messagebox


nums_ok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def generate_numbers():
    seq_1_to_15 = list(range(1, 16))
    random.shuffle(seq_1_to_15)
    print(seq_1_to_15)
    return seq_1_to_15


class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.CreateWidgets()

    def CreateWidgets(self):
        for i in range(0, 5):
            self.rowconfigure(i, weight=1)
        for i in range(0, 4):
            self.columnconfigure(i, weight=1)
        self.newgame_button = tk.Button(self, text='New Game', command=self.NewGame)
        self.newgame_button.grid(column = 0, row = 0, columnspan = 4, sticky = "NEW")
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(column = 3, row = 5, columnspan = 2)

        self.squares = [[tk.Button(self) for j in range(4)] for i in range(4)]
        self.empty_cell = (3, 3)

    
    def NewGame(self):
        numbers = generate_numbers()
        for i in range(0, 4):
            for j in range(0, 4):
                if i == 3 and j == 3:
                    self.squares[i][j].grid_forget()
                    break
                self.squares[i][j].config(text = numbers[i * 4 + j], command = self.Move(i, j))
                self.squares[i][j].grid(column = i, row = j + 1, sticky = "NEWS")
        print(self.squares[1][1]["text"])

    def Move(self, i, j):
        def process_shift():
            print("MOVING", i, j)
            empty_col = self.empty_cell[0]
            empty_row = self.empty_cell[1]
            if i == empty_col:
                diff = empty_row - j 
                if abs(diff) == 1:
                    print("CAN MOVE")
                    num = self.squares[i][j]["text"]
                    self.squares[i][j].grid_forget()
                    self.squares[i][j]["text"] = 0
                    self.squares[empty_col][empty_row].grid(column = i, row = j + diff + 1, sticky = "NEWS")
                    self.squares[empty_col][empty_row].config(text = num, command = self.Move(empty_col, empty_row))
                    self.empty_cell = (i, j)
            if j == empty_row:
                diff = empty_col - i
                if abs(diff) == 1:
                    print("CAN MOVE")
                    num = self.squares[i][j]["text"]
                    self.squares[i][j].grid_forget()
                    self.squares[i][j]["text"] = 0
                    self.squares[empty_col][empty_row].grid(column = i + diff, row = j + 1, sticky = "NEWS")
                    self.squares[empty_col][empty_row].config(text = num, command = self.Move(empty_col, empty_row))
                    self.empty_cell = (i, j)
            if self.GameOver():
                messagebox.showinfo(message = "Congratulations! You win!")
                self.NewGame()
        return process_shift

    def GameOver(self):
        nums = []
        for i in range(0, 4):
            for j in range(0, 4):
                nums.append(self.squares[j][i]["text"])
        print(nums)
        if nums == nums_ok:
            return True
        else:
            return False

        

app = Application()
app.title('Play 15')
app.geometry("480x360")
app.configure(background='orange')
app.mainloop()