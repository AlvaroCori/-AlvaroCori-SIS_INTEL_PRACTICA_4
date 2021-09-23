import random
from functools import reduce
class Chromosome:
    def evaluateFitness(self):
        self.fitness = reduce(lambda com, g:com +( 1 if g else 0), self.gens)
    def __init__(self,size):
         self.gens = [bool(random.getrandbits(1)) for _ in range(size)]
         self.size = size
         self.fitness = 0
         self.evaluateFitness()
    def mutateGen(self):
        position = random.randint(0,self.size-1)
        self.gens[position]= ~self.gens[position]
        self.evaluateFitness()
    def crossover(self, chromosome):
        index = random.randint(0,chromosome.size-1)#int(chromosome.size/2)
        part1 = chromosome.gens[0:index]
        part2 = chromosome.gens[index:chromosome.size]
        newChromosome1 = Chromosome(chromosome.size)
        newChromosome2 = Chromosome(chromosome.size)
        newChromosome1.gens = part1 + self.gens[index:self.size]
        newChromosome1.evaluateFitness()
        newChromosome2.gens = self.gens[0:index] + part2
        newChromosome2.evaluateFitness()
        return newChromosome1, newChromosome2

