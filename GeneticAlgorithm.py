import random
from numpy.random.mtrand import rand
from Cromosome import Cromosome
from Cell import Cell
import copy as cp
import pandas as pd
import numpy as np

def getProbability(probability):
    return random.randint(0,1000)/1000 < probability

def selection(cell, quantity):
    return np.random.choice(a=cell.cromosomes,size=quantity,p=cell.probabilities)

def intentCrossover(c1, c2, probability):
    nc1 = None
    nc2 = None
    if (getProbability(probability)):
        nc1, nc2 = c1.crossover(c2)
    else:
        nc1 = cp.copy(c1)
        nc2 = cp.copy(c2)
    return nc1,nc2

def intentMutation(c1,c2,probability):
    if (getProbability(probability)):
            c1.mutateGen()
            c2.mutateGen()
    return c1,c2

def evolucionate(cell , generations, probabilityCross, probabilityMut,runUntilTheSolution=False,solution=0):
    bestResults = [cell.selectBestFitness()] 
    if (runUntilTheSolution):
        generations = 9999999
    for i in range(generations-1):
        cromosomes=[]
        for j in range(int(cell.poblation/2)):
            c1, c2 = selection(cell, 2)
            nc1, nc2 = intentCrossover(c1,c2,probabilityCross)
            nc1, nc2 = intentMutation(nc1,nc2, probabilityMut)
            cromosomes.append(nc1)
            cromosomes.append(nc2)
        cell.insertAListOfCromosomes(cromosomes)
        bestFitness = cell.selectBestFitness()
        bestResults.append(bestFitness)
        if (runUntilTheSolution and bestFitness.fitness >= solution):
            break
    return bestResults