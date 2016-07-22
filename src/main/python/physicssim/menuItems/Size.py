from enum import Enum
import os
import pygame

class Size(Enum):
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
		return pygame.image.load(cls.getDIr() + "\\small.png")

	@classmethod
	def getSmallSelectedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\small_selected.png")

	@classmethod
	def getMedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\med.png")

	@classmethod
	def getMedSelectedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\med_selected.png")

	@classmethod
	def getLargeImg(cls):
		return pygame.image.load(cls.getDIr() + "\\large.png")

	@classmethod
	def getLargeSelectedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\large_selected.png")
