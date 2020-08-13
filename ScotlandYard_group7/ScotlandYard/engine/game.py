import random
import copy
from tkinter import messagebox

import os

from ScotlandYard.engine.loadBoard import load_board
from ScotlandYard.engine.player import Player


class Game:
    def __init__(self, mr_x, detectives, player_number):
        self.detectives_ai = detectives
        self.mr_x_ai = mr_x
        self.boardmap = load_board()
        # self.x_history = []
        self.detectives = []
        self.x = None
        self.round = 1
        self.turn = 0
        self.reveal_rounds = [3, 8, 13, 18, 24]
        self.player_number = player_number

        startTickets = {"taxi": 10, "bus": 8, "underground": 4}

        startLocs = []
        baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fileName = baseDirectory + os.sep + "Files" + os.sep + "start_locations.txt"
        with open(fileName, "r") as f:
            for line in f:
                startLocs.append(int(line.strip()))
        random.shuffle(startLocs)

        self.x = Player({"taxi": 100, "bus": 100, "underground": 100, "black": 5, "2x": 2}, startLocs[0], "X")

        names = ["A", "B", "C", "D", "E"]

        for n in range(self.player_number - 1):
            self.detectives.append(Player(dict(startTickets), startLocs[n + 1], names[n]))

        self.players = [self.x] + self.detectives.copy()

    def next_turn(self, is_player_move=False, is_use_2x=False):
        turn = self.turn
        self.turn += 1

        if turn <= 0:
            # Mr. X's turn
            if is_player_move:
                move = is_player_move
            else:
                move = self.mr_x_ai.play_move(copy.deepcopy(self.x))

            if is_use_2x:
                self.x.tickets["2x"] -= 1
                if self.x.tickets["2x"] < 0:
                    messagebox.showinfo("Error",
                                        "Mr X: stop trying to be special - it isn't working.  attempted to use too many 2x tickets")
                else:
                    self.turn -= 1
                    self.perform_move(self.x, move)
                    # self.x_history.append((self.x.pos if self.round in self.reveal_rounds else None, move[1]))
            else:
                self.perform_move(self.x, move)
                # self.x_history.append((self.x.pos if self.round in self.reveal_rounds else None, move[1]))

            # print("X Ledger is updated to ", self.x_history)

        else:
            # Detective's turn
            detective = self.detectives[turn - 1]

            if self.cant_move(detective):
                print("Detective {} can't move!".format(detective.name))
            else:
                if is_player_move:
                    move = is_player_move
                else:
                    move = self.detectives_ai.play_move(copy.deepcopy(detective), copy.deepcopy(self.detectives))
                self.perform_move(detective, move)

        if self.is_game_over():
            messagebox.showinfo("Game Result", self.is_game_over())
            exit()

        if self.turn >= self.player_number:
            self.turn = 0
            self.round += 1

    def next_round(self):
        for i in range(6):
            self.next_turn()

    def perform_move(self, player, move):
        # check for legality of move
        if move[0] not in self.boardmap[player.pos][move[1]]:
            messagebox.showinfo("Error",
                                "{}: Move from {} to {} via {} ticket is illegal".format(player.name, player.pos,
                                                                                         move[0], move[1]))
        elif player is not self.x and any(move[0] == plr.pos for plr in self.detectives):
            messagebox.showinfo("Error",
                                "{}: This node ain't big enough for the both of us! node {} has two people".format(
                                    player.name, move[0]))
        else:
            player.pos = move[0]
            transport = move[1]
            player.tickets[transport] -= 1
            if player.tickets[transport] < 0:
                messagebox.showinfo("Error",
                                    "{} used a {} ticket they didn't have!".format(player.name, transport))

            print("{} moved to {} using {}".format(player.name, move[0], move[1]))

    def cant_move(self, player):
        for ticket in player.tickets.keys():
            if player.tickets[ticket] > 0 and ticket in self.boardmap[player.pos]:
                return False
        return True

    def is_game_over(self):
        detectives_win = any(self.x.pos == plr.pos for plr in self.detectives)
        x_wins = all(self.cant_move(plr) for plr in self.detectives)
        if detectives_win:
            return "The detectives win!"
        if x_wins:
            return "Mr X wins!"
        return False
