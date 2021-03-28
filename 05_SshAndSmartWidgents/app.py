import tkinter as tk
from tkinter.font import Font as tkFont

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.geometry("480x360")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''


class App(Application):
    def create_widgets(self):
        self.frame1 = tk.LabelFrame(self)
        self.frame1.grid(row=1, column=0, sticky="NEWS")
        self.drawing = tk.LabelFrame(self, text='Editor', font="fixed")
        self.drawing.grid(row = 0, column = 0, sticky="NEWS")
        self.drawing.columnconfigure(0, weight=1)
        self.drawing.columnconfigure(1, weight=1)
        self.drawing.rowconfigure(0, weight=1)

        self.quit_button = tk.Button(self.frame1, text="Quit", font="fixed",
                           command=self.master.quit)
        self.quit_button.grid(row = 0, column = 1, sticky = "E")
        self.load_button = tk.Button(self.frame1, text="Load changes", font="fixed",
                             command=self.upload)
        self.load_button.grid(row=0,column=0, sticky = "WE")

        self.txt = tk.Text(self.drawing, undo=True, wrap=tk.WORD, font="fixed", inactiveselectbackground="blue", takefocus=False, width=20)
        self.txt.grid(row=0, column=1, sticky = "NEWS")
        self.canv = tk.Canvas(self.drawing, bg='peach puff', width="5c")
        self.canv.grid(row=0, column=0, sticky = "NEWS")

    def upload():
        pass


app = App(title="Editor")
app.mainloop()