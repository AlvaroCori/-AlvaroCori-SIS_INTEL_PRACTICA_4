import random
from functools import reduce
class Cromosome:
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
    def crossover(self, cromosome):
        index = random.randint(1,cromosome.size-2)#int(cromosome.size/2)
        part1 = cromosome.gens[0:index]
        part2 = cromosome.gens[index:cromosome.size]
        newCromosome1 = Cromosome(cromosome.size)
        newCromosome2 = Cromosome(cromosome.size)
        newCromosome1.gens = part1 + self.gens[index:self.size]
        newCromosome1.evaluateFitness()
        newCromosome2.gens = self.gens[0:index] + part2
        newCromosome2.evaluateFitness()
        return newCromosome1, newCromosome2
        '''
        cromosome.gens = part1 + self.gens[int(self.size/2):self.size]
        cromosome.evaluateFitness()
        self.gens = self.gens[0:int(self.size/2)]+part2
        self.evaluateFitness()
        '''

#boolean python
#https://www.kite.com/python/answers/how-to-get-a-random-boolean-in-python
#reduce
#https://www.geeksforgeeks.org/reduce-in-python/