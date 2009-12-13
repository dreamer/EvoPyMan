from random import Random, randint, random
from pygene.gene import BaseGene, FloatGene
from pygene.organism import Organism
from pygene.population import Population
from hashlib import sha1
from instruction import *
    
organismLen = 10

class MyGen(BaseGene):
    mutProb = 0.01
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
    mutateOneOnly = False
    crossoverRate = 0.5
    def fitness(self):
        return sha1(self.hashIt()).hexdigest()
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
    # cull to this many children after each generation
    childCull = 20
    
    # number of children to create after each generation (tak naprawde to liczba par dzieci)
    childCount = 100
    
    # max number of best parents to mix amongst the kids for
    # next generation
    incest = 2
    
    # parameters governing addition of random new organisms
    numNewOrganisms = 0 # number of new orgs to add each generation (tak naprawde dodaje initPopulation organizmow, i to dodaje je przed krzyzowaniem, ostro przymula)
    
    # set to initial population size
    initPopulation = 20
    
    # set to species of organism
    species = MySpecimen
    
    # mutate this proportion of organisms
    mutants = 0.2
    
    # set this to true to mutate all progeny
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