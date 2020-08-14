# AI for Mr. X

from typing import List, Tuple
import random

from ScotlandYard_group7.ScotlandYard.engine.loadBoard import load_board
from ScotlandYard_group7.ScotlandYard.engine.player import Player


def play_move(mr_x: Player) -> Tuple[int, str]:
    # Haven't been finished, only returns taxi moves in this example
    boardmap = load_board()
    return random.choice(boardmap[mr_x.pos]["taxi"]), "taxi"
