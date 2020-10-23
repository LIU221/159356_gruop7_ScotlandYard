import unittest
import random
import sys, os
sys.path.append("..")
sys.path.extend([os.path.join(root, name) for root, dirs, _ in os.walk("../") for name in dirs])
from win import mrx, detectives
from win.game import Game
from win.loadBoard import load_board
from win.player import Player


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.boardmap = load_board()

    # AI/player, which role, if use '2x' ticket(Mrx)
    # Player, mrx, use '2x' ticket
    def test_next_turn_player1(self):
        game = Game(mrx, detectives, 6)
        pos1 = random.choice(self.boardmap[game.x.pos]["taxi"])
        game.next_turn((pos1, "taxi"), True)
        pos2 = random.choice(self.boardmap[pos1]["taxi"])
        game.next_turn((pos2, "taxi"))
        self.assertEqual(game.x.pos, pos2)

    # Player, mrx, don't use '2x' ticket
    def test_next_turn_player2(self):
        game = Game(mrx, detectives, 6)
        pos = random.choice(self.boardmap[game.x.pos]["taxi"])
        game.next_turn((pos, "taxi"))
        self.assertEqual(game.x.pos, pos)

    # Player, detective
    def test_next_turn_player3(self):
        game = Game(mrx, detectives, 6)
        game.next_turn()
        pos = random.choice(self.boardmap[game.detectives[0].pos]["taxi"])
        game.next_turn((pos, "taxi"))
        self.assertEqual(game.detectives[0].pos, pos)

    def test_cant_move1(self):
        game = Game(mrx, detectives, 6)
        game.x = Player({"taxi": 100, "bus": 100, "underground": 100, "black": 5, "2x": 2}, 155, "X")
        self.assertFalse(game.cant_move(game.x))

    def test_cant_move2(self):
        game = Game(mrx, detectives, 6)
        game.x = Player({"taxi": 0, "bus": 0, "underground": 0, "black": 0, "2x": 0}, 155, "X")
        self.assertTrue(game.cant_move(game.x))

    def test_cant_move3(self):
        game = Game(mrx, detectives, 6)
        game.x = Player({"taxi": 0, "bus": 0, "underground": 0, "black": 0, "2x": 2}, 155, "X")
        self.assertTrue(game.cant_move(game.x))

    def test_is_game_over1(self):
        game = Game(mrx, detectives, 6)
        game.next_turn()
        p = [100, 101, 102, 103, 104]
        for detective in game.detectives:
            detective.pos = p[game.detectives.index(detective)]
        game.x.pos = 155
        game.detectives[0].pos = 155
        self.assertTrue(game.is_game_over())

    def test_is_game_over2(self):
        game = Game(mrx, detectives, 6)
        game.next_turn()
        for detective in game.detectives:
            detective.tickets = {"taxi": 0, "bus": 0, "underground": 0}
        self.assertTrue(game.is_game_over())

    def test_is_game_over3(self):
        game = Game(mrx, detectives, 6)
        game.next_turn()
        for detective in game.detectives:
            detective.tickets = {"taxi": 1, "bus": 0, "underground": 0}
        self.assertFalse(game.is_game_over())
