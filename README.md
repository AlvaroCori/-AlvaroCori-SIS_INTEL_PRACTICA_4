# -AlvaroCori-SIS_INTEL_PRACTICA_4
Algoritmos genericos practica 4 de Sistemas Inteligentes
## Description Of Problem
The genetic is a science of biology that study biological inheritance from generation to generation through DNA, the DNA is the essence of many living organisms, the DNA contain information that define the organisms like his shape, size, behavior, etc.
The chromosomes are highly organized structures, formed by proteins and Gens, the gens in turn contain DNA. When chromosomes are replicating, they can do an exact copy or a combination with another chromosome. Rarely the new chromosome mutates a part of the genetic information that contain
Well in Artificial Intelligence the genetic is used when we use an evolution of the input during the execution of a program, this is used for resolve problems of search the state like the problem of the 8 queens, search the best chromosome with the mayor information and other more.
When we search the mayor information in a chromosome. We need to take a generation that consist in combine and set parts of information of a chromosome, the input consists in a population of chromosomes that contain random information.
## Description Of Solution
For this algorithm we have a class Chromosome that contain n gens, every gen has a value (bool or int) initialized with random numbers and the fitness of the gens.
The fitness is similar at a heuristic function, this consist in the quantity of gens that are equal at 1 or true.
We will need a structure called Cell that contain the population of Chromosomes and can get the sum of all chromosome’s fitness, the fitness population.
All chromosome’s will replicate in every generation of two forms first we need to select, crossover 2 chromosome’s and mutate.

Selection. - Consist in take 2 chromosomes of the population with a probability, the probability for a chromosome be selected is the fitness of chromosome out of fitness population.

Crossover. – The crossover consist in combine the gens of 2 chromosomes, we take a position for cut the array and create a new array consisting of the first part of the genes of one chromosome next to the second of the other chromosome to create a new one. For the other chromosome also we do the change but taking the parts that don’t have the first new chromosome.
The condition of realize a crossover is a probability if the probability is into 0% and a n% (at most 100%) we realize the crossover in other case we only replicate both chromosomes forming 2 news chromosomes equals in gens and fitness.

Mutation. – A mutation is the altering of array element example (0 -> 1 or 1->0), we take a probability if the probability is into 0.0% and a n% (at most 100.0%) we realize the mutation in other case we not alter any array element. 

The crossover and the mutation are probabilities independents of each one.

###### Initial State:
A population of chromosomes with a specific size of information (array of int).
###### Goal State:
A chromosome that contain the biggest quantity of information (The chromosome that contain all the array with ones).
###### Actions:
Select two chromosomes of population.
Crossover bot chromosomes with a probability.
Mutate a element of array changing the information with a probability.
###### Transition Module:
Selection (chromosomes, quantity, probabilities of chromosome)
Crossover (chromosome1, chromosome2, index of cut)
Mutation (chromosome)
###### Test of the target:
Get the biggest quantity of information in a chromosome.
###### Cost of the path:
The number of generation.

#### Python
We use the language Python because this language has a large collection of util libraries, In this exercise a clarity preference in order to use Python is the pass of parameters for Functions because we are pass the heuristic function like a variable.
Python also is a language applicable and recommendable for the Intelligence Artificial because the syntax helps much in the development.

## Experiments And Results
==========================

The first point to experiment is run the algorithm 20 times and see all the results and in which generation finds the better solution.

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |    406    | 
|   2   |    119    |   
|   3   |     86    | 
|   4   |     24    | 
|   5   |     63    | 
|   6   |    251    | 
|   7   |   1755    | 
|   8   |     39    | 
|   9   |    158    | 
|  10   |     81    | 
|  11   |    113    | 
|  12   |     60    | 
|  13   |     23    | 
|  14   |    106    | 
|  15   |    128    | 
|  16   |     63    | 
|  17   |   1029    | 
|  18   |     19    | 
|  19   |    190    | 
|  20   |    829    | 
|  AVG  |    277.1  | 

Esta tabla es haciendo siempre crossover y siempre mutacion

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |    11    | 
|   2   |    13    |   
|   3   |    11    | 
|   4   |    11    | 
|   5   |    11    | 
|   6   |    13    | 
|   7   |    11    | 
|   8   |    13    | 
|   9   |    18    | 
|  10   |    18    | 
|  11   |    17    | 
|  12   |    12    | 
|  13   |    13    | 
|  14   |    11    | 
|  15   |    16    | 
|  16   |     7    | 
|  17   |    13    | 
|  18   |    13    | 
|  19   |     6    | 
|  20   |    14    | 
|  AVG   |  12.6    | 

On average the algorithm needs 12~13 generations to find the better solution

To the next experiment, we tried the same but the probability of the crossover is 0, and these are the results:



For this experiment, the results are more dispersed, we have like the best result ass 5, and the worse ass 78, the gap is very big, but the average is better with a crossover probability of zero, and there are more results under 10 than the previous experiment.


For the next experiment, we tried change the mutation probability to zero, but with a probability of the crossover in 0.7, and the results are:



