# AI for the detectives

from typing import List, Tuple
import random

from loadBoard import load_board
from player import Player


def play_move(detective: Player, detectives: List[Player]) -> Tuple[int, str]:
    # This line shows which tickets we have that can be used
    boardmap = load_board()
    transport = map(lambda x: x[0],
                    filter(lambda x: x[1] > 0 and x[0] in boardmap[detective.pos].keys(), detective.tickets.items()))
    #transport = ['taxi', 'bus', 'background', 'black']
    valid_nodes = []
    print(boardmap[detective.pos].keys())
    for t in transport:
        temp = boardmap[detective.pos].get(t, [])
        for neighbor in temp:
            if neighbor not in [d.pos for d in detectives]:
                valid_nodes.append((neighbor, t))
    # Return a tuple: int, string
    for item in valid_nodes:
        print(item)
    return random.choice(valid_nodes)

def play_move_ds(detective: Player, detectives: List[Player], mrx_location) -> Tuple[int, str]:
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
    for item in valid_nodes:
        print(item)
    return (deep_search(detective, detectives, mrx_location, []), 'Taxi')
    # return random.choice(valid_nodes)

def transport_valid_nodes(boardmap, pos, end_pos, counts, pos2 = []):
    counts = counts + 1
    transport = ['taxi', 'bus', 'background', 'black']
    valid_nodes = []
    for t in transport:
        temp = boardmap[pos].get(t, [])
        for neighbor in temp:
            if neighbor not in [d for d in pos2]:
                if (neighbor == end_pos or counts > 200):
                    return counts
                else:
                    transport_valid_nodes(boardmap, neighbor, end_pos, counts, pos2)
    # Return a tuple: int, string
    # for item_node in valid_nodes:
    #     transport_valid_nodes(boardmap, item_node[0], end_pos, counts, pos2)
    return counts

def deep_search(detective: Player, detectives: List[Player], end_pos, pos2 = []):
    max_count = -1
    way = 0
    boardmap = load_board()
    transport = ['taxi', 'bus', 'background', 'black']
    valid_nodes = []
    for t in transport:
        temp = boardmap[detective.pos].get(t, [])
        for neighbor in temp:
            if neighbor not in [d.pos for d in detectives]:
                valid_nodes.append((neighbor, t))
    for target_list in valid_nodes:
        counts = 0
        counts = transport_valid_nodes(boardmap, target_list[0],end_pos, counts, pos2)
        if (max_count > counts):
            max_count = counts
            way = target_list[0]
    return way
    
