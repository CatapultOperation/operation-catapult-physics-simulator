from main.python.physicssim.menuItems.Size import Size
from main.python.physicssim.menuItems.Strength import Strength



class GraphicalButton:

    
    def __init__(self, rect, size=Size.NONE, strength=Strength.NONE):
        self.rect = rect
        self.size = size
        self.strength = strength
        
    