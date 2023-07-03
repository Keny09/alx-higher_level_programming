#!/usr/bin/python3
class Rectangle:
	def __init__(self, height=0, width=0):
		self.width=width
		self.height=height

	@property
	def width(self):
		 return self.__width
	
	@width.setter
	def width(self, value):
		 if value < 0:
		 	raise ValueError("width must be >= 0")
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		self.__weight = value

	@property
	def height(self):
		return self.__height
	
	@height.setter
	def height(self, value):
		if value < 0:
			raise ValueError("height must be >= 0")
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		self.__height = value
