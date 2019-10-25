# This is the module where the genetic operation happen
from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
import random
from Chromosome import Chromosome
from Population import Population
from Fitness import Fitness

class GA:
	def __init__(self,arr_solution,populationSize):
		self.crossoverRate=0.5
		self.mutationRate=0.05
		self.MAX_GENERATIONS = 3
		self.m_fitness = Fitness(arr_solution)
		self.m_population = Population(populationSize)
		self.Solution_Index = 0
	# Here we find the fitness of each chromosome of a char of cipher and save it in the population
	def initializePopulation(self, population):
		fitPopulation = self.m_fitness.calculateFitness(population)
		self.m_population.initializePopulation(fitPopulation)
	def evolvePopulation(self):
		
		child = None
		for i in range(self.MAX_GENERATIONS):
			# Extracting two parents from the population
			parent1 = self.rankSelection(self.m_population)
			parent2 = self.rankSelection(self.m_population)
			child = self.crossover(parent1, parent2)
			self.m_population.updateChromosome(child)
			# If we were not able to find the exact solution and have reached the max limit of generations
			if(child.getSolutionId() == -1 and i==(self.MAX_GENERATIONS -1 )):
				child.setSolutionId(self.Solution_Index)
				self.m_population.updateChromosome(child)
				break
			# If we found exact solution
			elif child.getSolutionId() != -1 :
				break
			# This is for the mutation part of the algorithm(as we want some new features to get added to the population)
			fittestChromosomes =  self.m_population.getFittestChromoCount()
			for j in range(len(fittestChromosomes)): #Check
				self.m_population.updateChromosome(self.mutate(fittestChromosomes[j]))
		# This is to go to the next cipher character
		self.m_fitness.incrementSolutionIndex();
		self.Solution_Index+=1
		
		return self.m_population

	# This is where the child chromosome is produced
	def crossover(self,parent1,parent2):
		child = Chromosome();
		if (parent1.getFitness()<parent2.getFitness()):
			child = parent1
		else:
			child = parent2

		solution = self.m_fitness.getSolution()
		r = child.getGene(0)
		g = child.getGene(1)
		b = child.getGene(2)
		dr = abs(solution - r)
		dg = abs(solution - g)
		db = abs(solution - b)
		
		minz = dr
		chosen = 1
		if ( dg < minz	):
			minz = dg
			chosen = 2
		if (db < minz):
			minz = db
			chosen = 3
		# Modifying the genes to get closer to the solution
		if chosen == 1:
			if r > solution :
				r = r - int(dr*self.crossoverRate)
			elif r < solution :
				r = r + int(dr*self.crossoverRate)
			else :
				child.setSolutionId(self.Solution_Index)
			child.setGene(0,r)
			

		elif chosen == 2:
			if 	g > solution:
				g = g - int(dg*self.crossoverRate)

			elif g < solution:
				g = g + int(dg*self.crossoverRate)
			else:
				child.setSolutionId(self.Solution_Index)
			child.setGene(1,g)
			
		elif chosen == 3:
			if b > solution:
				b = b - int(db*self.crossoverRate)
			elif b < solution:
				b = b + int(db*self.crossoverRate)
			else:
				child.setSolutionId(self.Solution_Index)
			child.setGene(2,b)
			
		return child

	# This is mainly defined to carry out the mutation
	def mutate(self,c):
		gene_count=3
		SUBRACT=1
		ADD=2
		operation=random.randint(1,2)

		for index in range(gene_count):
			value=c.getGene(index)
			if(operation==SUBRACT):
				value-=int(value*self.mutationRate)
				if(value<0):
					value+=int(value*self.mutationRate)

			elif (operation==ADD):
				value+=int(value*self.mutationRate)
				if(value>254):
					value-=int(value*self.mutationRate)

			c.setGene(index,value)
		return c
	# This is used to select parent from the population
	def rankSelection(self, pop):

		randomFromRank=random.randint(0, 2)
		fittestChromosomes=pop.getFittestChromoCount()
		abc=fittestChromosomes[0]

		return fittestChromosomes[randomFromRank]