import os
from tkinter import Tk, Label, IntVar, Button, Radiobutton, YES, BOTH

import tkinter as tk
from PIL import Image, ImageTk

from ScotlandYard_group7.ScotlandYard.engine import mrx, detectives
from ScotlandYard_group7.ScotlandYard.engine.game import Game
from ScotlandYard_group7.ScotlandYard.engine.gui import Window


class RolePage(Tk):
    def __init__(self, mode, player_number):
        Tk.__init__(self)

        self.mode = mode
        self.player_number = player_number

        self.title('Scotland-Choose role')

        self.geometry('700x500')

        baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fileName_image = baseDirectory + os.sep + "img" + os.sep + "London.jpg"
        self.img_pil = Image.open(fileName_image)
        self.img = ImageTk.PhotoImage(self.img_pil.resize((700, 500)))

        self.label = Label(self, compound=tk.CENTER, font='Georgia 30 bold', text="Choose your game role\n\n\n\n\n",
                           fg='white')

        roles = ['MrX', 'Detective A', 'Detective B', 'Detective C', 'Detective D', 'Detective E']

        self.v = IntVar()
        for i in range(player_number):
            rb = self.rb1 = Radiobutton(self.label, text=roles[i], variable=self.v, value=i)
            rb.place(x=300, y=200+25*i, width=100)

        self.button_confirm = Button(self.label, font='Georgia 14', text="Confirm", cursor="hand2",
                                     command=self.confirm)
        self.button_confirm.place(x=275, y=370, width=150, height=50)

        self.button_confirm.bind("<Enter>", self.hover)
        self.button_confirm.bind("<Leave>", self.leave)

        self.label.configure(image=self.img)
        self.label.pack(expand=YES, fill=BOTH)

    def confirm(self):
        self.destroy()
        the_game = Game(mrx, detectives, self.player_number)
        win = Window(the_game, self.mode, self.player_number, self.v.get())
        win.mainloop()

    def hover(self, event):
        self.button_confirm.configure(background="black", fg='white')

    def leave(self, event):
        self.button_confirm.configure(background="SystemButtonFace", fg='black')
