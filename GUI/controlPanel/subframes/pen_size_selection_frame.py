import tkinter as tk
from injections.instances import pen

class PenSizeSelectionFrame(tk.Frame):

    def __init__(self, parent, columnLocation):
        self.parent = parent
        tk.Frame.__init__(self, parent)


        self.size_info_label = tk.Label(
            master=self,
            text="Enter pen size"
        )
        self.size_info_label.grid(row=0, column=0)


        self.size_entry = tk.Entry(
            master=self
        )
        self.size_entry.grid(row=1, column=0)

        self.size_button = tk.Button(
            master=self,
            width=5,
            text="apply",
            command=lambda: self.setPenSize(self.size_entry.get())
        )
        self.size_button.grid(row=2, column=0)


        self.grid(row = 0, column = columnLocation, padx = 20)

    def setPenSize(self, size):
        try:
            size = float(size)
            pen.size = size
            self.parent.activePropertiesFrame.updateProperties()
        except ValueError:
            print("not number")