import os
import tkinter as tk
from tkinter import Tk, Label, Button, YES, BOTH

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

        self.img_pil = Image.open(baseDirectory + os.sep + "img" + os.sep + "London.jpg")
        self.img = ImageTk.PhotoImage(self.img_pil.resize((700, 500)))

        self.label = Label(self, compound=tk.CENTER, font='Georgia 30 bold', text="Choose your game role\n\n\n\n\n",
                           fg='white')

        self.button_Mrx = Button(self.label, cursor="hand2", command=self.role0)
        self.detectiveA = Button(self.label, cursor="hand2", command=self.role1)
        self.detectiveB = Button(self.label, cursor="hand2", command=self.role2)
        self.detectiveC = Button(self.label, cursor="hand2", command=self.role3)
        self.detectiveD = Button(self.label, cursor="hand2", command=self.role4)
        self.detectiveE = Button(self.label, cursor="hand2", command=self.role5)

        self.label0 = Label(self.label, font='Georgia 12 bold', text="Mrx", fg='white', background='black')
        self.label1 = Label(self.label, font='Georgia 12 bold', text="DetectiveA", fg='white', background='black')
        self.label2 = Label(self.label, font='Georgia 12 bold', text="DetectiveB", fg='white', background='black')
        self.label3 = Label(self.label, font='Georgia 12 bold', text="DetectiveC", fg='white', background='black')
        self.label4 = Label(self.label, font='Georgia 12 bold', text="DetectiveD", fg='white', background='black')
        self.label5 = Label(self.label, font='Georgia 12 bold', text="DetectiveE", fg='white', background='black')

        buttons = [self.button_Mrx, self.detectiveA, self.detectiveB, self.detectiveC, self.detectiveD, self.detectiveE]
        labels = [self.label0, self.label1, self.label2, self.label3, self.label4, self.label5]
        hovers = [self.hover0, self.hover1, self.hover2, self.hover3, self.hover4, self.hover5]
        leaves = [self.leave0, self.leave1, self.leave2, self.leave3, self.leave4, self.leave5]

        self.img0 = ImageTk.PhotoImage(
            Image.open(baseDirectory + os.sep + "img" + os.sep + "Mrx.jpg").resize((100, 250)))
        self.img1 = ImageTk.PhotoImage(
            Image.open(baseDirectory + os.sep + "img" + os.sep + "detective.jpg").resize((100, 250)))
        self.img2 = ImageTk.PhotoImage(
            Image.open(baseDirectory + os.sep + "img" + os.sep + "Mrx2.jpg").resize((100, 250)))
        self.img3 = ImageTk.PhotoImage(
            Image.open(baseDirectory + os.sep + "img" + os.sep + "detective2.jpg").resize((100, 250)))

        for i in range(player_number):
            if i == 0:
                buttons[i].configure(image=self.img0)
            else:
                buttons[i].configure(image=self.img1)
            buttons[i].bind("<Enter>", hovers[i])
            buttons[i].bind("<Leave>", leaves[i])
            buttons[i].place(x=(600 - player_number * 100) / 2 + 50 + 100 * i, y=200, width=100, height=250)
            labels[i].place(x=(600 - player_number * 100) / 2 + 50 + 100 * i, y=450, width=100, height=50)

        self.label.configure(image=self.img)
        self.label.pack(expand=YES, fill=BOTH)

    def role0(self):
        self.confirm(0)

    def role1(self):
        self.confirm(1)

    def role2(self):
        self.confirm(2)

    def role3(self):
        self.confirm(3)

    def role4(self):
        self.confirm(4)

    def role5(self):
        self.confirm(5)

    def confirm(self, role):
        self.destroy()
        the_game = Game(mrx, detectives, self.player_number)
        win = Window(the_game, self.mode, self.player_number, role)
        win.mainloop()

    def hover0(self, event):
        self.button_Mrx.configure(image=self.img2)

    def leave0(self, event):
        self.button_Mrx.configure(image=self.img0)

    def hover1(self, event):
        self.detectiveA.configure(image=self.img3)

    def leave1(self, event):
        self.detectiveA.configure(image=self.img1)

    def hover2(self, event):
        self.detectiveB.configure(image=self.img3)

    def leave2(self, event):
        self.detectiveB.configure(image=self.img1)

    def hover3(self, event):
        self.detectiveC.configure(image=self.img3)

    def leave3(self, event):
        self.detectiveC.configure(image=self.img1)

    def hover4(self, event):
        self.detectiveD.configure(image=self.img3)

    def leave4(self, event):
        self.detectiveD.configure(image=self.img1)

    def hover5(self, event):
        self.detectiveE.configure(image=self.img3)

    def leave5(self, event):
        self.detectiveE.configure(image=self.img1)
