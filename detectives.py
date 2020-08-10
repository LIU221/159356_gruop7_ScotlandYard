# AI for the detectives

from typing import List, Tuple
import random

from ScotlandYard.engine.loadBoard import load_board
from ScotlandYard.engine.player import Player


def play_move(detective: Player, detectives: List[Player]) -> Tuple[int, str]:
    # This line shows which tickets we have that can be used
    boardmap = load_board()
    transport = map(lambda x: x[0],
                    filter(lambda x: x[1] > 0 and x[0] in boardmap[detective.pos].keys(), detective.tickets.items()))
    valid_nodes = []
    for t in transport:
        for neighbor in boardmap[detective.pos][t]:
            if neighbor not in [d.pos for d in detectives]:
                valid_nodes.append((neighbor, t))
    # Return a tuple: int, string
    return random.choice(valid_nodes)
