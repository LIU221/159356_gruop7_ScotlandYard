from tkinter import Tk, Label, Button

from ScotlandYard_group7.ScotlandYard.engine.choose_player_number import PlayerNumberPage


class StartPage(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('Start Page')

        self.geometry('500x300')
        self.label_choose_game_mode = Label(self, text="Choose Game Mode")
        self.button_vs_ai = Button(self, text="VS AI", command=self.vs_ai)
        self.button_multiplayer = Button(self, text="Multiplayer", command=self.multiplayer)

        self.label_choose_game_mode.pack(fill='x')
        self.button_vs_ai.pack(fill='x')
        self.button_multiplayer.pack(fill='x')

    def vs_ai(self):
        self.destroy()
        palyer_number_page = PlayerNumberPage("ai")
        palyer_number_page.mainloop()

    def multiplayer(self):
        pass


if __name__ == '__main__':
    stPage = StartPage()
    stPage.mainloop()
