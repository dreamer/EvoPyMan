from random import Random, randint, random
from pygene.gene import BaseGene, FloatGene
from pygene.organism import Organism
from pygene.population import Population
    
organismLen = 5

MyRandom = Random()

Direction = {
    "north" : 0,
    "n" : 0,
    0 : "north",
    "south" : 1,
    "s" : 1,
    1 : "south",
    "east"  : 2,
    "e" : 2,
    2 : "east",
    "west"  : 3,
    "w" : 3,
    3 : "west"
    }
    
Element = {
    "Ghost" : 0,
    0 : "Ghost",
    "SmallDot" : 1,
    1 : "SmallDot",
    "BigDot" : 2,
    2 : "BigDot"
    }

Mode = { "Good" : 0,
    0 : "Good",
    "Bad" : 1,
    1 : "Bad"
    }

class Instruction:
    def __init__(self):
        self.randomValue()
    def randomValue(self):
        self.direction = Direction[randint(0,3)]
        self.mode = Mode[randint(0,1)]
        self.element = Element[randint(0,2)]
        self.distStart = randint(1, 10)
    def __repr__(self):
        return "%s : %s - %s : %s - %s -" % (
            self.direction, Direction[self.direction], 
            self.mode, Mode[self.mode],
            self.dist)
    
class MyGen(BaseGene):
    maxInt = 100
    mutProb = 0.05
    def mutate(self):
        self.value = self.randomValue()
        #print "mutate"
    def randomValue(self):
        r = MyRandom.randint(1,self.maxInt)
        #print r
        return r
        # print "randomValue"
    def __add__(self, other):
        print "add"
        return (self.value + other.value) / 2
    
genomeProto = {}
for i in range(organismLen):
    genomeProto[str(i)] = MyGen
    
class MySpecimen(Organism):
    genome = genomeProto
    mutateOneOnly = False
    crossoverRate = 0.5
    def fitness(self):
        fit = 0
        for i in xrange(organismLen):
            fit += self[str(i)]
        return fit
    def mate(self, partner):
        """
        Mates this organism with another organism to
        produce two entirely new organisms via random choice
        of genes from this or the partner
        """
        child1 = MySpecimen()
        child2 = MySpecimen()
    
        # gene by gene, we assign our and partner's genes randomly
        for i in xrange(organismLen):
            if random() < self.crossoverRate:
                child1.genes[str(i)].value = self[str(i)]
                child2.genes[str(i)].value = partner[str(i)]
            else:
                child1.genes[str(i)].value = partner[str(i)]
                child2.genes[str(i)].value = self[str(i)]
        
        # done
        return (child1, child2)
    def __repr__(self):
        s = ""
        for i in xrange(organismLen):
            s += " " + str(self[str(i)])
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
    i = Instruction()
    print i
    return
    try:
        print pop
        while True:
            pop.gen()
            #print "GenSize: ", len(pop)
            best = pop.best()
            print best
            #return

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()