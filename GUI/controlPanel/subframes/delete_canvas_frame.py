import tkinter as tk


class DeleteCanvasFrame(tk.Frame):

    def __init__(self, parent, columnLocation):
        self.parent = parent
        tk.Frame.__init__(self, parent)

        self.canvas_delete_button = tk.Button(
            master=self,
            text="VYMAZ\nPLATNO",
            width=20,
            command=self.cleanCanvas
        )
        self.canvas_delete_button.grid(row=0, column=0)

        self.rubber_button = tk.Button(
            master=self,
            text="Aktivuj gumu",
            width=20,
            command=self.rubber
        )
        self.rubber_button.grid(row=1, column=0)



        self.grid(row = 0, column = columnLocation, padx = 20)

    def cleanCanvas(self):
        self.parent.parent.canvasFrame.canvas.delete("all")

    def rubber(self):
        rubberColor = self.parent.parent.canvasFrame.canvas["bg"]
        self.parent.penColorSelectionFrame.setPenColor(rubberColor)