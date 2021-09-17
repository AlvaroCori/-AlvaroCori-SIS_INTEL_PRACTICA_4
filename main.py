from Cromosome import Cromosome
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
#the function return true if a number stay in the range of probability
def getProbability(prob, size):
    return prob <= np.random.randint(1,size+1)
def selection():
    return True
def crossover(prob , cromosome1, cromosome2):
    if (getProbability(prob, 100)):
        cromosome1.crossover(cromosome2)
    return True

def mutation(prob , cromosome):
    if (getProbability(prob, 100)):
        cromosome.mutateGen()
c = Cromosome(10)
d = Cromosome(10)
print(c.gens)
print(d.gens)
c.crossover(d)

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