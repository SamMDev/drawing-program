import tkinter as tk
from injections.instances import pen

class ActivePropertiesFrame(tk.Frame):

    def __init__(self, parent, columnLocation):
        self.parent = parent

        tk.Frame.__init__(self, parent)

        self.active_color_lable = tk.Label(
            master=self,
            text="Aktivna farba"
        )
        self.active_color_lable.grid(row=0, column=0)
        self.active_pen_color_button = tk.Button(
            master=self,
            bg=pen.color,
            activebackground=pen.color
        )
        self.active_pen_color_button.grid(row=0, column=1)

        self.active_pen_size_label_info = tk.Label(
            text="Aktivna velkost kreslenia: ",
            master=self
        )
        self.active_pen_size_label_info.grid(row=1, column=0)
        self.active_pen_size_label = tk.Label(
            text=pen.size,
            master=self
        )
        self.active_pen_size_label.grid(row=1, column=1)


        self.grid(row = 0, column = columnLocation, padx = 20)

    def updateProperties(self):
        self.active_pen_color_button["bg"] = pen.color
        self.active_pen_size_label["text"] = pen.size