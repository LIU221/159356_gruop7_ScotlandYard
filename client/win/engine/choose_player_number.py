import os
import tkinter as tk
from tkinter import Tk, Label, Button, OptionMenu, IntVar, YES, BOTH

from PIL import Image, ImageTk

from choose_role import RolePage


class PlayerNumberPage(Tk):
    def __init__(self, mode):
        Tk.__init__(self)

        self.mode = mode

        self.title('Scotland-Choose player number')

        self.geometry('700x500')

        baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fileName_image = baseDirectory + os.sep + "img" + os.sep + "London.jpg"
        self.img_pil = Image.open(fileName_image)
        self.img = ImageTk.PhotoImage(self.img_pil.resize((700, 500)))

        self.label = Label(self, compound=tk.CENTER, font='Georgia 30 bold', text="Choose the number of "
                                                                                  "players\n\n\n\n\n", fg='white')

        drop_down_options = [2, 3, 4, 5, 6]
        self.drop_down_selected = IntVar(self)
        self.drop_down_selected.set(2)
        self.drop_down_menu = OptionMenu(self.label, self.drop_down_selected, *drop_down_options)
        self.drop_down_menu.place(x=325, y=300, width=50, height=50)

        self.button_confirm = Button(self.label, font='Georgia 14', text="Confirm", cursor="hand2",
                                     command=self.confirm)
        self.button_confirm.place(x=275, y=350, width=150, height=50)

        self.button_confirm.bind("<Enter>", self.hover)
        self.button_confirm.bind("<Leave>", self.leave)

        self.label.configure(image=self.img)
        self.label.pack(expand=YES, fill=BOTH)

    def confirm(self):
        self.destroy()
        role_page = RolePage(self.mode, self.drop_down_selected.get())
        role_page.mainloop()

    def hover(self, event):
        self.button_confirm.configure(background="black", fg='white')

    def leave(self, event):
        self.button_confirm.configure(background="SystemButtonFace", fg='black')
