from enum import Enum
import os
import pygame

class Size(Enum):
	NONE = 0
	SMALL = 1
	MED = 2
	LARGE = 3

	@classmethod
	def getDir(cls):
		"""Internally used function, returns path of image files"""
		thisdir = os.path.dirname(__file__)
		return os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(thisdir)))))

	@classmethod
	def getSmallImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\small.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getSmallSelectedImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\small_selected.png")
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
	def getLargeImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\large.png")
		return pygame.transform.scale(surf, (50, 50))

	@classmethod
	def getLargeSelectedImg(cls):
		surf = pygame.image.load(cls.getDir() + "\\large_selected.png")
		return pygame.transform.scale(surf, (50, 50))
