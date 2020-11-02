import json
from mesa.visualization.ModularVisualization import VisualizationElement
class TextDisplay(VisualizationElement):
    package_includes = []
    local_includes = ["Visualizatons_module\\TextDisplay_base.js"]

    def __init__(self):
        new_element = "new TextDisplay()"
        self.js_code = "elements.push(" + new_element + ");"