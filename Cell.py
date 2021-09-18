from Cromosome import Cromosome
import random
class Cell:
    def evaluatePoblationFitness(self):
        counter = 0
        for cromosome in self.cromosomes:
            counter+=cromosome.fitness
        self.poblationFitness = counter
    def evaluateCromosomeProbabilities(self):
        self.probabilities = []
        for cromosome in self.cromosomes:
            self.probabilities.append(cromosome.fitness/self.poblationFitness)

    def __init__(self,poblation, sizeCromosome):
        self.cromosomes = [Cromosome(sizeCromosome) for _ in range(poblation)]
        self.poblation = poblation
        self.poblationFitness = 0
        self.probabilities = []
        self.evaluatePoblationFitness()
        self.evaluateCromosomeProbabilities()

    def insertAListOfCromosomes(self,cromosomes):
            self.cromosomes = cromosomes
            self.poblation = len(self.cromosomes)
            self.evaluatePoblationFitness()
            self.evaluateCromosomeProbabilities()

    def selectBestFitness(self):
        bestFitness = 0
        bestCromosome = None
        for cromosome in self.cromosomes:
            if (cromosome.fitness > bestFitness):
                bestCromosome = cromosome
                bestFitness = cromosome.fitness
        return bestCromosome


#random choice
#https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    