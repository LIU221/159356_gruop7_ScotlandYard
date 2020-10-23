import os


def load_board():
    boardmap = {}
    t = "taxi"
    b = "bus"
    u = "underground"
    baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fileName = baseDirectory + os.sep + "Files" + os.sep + "board_data.txt"
    with open(fileName, "r") as f:
        for line in f:
            data = [a.strip() for a in line.split("|")]
            entry = {}
            if len(data) > 1 and data[1] != '':
                entry[t] = [int(a.strip()) for a in data[1].split(" ")]
            if len(data) > 2 and data[2] != '':
                entry[b] = [int(a.strip()) for a in data[2].split(" ")]
            if len(data) > 3 and data[3] != '':
                entry[u] = [int(a.strip()) for a in data[3].split(" ")]

            blackTicket = []
            for key in entry.keys():
                blackTicket += entry[key]

            entry["black"] = blackTicket

            tList = '[]'
            bList = '[]'
            uList = '[]'
            if "taxi" in entry:
                tList = (str(entry["taxi"]))
            if "bus" in entry:
                bList = (str(entry["bus"]))
            if "underground" in entry:
                uList = (str(entry["underground"]))
            # print(str(entry["underground"])) print('{ ' +  '"id": '+  data[0] + ', "taxi" :' +tList + ',
            # "bus": ' +bList + ', "underground": ' + uList + '},')
            if len(data) > 4:
                entry["black"] += list(set([int(a.strip()) for a in data[4].split(' ')]))

            if len(data) > 0:
                boardmap[int(data[0])] = entry
               
    return boardmap
