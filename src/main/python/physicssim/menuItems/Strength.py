from enum import Enum
import os
import pygame

class Strength(Enum):
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
		return pygame.image.load(cls.getDIr() + "\\low.png")

	@classmethod
	def getLowSelectedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\low_selected.png")

	@classmethod
	def getMedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\med.png")

	@classmethod
	def getMedSelectedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\med_selected.png")

	@classmethod
	def getHighImg(cls):
		return pygame.image.load(cls.getDIr() + "\\high.png")

	@classmethod
	def getHighSelectedImg(cls):
		return pygame.image.load(cls.getDIr() + "\\high_selected.png")
