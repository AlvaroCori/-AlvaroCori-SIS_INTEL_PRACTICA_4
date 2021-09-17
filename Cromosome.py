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
        position = random.randint(0,self.size)
        self.gens[position]= ~self.gens[position]
        self.evaluateFitness()
    def crossover(self, cromosome):
        part1 = cromosome.gens[0:int(cromosome.size/2)]
        part2 = cromosome.gens[int(cromosome.size/2):cromosome.size]
        cromosome.gens = part1 + self.gens[int(self.size/2):self.size]
        cromosome.evaluateFitness()
        self.gens = self.gens[0:int(self.size/2)]+part2
        self.evaluateFitness()
        print(self.gens)
        print(cromosome.gens)


#boolean python
#https://www.kite.com/python/answers/how-to-get-a-random-boolean-in-python
#reduce
#https://www.geeksforgeeks.org/reduce-in-python/