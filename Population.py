from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
from Chromosome import Chromosome


# This module is used to handle all the operations related to Population
class Population:
	# This initializes the population
	def __init__(self,popSize):
		self.chromosomes=[None]*popSize
		for i in range(popSize):
			self.chromosomes[i]=Chromosome()
	# This is used to initialize the initial population from the given image pixels(chromosomes)
	def initializePopulation(self,chromosomes):
		for i in range(len(chromosomes)):
			self.chromosomes[i]=chromosomes[i]
		# This is used to sort the population in the decreasing order of fitness
		self.chromosomes=sorted(self.chromosomes,key=lambda x: x.fitness)
	# This returns the size of the population
	def size(self):
		return len(self.chromosomes)
	# This is used to update the details of the chromosome
	def updateChromosome(self,c):
		for i in range(len(self.chromosomes)):
			if self.chromosomes[i].id==c.id:
				self.chromosomes[i]=c
	# This is used to get all the chromosomes(whole of the population)
	def getAllChromosome(self):
		return self.chromosomes
	# This is used to get the fittest chromosome in the population
	def getFittest(self):
		c=self.chromosomes[0]
		for i in range(len(self.chromosomes)):
			if self.chromosomes[i].getFitness()<c.getFitness():
				c=self.chromosomes[i]
		return c
	# This is used to get the top 3 fittest chromosomes back
	def getFittestChromoCount(self):
		self.chromosomes=sorted(self.chromosomes,key=lambda x: x.fitness)
		fittestChroms=[None]*3
		index=0
		for i in range(len(self.chromosomes)):
			if self.chromosomes[i].getSolutionId()==-1:
				fittestChroms[index]=self.chromosomes[i]
				index+=1
			if index==3:
				break
		return fittestChroms

