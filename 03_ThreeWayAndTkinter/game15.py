import tkinter as tk

class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.CreateWidgets()

    def CreateWidgets(self):
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(column = 3, row = 5, columnspan = 2)
    
    def NewGame(self):
        pass

app = Application()
app.title('Play 15')
app.geometry("480x360")
app.mainloop()