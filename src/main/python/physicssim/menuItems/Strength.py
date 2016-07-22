from enum import Enum
import os
import pygame

class Strength(Enum):
	NONE = 0
	LOW = 1
	MED = 2
	HIGH = 3

	@classmethod
	def getDir(cls):
		"""Internally used function, returns path of image files"""
		thisdir = os.path.dirname(__file__)
		return os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(thisdir)))))

	@classmethod
	def getLowImg(cls):
		surf =  pygame.image.load(cls.getDir() + "\\low.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getLowSelectedImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\low_selected.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getMedImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\med.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getMedSelectedImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\med_selected.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getHighImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\high.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getHighSelectedImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\high_selected.png")
		return pygame.transform.scale(surf, (50, 50))
