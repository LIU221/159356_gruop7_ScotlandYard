from tkinter import Tk, Label, IntVar, Button, Radiobutton

from ScotlandYard_group7.ScotlandYard.engine import mrx, detectives
from ScotlandYard_group7.ScotlandYard.engine.game import Game
from ScotlandYard_group7.ScotlandYard.engine.gui import Window


class RolePage(Tk):
    def __init__(self, mode, player_number):
        Tk.__init__(self)

        self.mode = mode
        self.player_number = player_number

        self.title('Choose role')

        self.geometry('500x300')
        self.label_choose_your_game_role = Label(self, text="Choose your game role:")

        self.label_choose_your_game_role.pack(fill='x')

        roles = ['X', 'A', 'B', 'C', 'D', 'E']

        self.v = IntVar()
        for i in range(player_number):
            rb = self.rb1 = Radiobutton(self, text=roles[i], variable=self.v, value=i)
            rb.pack()

        self.button_confirm = Button(self, text="Confirm", command=self.confirm)
        self.button_confirm.pack()

    def confirm(self):
        self.destroy()
        the_game = Game(mrx, detectives, self.player_number)
        win = Window(the_game, self.mode, self.player_number, self.v.get())
        win.mainloop()
