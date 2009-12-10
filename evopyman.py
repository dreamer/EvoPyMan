from pygene.gene import FloatGene, FloatGeneMax
from pygene.organism import Organism
from pygene.population import Population

pop = Population(species=Converger, init=2, childCount=50, childCull=20)
    
class QuadraticSolver(Organism):
        

def main():
    try:
        while True:
            # execute a generation
            pop.gen()

            # get the fittest member
            best = pop.best()
            
            # and dump it out
            print best

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()