import tkinter as tk
from injections.instances import *


class CanvasFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.canvas = tk.Canvas(self, width = 950, height = 800, bg = "white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.pack()


    def draw(self, event):
        x, y = event.x, event.y
        if pen.shape == "oval":
            self.canvas.create_oval(x - pen.size, y - pen.size,
                                    x + pen.size, y + pen.size,
                                    fill=pen.color,
                                    outline="")
        elif pen.shape == "rectangle":
            self.canvas.create_rectangle(x - pen.size, y - pen.size,
                                         x + pen.size, y + pen.size,
                                         fill=pen.color,
                                         outline="")
        elif pen.shape == "cross":
            self.canvas.create_line(x - pen.size, y - pen.size, x + pen.size, y + pen.size, fill=pen.color)
            self.canvas.create_line(x - pen.size, y + pen.size, x + pen.size, y - pen.size, fill=pen.color)

