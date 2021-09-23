import random
import math
class ChromosomeNumbers:
    def evaluateFitness(self):
        self.fitness = 0
        for gen in self.gens:
            if gen == 0:
                self.fitness+= 6
            elif gen == 1:
                self.fitness+= 10
            elif gen >= 2 and gen <= 4:
                self.fitness+= 6
            elif gen >= 5 and gen <= 7:
                self.fitness+= 4
            else:
                self.fitness+= 2
        
    def __init__(self,size):
         self.gens = [random.randint(0,9) for _ in range(size)]
         self.size = size
         self.fitness = 0
         self.evaluateFitness()
    def mutateGen(self):
        position = random.randint(0,self.size-1)
        newNumber = random.randint(0,9)
        self.gens[position]= newNumber
        self.evaluateFitness()

    def crossover(self, chromosome):
        index = random.randint(0,chromosome.size-1)#int(cromosome.size/2)
        part1 = chromosome.gens[0:index]
        part2 = chromosome.gens[index:chromosome.size]
        newCromosome1 = ChromosomeNumbers(chromosome.size)
        newCromosome2 = ChromosomeNumbers(chromosome.size)
        newCromosome1.gens = part1 + self.gens[index:self.size]
        newCromosome1.evaluateFitness()
        newCromosome2.gens = self.gens[0:index] + part2
        newCromosome2.evaluateFitness()
        return newCromosome1, newCromosome2
