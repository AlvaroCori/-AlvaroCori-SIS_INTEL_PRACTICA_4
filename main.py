import random

from numpy.random.mtrand import rand
from Cromosome import Cromosome
from Cell import Cell
import copy as cp
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
#the function return true if a number stay in the range of probability
def getProbability(probability):
    return random.randint(0,1000)/1000 < probability
def selection():
    return True


def evolucionate(cell , generations, probabilityCross, probabilityMut):
    bestResults = [cell.selectBestFitness()] 
    for i in range(generations):
        cromosomes=[]
        for j in range(int(cell.poblation/2)):
            c1, c2 = np.random.choice(a=cell.cromosomes,size=2,p=cell.probabilities)
            if (getProbability(probabilityCross)):
                nc1, nc2 = c1.crossover(c2)
            else:
                nc1 = cp.copy(c1)
                nc2 = cp.copy(c2)
            if (getProbability(probabilityMut)):
                nc1.mutateGen()
                nc2.mutateGen()
            cromosomes.append(nc1)
            cromosomes.append(nc2)
        cell.insertAListOfCromosomes(cromosomes)
        bestResults.append(cell.selectBestFitness())
    return bestResults

solution = 20
cell = Cell(poblation = 100, sizeCromosome = 20)
a = 0
for cromosome in evolucionate(cell,20,0.7,0.001):
    if (cromosome):
        a+=1
        print(cromosome.fitness)
        if (cromosome.fitness == solution):
            print("Se hallo el cromosoma objetivo en la generacion: ",a-1)

#print(np.random.choice(a=[2,8],size=1,p=[1,0]))

'''
# Ejemplo ley de grandes números
# moneda p=1/2 cara=1 seca=0
resultados = []
for lanzamientos in range(1,10000):
    lanzamientos = np.random.choice([0,1], lanzamientos) 
    caras = lanzamientos.mean()
    resultados.append(caras)
# graficamente
df = pd.DataFrame({ 'lanzamientos' : resultados})
matplotlib.use('TkAgg')
df.plot(title='Ley de grandes números',color='r',figsize=(8, 6))
plt.axhline(0.5)
plt.xlabel("Número de lanzamientos")
plt.ylabel("frecuencia caras")
plt.show()
#https://dcain.etsin.upm.es/~pablo/oye/simulaciones.html
'''
