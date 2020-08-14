import os
from tkinter import Tk, Canvas, Label, Button, Frame, Entry, StringVar, OptionMenu, messagebox

from PIL import ImageTk, Image

from ScotlandYard_group7.ScotlandYard.engine.game import Game

UNSCALED_RECT_SIZE = 0.008


class Window(Tk):
    def __init__(self, game: Game, mode, player_number, role):

        Tk.__init__(self)

        # setup variables
        self.game = game

        self.mode = mode

        self.player_number = player_number
        self.role = role
        self.roles = ["X", "A", "B", "C", "D", "E"]

        self.is_use_2x = False

        self.reveal_rounds = [3, 8, 13, 18, 24]

        self.geometry('500x300')

        # create widgets
        self.board_canvas = Canvas(self, background="white")
        self.control_frame = Frame(self)
        self.label_current_round = Label(self.control_frame, text="Current Round: 1")
        self.label_current_player = Label(self.control_frame, text="Current Player: X")
        self.label_mrx_ticket = Label(self.control_frame, text="Ticket Mrx used: None")
        self.button_next_turn = Button(self.control_frame, text="Next Turn", command=self.next_turn)
        self.text_user_input = Entry(self.control_frame, text="move")

        self.button_2x = Button(self.control_frame, text="Use 2x ticket", command=self.use_2x_ticket)

        drop_down_options = {"taxi", "bus", "underground", "black"}
        self.drop_down_selected = StringVar(self.control_frame)
        self.drop_down_selected.set("taxi")
        self.drop_down_menu = OptionMenu(self.control_frame, self.drop_down_selected, *drop_down_options)
        self.button_send_action = Button(self.control_frame, text="Move", command=self.move)

        # layout widgets
        self.board_canvas.pack(fill='both', expand=True, anchor='w')
        self.control_frame.pack(before=self.board_canvas, side='right', anchor='e')
        self.label_current_round.pack(fill='x')
        self.label_current_player.pack(fill='x')
        self.label_mrx_ticket.pack(fill='x')
        self.button_next_turn.pack(fill='x')
        Label(self.control_frame, text="\n\n\n").pack(fill='x')
        self.button_2x.pack(fill='x')
        self.text_user_input.pack(fill='y')
        self.drop_down_menu.pack(fill='y')
        self.button_send_action.pack(fill='y')

        # setup canvas
        baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fileName_imageboard = baseDirectory + os.sep + "Files" + os.sep + "board.jpg"
        self.board_img_pil = Image.open(fileName_imageboard)
        self.board_img = ImageTk.PhotoImage(self.board_img_pil)
        self.img_id = self.board_canvas.create_image(300, 300, image=self.board_img)

        # move images
        self.bind("<Configure>", self.update_ui)
        self.player_colors = ["black", "red", "yellow", "green", "blue", "purple"]
        self.old_canvas_size = self.winfo_width(), self.winfo_height()
        self.player_rects = [self.board_canvas.create_rectangle(0, 0, 1, 1, fill=self.player_colors[i]) for i in
                             range(len(self.game.players))]
        self.player_txts = [self.board_canvas.create_text(0, 0, text=plr.name) for plr in self.game.players]

        # create data for node locations on image
        self.node_locations = {}
        fileName_nodeLocation = baseDirectory + os.sep + "Files" + os.sep + "node_locations.txt"
        with open(fileName_nodeLocation, "r") as f:
            for line in f:
                l = line.split(" ")
                self.node_locations[int(l[0])] = (float(l[1]), float(l[2]))

    def next_turn(self, *_):
        print(self.game.turn)
        try:
            # checks if move should be AI made or player made
            if self.game.players[self.game.turn].name != self.roles[self.role]:
                self.game.next_turn()
                self.label_current_round.configure(
                    text="Current Round: {}".format(self.game.round))
                self.label_current_player.configure(
                    text="Current Player: {}".format(self.game.players[self.game.turn].name))
                self.label_mrx_ticket.configure(
                    text="Ticket Mrx used: {}".format(self.game.mrx_ticket))
            else:
                messagebox.showinfo("Error",
                                    "It's your turn.")
        except:
            w, h = self.board_canvas.winfo_width(), self.board_canvas.winfo_height()
            self.board_canvas.create_rectangle(w / 4, h / 4, w * 3 / 4, h * 3 / 4, fill="red")
            self.board_canvas.create_text(w / 2, h / 2, text="EXCEPTION OCCURED; CHECK LOG", font="Helvetica 36")
            raise
        self.update_ui()

    def update_ui(self, *_):
        width = self.board_canvas.winfo_width()
        height = self.board_canvas.winfo_height()
        if self.old_canvas_size != (width, height):  # don't update the image unless we *have* to
            self.old_canvas_size = (width, height)

            tmp_pil = self.board_img_pil.resize((width, height))
            self.board_canvas.delete(self.img_id)
            self.board_img = ImageTk.PhotoImage(tmp_pil)
            self.img_id = self.board_canvas.create_image(int(width / 2), int(height / 2), image=self.board_img)
        if self.role > 0 and self.game.round in self.reveal_rounds or self.role == 0:
            for i, player in enumerate(self.game.players):
                x, y = self.node_locations[player.pos]
                x *= width
                y *= height
                self.board_canvas.coords(self.player_rects[i], x + width * UNSCALED_RECT_SIZE,
                                         y + width * UNSCALED_RECT_SIZE, x - width * UNSCALED_RECT_SIZE,
                                         y - width * UNSCALED_RECT_SIZE)
                self.board_canvas.coords(self.player_txts[i], x, y)
                self.board_canvas.lift(self.player_rects[i])
                self.board_canvas.lift(self.player_txts[i])
        else:
            tmp_pil = self.board_img_pil.resize((width, height))
            self.board_canvas.delete(self.img_id)
            self.board_img = ImageTk.PhotoImage(tmp_pil)
            self.img_id = self.board_canvas.create_image(int(width / 2), int(height / 2), image=self.board_img)
            for i, player in enumerate(self.game.players):
                if player.name == "X":
                    pass
                else:
                    x, y = self.node_locations[player.pos]
                    x *= width
                    y *= height
                    self.board_canvas.coords(self.player_rects[i], x + width * UNSCALED_RECT_SIZE,
                                             y + width * UNSCALED_RECT_SIZE, x - width * UNSCALED_RECT_SIZE,
                                             y - width * UNSCALED_RECT_SIZE)
                    self.board_canvas.coords(self.player_txts[i], x, y)
                    self.board_canvas.lift(self.player_rects[i])
                    self.board_canvas.lift(self.player_txts[i])

    # sends user inputted move
    def move(self, *_):
        if self.game.players[self.game.turn].name == self.roles[self.role]:
            if self.text_user_input.get():
                move = (int(self.text_user_input.get()), self.drop_down_selected.get())  # should be changed
                if self.role > 0 and self.drop_down_selected.get() == "black":
                    messagebox.showinfo("Error",
                                        "Detectives can't use black ticket")
                elif self.is_use_2x:
                    if not self.game.next_turn(move, self.is_use_2x):
                        self.is_use_2x = True
                    else:
                        self.is_use_2x = False
                        self.update_ui()
                        self.label_current_player.configure(
                            text="Current Player: {}".format(self.game.players[self.game.turn].name))
                        self.label_mrx_ticket.configure(
                            text="Ticket Mrx used: {}".format(self.game.mrx_ticket))
                else:
                    self.game.next_turn(move, self.is_use_2x)
                    self.update_ui()
                    self.label_current_player.configure(
                        text="Current Player: {}".format(self.game.players[self.game.turn].name))
                    self.label_mrx_ticket.configure(
                        text="Ticket Mrx used: {}".format(self.game.mrx_ticket))
            else:
                messagebox.showinfo("Error",
                                    "Please enter a location")
        else:
            messagebox.showinfo("Error",
                                "You can't control this role")

    def use_2x_ticket(self):
        if self.role != 0:
            messagebox.showinfo("Error",
                                "Detectives can't use 2x ticket")
        else:
            self.is_use_2x = True
