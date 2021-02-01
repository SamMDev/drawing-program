import tkinter as tk
from GUI.controlPanel.subframes.pen_color_selection_frame import PenColorSelectionFrame
from GUI.controlPanel.subframes.pen_size_selection_frame import PenSizeSelectionFrame
from GUI.controlPanel.subframes.canvas_color_selection_frame import CanvasColorSelectionFrame
from GUI.controlPanel.subframes.delete_canvas_frame import DeleteCanvasFrame
from GUI.controlPanel.subframes.pen_shape_selection_frame import PenShapeSelectionFrame
from GUI.controlPanel.subframes.active_properties_frame import ActivePropertiesFrame


class ControlPanelFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.penColorSelectionFrame = PenColorSelectionFrame(self, 0)
        self.penSizeSelectionFrame = PenSizeSelectionFrame(self, 1)
        self.canvasColorSelectionFrame = CanvasColorSelectionFrame(self, 2)
        self.deleteCanvasFrame = DeleteCanvasFrame(self, 3)
        self.penShapeSelectionFrame = PenShapeSelectionFrame(self, 4)
        self.activePropertiesFrame = ActivePropertiesFrame(self, 5)

        self.pack()