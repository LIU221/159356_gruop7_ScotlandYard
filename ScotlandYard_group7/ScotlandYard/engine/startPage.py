import os
from tkinter import Tk, Label, Button, Canvas, Frame, BOTH, YES
import tkinter as tk
from PIL import Image, ImageTk

from ScotlandYard_group7.ScotlandYard.engine.choose_player_number import PlayerNumberPage


class StartPage(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('Scotland-StartPage')
        self.geometry('700x500')

        baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fileName_image = baseDirectory + os.sep + "img" + os.sep + "London.jpg"
        self.img_pil = Image.open(fileName_image)
        self.img = ImageTk.PhotoImage(self.img_pil.resize((700, 500)))

        self.label = Label(self, compound=tk.CENTER, font='Georgia 30 bold', text="Welcome to Scotland\n\n\n\n\n",
                           fg='white')

        self.button_vs_ai = Button(self.label, font='Georgia 14', text="VS AI", cursor="pirate", command=self.vs_ai)
        self.button_multiplayer = Button(self.label, font='Georgia 14', text="Multiplayer", cursor="spider",
                                         command=self.multiplayer)

        self.button_vs_ai.bind("<Enter>", self.hover1)
        self.button_vs_ai.bind("<Leave>", self.leave1)
        self.button_multiplayer.bind("<Enter>", self.hover2)
        self.button_multiplayer.bind("<Leave>", self.leave2)

        self.button_vs_ai.place(x=275, y=300, width=150, height=50)
        self.button_multiplayer.place(x=275, y=350, width=150, height=50)

        self.label.configure(image=self.img)
        self.label.pack(expand=YES, fill=BOTH)

    def vs_ai(self):
        self.destroy()
        palyer_number_page = PlayerNumberPage("ai")
        palyer_number_page.mainloop()

    def multiplayer(self):
        pass

    def hover1(self, event):
        self.button_vs_ai.configure(background="black", fg='white')

    def leave1(self, event):
        self.button_vs_ai.configure(background="SystemButtonFace", fg='black')

    def hover2(self, event):
        self.button_multiplayer.configure(background="black", fg='white')

    def leave2(self, event):
        self.button_multiplayer.configure(background="SystemButtonFace", fg='black')


if __name__ == '__main__':
    stPage = StartPage()
    stPage.mainloop()
