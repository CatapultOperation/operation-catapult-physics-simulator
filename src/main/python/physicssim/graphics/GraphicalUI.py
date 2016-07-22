import enum

import pygame

from main.python.physicssim.graphics.GraphicalButton import GraphicalButton


class Strength(enum):
    NONE = 0
    LOW = 1
    MED = 2
    HIGH = 3
    
class Size(enum):
    NONE = 0
    SMALL = 1
    MED = 2
    LARGE = 3

class GraphicalUI: 
    
    
    
    def __init__(self):
        self.strength = Strength.NONE
        self.size = Size.NONE
        self.sizeButtonRectList = []
        self.strengthButtonList = []
        
        self.sizeButtonRectList.append(GraphicalButton(pygame.Rect((10, 100), (50, 50)), Size.SMALL))
        self.sizeButtonRectList.append(GraphicalButton(pygame.Rect((60, 100), (50, 50)), Size.MED))
        self.sizeButtonRectList.append(GraphicalButton(pygame.Rect((110, 100), (50, 50)), Size.LARGE))
        
        self.strengthButtonList.append(GraphicalButton(pygame.Rect((10, 150), (50, 50)), Strength.LOW))
        self.strengthButtonList.append(GraphicalButton(pygame.Rect((60, 150), (50, 50)), Strength.MED))
        self.strengthButtonList.append(GraphicalButton(pygame.Rect((110, 150), (50, 50)), Strength.HIGH))
    
    def draw(self, screen):
        UI = pygame.Surface((300, 300))
        for sizeButtonRect in self.sizeButtonRectList: 
            pygame.draw.rect(UI, (0, 0, 0), sizeButtonRect)
        for strengthButtonRect in self.strengthButtonRectList: 
            pygame.draw.rect(UI, (0, 0, 0), strengthButtonRect)
        
        if(self.size == Size.NONE):
            UI.blit(Size.getSmallImg(), (10, 100))
            UI.blit(Size.getMedImg(), (60, 100))
            UI.blit(Size.getLargeImg(), (110, 100))
        elif(self.size == Size.SMALL): 
            UI.blit(Size.getSmallSelectedImg(), (10, 100))
            UI.blit(Size.getMedImg(), (60, 100))
            UI.blit(Size.getLargeImg(), (110, 100))
        elif(self.size == Size.MED): 
            UI.blit(Size.getSmallImg(), (10, 100))
            UI.blit(Size.getMedSelectedImg(), (60, 100))
            UI.blit(Size.getLargeImg(), (110, 100))
        elif(self.size == Size.LARGE): 
            UI.blit(Size.getSmallImg(), (10, 100))
            UI.blit(Size.getMedImg(), (60, 100))
            UI.blit(Size.getLargeSelectedImg(), (110, 100))
        
        if(self.strength == Strength.NONE):
            UI.blit(Strength.getLowImg(), (10, 150))
            UI.blit(Strength.getMedImg(), (60, 150))
            UI.blit(Strength.getHighImg(), (110, 150))
        elif(self.strength == Strength.LOW):
            UI.blit(Strength.getLowSelectedImg(), (10, 150))
            UI.blit(Strength.getMedImg(), (60, 150))
            UI.blit(Strength.getHighImg(), (110, 150))
        elif(self.strength == Strength.MED):
            UI.blit(Strength.getLowImg(), (10, 150))
            UI.blit(Strength.getMedSelectedImg(), (60, 150))
            UI.blit(Strength.getHighImg(), (110, 150))
        elif(self.strength == Strength.HIGH):
            UI.blit(Strength.getLowdImg(), (10, 150))
            UI.blit(Strength.getMedImg(), (60, 150))
            UI.blit(Strength.getHighSelecteImg(), (110, 150))
    
    def mouseCollision(self, event):
        for sizeButtonRect in self.seizeButtonRectList: 
            if (sizeButtonRect.rect.collidepoint(event.pos)):
                self.setSize(sizeButtonRect.size)
        for strengthButtonRect in self.strengthButtonRectList: 
            if (strengthButtonRect.rect.collidepoint(event.pos)):
                self.setStrength(strengthButtonRect.strength)
    
    def setStrength(self, strength):
        self.strength = strength
    
    def setSize(self, size):
        self.size = size
    