from Cromosome import Cromosome
from Cell import Cell
import pandas as pd
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
from GeneticAlgorithm import * 
#the function return true if a number stay in the range of probability            

def insertVariables(size,generations,poblation,solution,probabilityCrossover, probabilityMutation):
    variables = [size,generations,poblation,solution,probabilityCrossover, probabilityMutation]
    selection = -1
    while (selection != 0):
        print("SELECCION DE VARIABLES")
        print("------------------")
        print(f"1. Tamanio de cromosomas:     {variables[0]}")
        print(f"2. Numero de generaciones:    {variables[1]}")
        print(f"3. Poblacion de cromosomas:   {variables[2]}")
        print(f"4. Fitness para el objetivo:  {variables[3]}")
        print(f"5. Probabilidad de crossover: {variables[4]}")
        print(f"6. Probabilidad de mutacion:  {variables[5]}")
        print("0. volver.")
        print("------------------")
        selection = int(input())
        if (selection == 1):
            variables[0] = int(input())
        elif (selection == 2):
            variables[1] = int(input())
        elif (selection == 3):
            variables[2] = int(input())
        elif (selection == 4):
            variables[3] = float(input())
        elif (selection == 5):
            variables[4] = float(input())
        elif (selection == 6):
            variables[5] = float(input())
    return variables

def viewResults(cromosomes):
    a = 0
    for cromosome in cromosomes:
        if (cromosome):
            a+=1
            print(f" ({a}. {cromosome.fitness})",end="")
    print("")
def getAverageFitness(cromosomes):
    fitnessSum = 0
    size = len(cromosomes)
    for cromosome in cromosomes:
        fitnessSum += cromosome.fitness
    return fitnessSum/size
def viewPlot(cromosomes):
    size = len(cromosomes)
    fitnessList = [cromosome.fitness for cromosome in cromosomes]
    maxValue = max(fitnessList)
    minValue = min(fitnessList)
    average = sum(fitnessList)/len(fitnessList)
    maxIndex = fitnessList.index(maxValue)
    minIndex = fitnessList.index(minValue)
    df = pd.DataFrame({f"El punto mas alto es: {maxValue} en la {maxIndex+1}° generacion \nEl punto mas bajo es: {minValue} en la {minIndex+1}° generacion \n El promedio es: {average}" : fitnessList})
    matplotlib.use('TkAgg')
    df.plot(title='Fitness por generacion',color='blue',figsize=(9, 4))
    plt.scatter(range(size),fitnessList,color="yellow")
    plt.scatter([minIndex, maxIndex],[minValue,maxValue],color="red")
    plt.grid(color='black', linestyle='-', linewidth=0.5)
    plt.xlabel("Generacion")
    plt.ylabel("Fitness")
    plt.show()
def menu():
    init = 0
    end = 0
    selection = -1
    size = 20
    generations = 100
    population = 100
    solution = 20
    probabilityCrossover = 0.7
    probabilityMutation = 0.001
    bestResults = []
    cell = Cell(population, size)
    while(selection != 0):
        print("ALGORITMO GENETICO")
        print("------------------")
        print(f"Tamanio de cromosomas:     {size}")
        print(f"Numero de generaciones:    {generations}")
        print(f"Poblacion:    {population}")
        print(f"Solucion para el objetivo: {solution}")
        print(f"Probabilidad de crossover: {probabilityCrossover}")
        print(f"Probabilidad de mutacion:  {probabilityMutation}")
        print("------------------")
        print("1. Insertar variables.")
        print(f"2. Correr programa para {generations} generaciones.")
        print("3. Mostrar Grafico.")
        print(f"4. Ejecutar hasta encontrar una generacion con fitness de {solution}.")
        print(f"5. Ejecutar n veces hasta encontrar una generacion con fitness de {solution}.")
        print("0. Salir.")
        selection = int(input())
        if (selection == 1):
            size,generations, population,solution,probabilityCrossover, probabilityMutation = insertVariables(size,generations,population,solution,probabilityCrossover, probabilityMutation)
        elif (selection == 2):
            cell = Cell(population, size)
            init = time.time()
            bestResults = evolucionate(cell,generations,probabilityCrossover,probabilityMutation)
            end = time.time()
            viewResults(bestResults)
            print(f"El promedio del fitness es: {getAverageFitness(bestResults)}")
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")
        elif (selection == 3):
            viewPlot(bestResults)
        elif (selection == 4):
            cell = Cell(population, size)
            init = time.time()
            bestResults = evolucionate(cell,generations,probabilityCrossover,probabilityMutation,True, solution)
            end = time.time()
            viewResults(bestResults)
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")
        elif (selection == 5):
            print("Ingrese la cantidad: ", end="")
            n = int(input())
            total = 0
            init = time.time()
            for i in range(n):
                cell = Cell(population, size)
                bestResults = evolucionate(cell,generations,probabilityCrossover,probabilityMutation,True, solution)
                generation = len(bestResults)
                total += generation
                print(f"{i+1}. {generation}")
            end = time.time()
            print(f"El promedio es de: {total/n}")
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")
        if (selection >= 2 and selection <=5):
            input("presione enter para continuar.")

menu()

'''
#https://dcain.etsin.upm.es/~pablo/oye/simulaciones.html
'''
