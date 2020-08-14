from tkinter import Tk, Canvas
from PIL import ImageTk, Image
import os

root = Tk()
cnv = Canvas(root, width=2000, height=2000)
baseDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fileName = baseDirectory + os.sep + "Files" + os.sep + "board.jpg"
img = Image.open(fileName)
img = img.resize((2000, 2000))
img = ImageTk.PhotoImage(image=img)
cnv.create_image(1000, 1000, image=img)
n = 1


def callback(evt):
    global n
    print(n, evt.x, evt.y)
    n += 1


cnv.bind("<Button-1>", callback)

cnv.pack()

