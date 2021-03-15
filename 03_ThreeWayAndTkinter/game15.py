import tkinter as tk

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
        self.newgame_button.grid(column = 0, row = 0, columnspan = 4, sticky = "WE")
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(column = 3, row = 5, columnspan = 2)

        self.squares = [[tk.Button(self) for j in range(4)] for i in range(4)]

    
    def NewGame(self):
        for i in range(0, 4):
            for j in range(0, 4):
                self.squares[i][j].config(text = "LOL")
                self.squares[i][j].grid(column = i, row = j + 1)

app = Application()
app.title('Play 15')
app.geometry("480x360")
app.mainloop()