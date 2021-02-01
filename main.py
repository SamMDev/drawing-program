import tkinter as tk
from GUI.canvas.canvas_frame import CanvasFrame
from GUI.controlPanel.control_panel_frame import ControlPanelFrame


class MainApp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # control panel
        self.controlPanelFrame = ControlPanelFrame(self)
        # canvas
        self.canvasFrame = CanvasFrame(self)

        self.pack()


root = tk.Tk()
MainApp(root)
root.mainloop()
