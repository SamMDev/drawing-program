import tkinter as tk
from injections.instances import colorsTextFileManager

class CanvasColorSelectionFrame(tk.Frame):

    def __init__(self, parent, columnLocation):
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.createButtons()

        self.grid(row = 0, column = columnLocation, padx = 20)

    def createButtons(self):
        colors = colorsTextFileManager.getColorsAsArray()
        for r in range(int(len(colors) / 3)):
            for c in range(3):
                color = colors[c + (r * 3)]
                buttomToGrid = tk.Button(
                    master=self,
                    bg=color,
                    activebackground=color,
                    command=lambda color=color: self.setCanvasColor(color)
                )
                buttomToGrid.grid(row=r, column=c)

    def setCanvasColor(self, color):
        self.parent.parent.canvasFrame.canvas["bg"] = color
