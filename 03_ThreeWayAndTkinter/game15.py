import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.CreateWidgets()

    def CreateWidgets(self):
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()

app = Application()
app.master.title('15 game')
app.mainloop()