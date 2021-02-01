import tkinter as tk
from injections.instances import *


class PenColorSelectionFrame(tk.Frame):
    def __init__(self, parent, columnPosition):

        self.parent = parent

        tk.Frame.__init__(self, parent)

        self.grid(row=0, column=columnPosition)
        self.createButtons()

    def createButtons(self):
        colors = colorsTextFileManager.getColorsAsArray()

        for r in range(int(len(colors) / 3)):
            for c in range(3):

                color = colors[c + (r * 3)]

                buttomToGrid = tk.Button(
                    master=self,
                    bg=color,
                    activebackground=color,
                    command=lambda color=color: self.setPenColor(color)
                )
                buttomToGrid.grid(row=r, column=c)

    def setPenColor(self, color):
        pen.color = color
        self.parent.activePropertiesFrame.updateProperties()
