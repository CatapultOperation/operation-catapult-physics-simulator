import pygame

import graphics.GraphicsMain as graphics


pygame.init()
screen = pygame.display.set_mode((400, 400))
objects = []

def update():
    graphics.render()
    events = pygame.event.get()
    graphics.events(screen, objects, events)