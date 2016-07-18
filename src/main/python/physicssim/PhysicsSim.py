import pygame

<<<<<<< HEAD
import src.main.python.physicssim.graphics.GraphicsMain as graphics
=======
import graphics.GraphicsMain as graphics
>>>>>>> 466e371c83dfa0ba164515d6446e7e569266457b


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
objects = []

def update():
<<<<<<< HEAD
	events = pygame.event.get()

	graphics.events(screen, objects, events)

def mainLoop():
	while True:
		update()
		clock.tick(30)
=======
    graphics.render()
    events = pygame.event.get()
    graphics.events(screen, objects, events)
>>>>>>> 466e371c83dfa0ba164515d6446e7e569266457b
