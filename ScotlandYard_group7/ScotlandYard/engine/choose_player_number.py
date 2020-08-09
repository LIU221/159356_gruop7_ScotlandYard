from tkinter import Tk, Label, Button, OptionMenu, IntVar

from ScotlandYard.engine.choose_role import RolePage


class PlayerNumberPage(Tk):
    def __init__(self, mode):
        Tk.__init__(self)

        self.mode = mode

        self.title('Choose player number')

        self.geometry('500x300')
        self.label_choose_your_game_role = Label(self, text="Choose player number:")

        self.label_choose_your_game_role.pack(fill='x')

        drop_down_options = {2, 3, 4, 5, 6}
        self.drop_down_selected = IntVar(self)
        self.drop_down_selected.set(2)
        self.drop_down_menu = OptionMenu(self, self.drop_down_selected, *drop_down_options)
        self.drop_down_menu.pack(fill='y')

        self.button_confirm = Button(self, text="Confirm", command=self.confirm)
        self.button_confirm.pack()

    def confirm(self):
        self.destroy()
        role_page = RolePage(self.mode, self.drop_down_selected.get())
        role_page.mainloop()
