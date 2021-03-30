import tkinter as tk
from tkinter.font import Font as tkFont
import random as random

colors = ["dark orange", "DarkOliveGreen3", "SkyBlue2", "lemon chiffon", "MistyRose2", "gold", "khaki", "SlateGray3"]

def rand_col():
    r = random.randint(0, len(colors) - 1)
    return colors[r]

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ovals = []
        self.oval = None
        self.color = "white"

    def create_widgets(self):
        self.frame1 = tk.LabelFrame(self)
        self.frame1.grid(row=1, column=0, sticky="NEWS")
        self.draw_window = tk.LabelFrame(self, text='Editor', font="fixed")
        self.draw_window.grid(row = 0, column = 0, sticky="NEWS")
        self.draw_window.columnconfigure(0, weight=1)
        self.draw_window.columnconfigure(1, weight=1)
        self.draw_window.rowconfigure(0, weight=1)

        self.quit_button = tk.Button(self.frame1, text="Quit", font="fixed", command=self.master.quit)
        self.quit_button.grid(row = 0, column = 1, sticky = "WE")
        self.load_button = tk.Button(self.frame1, text="Load changes", font="fixed", command=self.upload)
        self.load_button.grid(row=0,column=0, sticky = "WE")

        self.txt = tk.Text(self.draw_window, undo=True, wrap=tk.WORD, font="fixed", inactiveselectbackground="blue", takefocus=False, width=20)
        self.txt.grid(row=0, column=1, sticky = "NEWS")
        self.canv = tk.Canvas(self.draw_window, bg='peach puff', width="5c")

        self.canv.bind("<Button-1>", self.button_press)
        self.canv.bind("<B1-Motion>", self.mouse_move)
        # self.canv.bind("<Motion", self.mouse_move)
        self.canv.bind("<ButtonRelease-1>", self.button_release)

        self.canv.grid(row=0, column=0, sticky = "NEWS")

    def upload():
        pass
    
    def button_press(self, event):
        # print("Button pressed")
        self.coords = (event.x, event.y)
        self.ovals.append(self.coords)
        self.color = rand_col()

    def mouse_move(self, event):
        # print(("moving"))
        if self.oval:
            self.canv.delete(self.oval)
        self.oval = self.canv.create_oval(*self.coords, event.x, event.y, tags="obj", fill=self.color, outline = "black", width=1)

    def button_release(self, event):
        self.coords = (None, None)
        self.oval = None




app = App(title="Editor")
app.mainloop()