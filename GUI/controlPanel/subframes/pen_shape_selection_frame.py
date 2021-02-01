import tkinter as tk
from injections.instances import pen


class PenShapeSelectionFrame(tk.Frame):

    def __init__(self, parent, columnLocation):
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.oval_pen_button = tk.Button(
            master=self,
            text="Kruh",
            command=lambda: self.setPenShape("oval")
        )
        self.oval_pen_button.grid(row=0, column=0)

        self.rect_pen_button = tk.Button(
            master=self,
            text="Stvorec",
            command=lambda: self.setPenShape("rectangle")
        )
        self.rect_pen_button.grid(row=1, column=0)

        self.cross_pen_button = tk.Button(
            master=self,
            text="Krizik",
            command=lambda: self.setPenShape("cross")
        )
        self.cross_pen_button.grid(row=2, column=0)

        self.grid(row = 0, column = columnLocation, padx = 20)

    def setPenShape(self, shape):
        pen.shape = shape
        self.parent.activePropertiesFrame.updateProperties()