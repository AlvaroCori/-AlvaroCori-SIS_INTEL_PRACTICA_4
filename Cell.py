from Chromosome import Chromosome
import random
class Cell:
    def evaluatePoblationFitness(self):
        counter = 0
        for chromosome in self.chromosomes:
            counter+=chromosome.fitness
        self.poblationFitness = counter
    def evaluateChromosomeProbabilities(self):
        self.probabilities = []
        for chromosome in self.chromosomes:
            self.probabilities.append(chromosome.fitness/self.poblationFitness)

    def __init__(self,poblation, sizeChromosome, classChromosome):
        self.chromosomes = [classChromosome(sizeChromosome) for _ in range(poblation)]
        self.poblation = poblation
        self.poblationFitness = 0
        self.probabilities = []
        self.evaluatePoblationFitness()
        self.evaluateChromosomeProbabilities()

    def insertAListOfChromosomes(self,chromosomes):
            self.chromosomes = chromosomes
            self.poblation = len(self.chromosomes)
            self.evaluatePoblationFitness()
            self.evaluateChromosomeProbabilities()

    def selectBestFitness(self):
        bestFitness = self.chromosomes[0].fitness
        bestChromosome = self.chromosomes[0]
        for chromosome in self.chromosomes:
            if (chromosome.fitness > bestFitness):
                bestChromosome = chromosome
                bestFitness = chromosome.fitness
        return bestChromosome



    