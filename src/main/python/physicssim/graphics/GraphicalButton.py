from main.python.physicssim.graphics.GraphicalUI import Size, Strength


class GraphicalButton():

    
    def __init__(self, rect, size=Size.NONE, strength=Strength.NONE):
        self.rect = rect
        self.size = size
        self.strength = strength
        
    