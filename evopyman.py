from random import Random, randint, random
from pygene.gene import BaseGene, FloatGene
from pygene.organism import Organism
from pygene.population import Population
from hashlib import sha1
from instruction import *
from pacman import pacman_fitness_function
from sys import argv
	
organismLen = 80 # PARAM: liczba instrukcji w mozgu
testsNum = 1 # PARAM: liczba powtorzen przy obliczaniu wartosci funkcji celu

class MyGen(BaseGene):
	mutProb = 0.01 # PARAM: prawdopodobienstwo zmutowania genu
	def mutate(self):
		self.value = self.randomValue()
	def randomValue(self):
		r = Instruction()
		# r = 1
		# print r
		return r
		
genomeProto = {}
for i in range(organismLen):
	genomeProto[str(i)] = MyGen
	
class MySpecimen(Organism):
	genome = genomeProto
	mutateOneOnly = False # PARAM: czy mutowac tylko jeden gen (True), czy sprawdzac dla kazdego mutProb (False)
	crossoverRate = 0.5
	def fitness(self):
		brain = []
		for i in xrange(organismLen):
			brain.append(self[str(i)])
		g = False
		if(len(argv) > 1):
			if argv[1] == "1":
				g = True
		pff = pacman_fitness_function(genotyp = brain, n = testsNum, graphics = g)
		return pff
		# return sha1(self.hashIt()).hexdigest()
	def mate(self, partner):
		child1 = MySpecimen()
		child2 = MySpecimen()
	
		for i in xrange(organismLen):
			if random() < self.crossoverRate:
				child1.genes[str(i)].value = self[str(i)]
				child2.genes[str(i)].value = partner[str(i)]
			else:
				child1.genes[str(i)].value = partner[str(i)]
				child2.genes[str(i)].value = self[str(i)]
		
		return (child1, child2)
	def hashIt(self):
		s = ""
		for i in xrange(organismLen):
			s += str(self[str(i)])
		return s
	def __repr__(self):
		s = ""
		for i in xrange(organismLen):
			s += " " + str(self[str(i)]) + "\n"
		return "{" + s + " }[ " + str(self.fitness()) + " ]"

class MyPopulation(Population):
	# PARAM: przycina populacje to tylu dzieci
	childCull = 20
	
	# PARAM: generuje duza populacje dzieci (tak naprawde to liczba par dzieci)
	childCount = 100
	
	# PARAM: liczba przekazywanych najlepszych rodzicow do kolejnen populacji
	incest = 2
	
	# PARAM: losuje nowe organizmy, nie uzywamy bo zamula
	numNewOrganisms = 0 
	
	# PARAM: wielkosc poczatkowej populacji
	initPopulation = 20
	
	# set to species of organism
	species = MySpecimen
	
	# PARAM: jesli mutateAfterMating == False to to oznacza ile jaki procent mutantow dodamy
	mutants = 0.2
	
	# PARAM: mutujemy wszystkie dzieci (True), albo dodajemy nowe mutanty (False)
	mutateAfterMating = True
		
pop = MyPopulation()

def main():
	try:
		while True:
			pop.gen()
			best = pop.best()
			print best

	except KeyboardInterrupt:
		pass


if __name__ == '__main__':
	main()