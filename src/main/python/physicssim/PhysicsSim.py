import pygame

import graphics.graphicsMain as graphics


pygame.init()
screen = pygame.display.set_mode((400, 400))
objects = []

def update():
    events = pygame.event.get()
    
    graphics.events(screen, objects, events)