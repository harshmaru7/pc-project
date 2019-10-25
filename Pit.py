# This module is used to handle Pixel Index Table related operations
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Chromosome import Chromosome
from Population import Population
from Fitness import Fitness
from GA import GA

class Pit:
	def __init__(self,x=-1,y=-1,deltaColorValues=[-1000,-1000,-1000]):
		self.x=x
		self.y=y

		self.deltaColorValues=deltaColorValues[:]

	def getX(self):
		return self.x

	def getY(self):
		return self.y 	

	def getDeltas(self):
		return self.deltaColorValues

	# Below two functions are mainly used in the extraction phase	
	# This returns the value that has to be added to the present pixel to get the ascii of the character back
	def getDecodeValue(self):
		value=-1000
		for i in range(len(self.deltaColorValues)):
			if self.deltaColorValues[i]!=-1000:
				value=self.deltaColorValues[i]
		return value
	# This is used to return which one r,g,b of a pixel is used to hide the cipher character
	def getDecodedValueIndex(self):
		index=-1
		for i in range(len(self.deltaColorValues)):
			if self.deltaColorValues[i]!=-1000:
				index=i
		return index
	# This is used to return a string containing all the details of a PIT entry
	def toString(self):
		#print("delta",self.deltaColorValues)
		return str(self.x)+","+str(self.y)+","+str(self.deltaColorValues[0])+","+str(self.deltaColorValues[1])+","+str(self.deltaColorValues[2])
