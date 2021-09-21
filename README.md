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

The experiments without crossover areÑ

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |   1051    | 
|   2   |    537    |   
|   3   |    305    | 
|   4   |     10    | 
|   5   |   6091    | 
|   6   |     10    | 
|   7   |   2124    | 
|   8   |    261    | 
|   9   |    173    | 
|  10   |   7717    | 
|  11   |    527    | 
|  12   |      6    | 
|  13   |      8    | 
|  14   |    694    | 
|  15   |     20    | 
|  16   |   2569    | 
|  17   |    397    | 
|  18   |   1695    | 
|  19   |    337    | 
|  20   |    133    | 
|  AVG  |   1233.3  | 

The experiments without mutations is:

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |      | 
|   2   |        |   
|   3   |        | 
|   4   |         | 
|   5   |       | 
|   6   |         | 
|   7   |       | 
|   8   |        | 
|   9   |        | 
|  10   |       | 
|  11   |       | 
|  12   |         | 
|  13   |          | 
|  14   |        | 
|  15   |         | 
|  16   |       | 
|  17   |        | 
|  18   |       | 
|  19   |        | 
|  20   |        | 
|  AVG  |     | 

The experiments using probability of crossocer like 0.9

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |   189   | 
|   2   |   250   |   
|   3   |   290   | 
|   4   |    10   | 
|   5   |   137   | 
|   6   |    30   | 
|   7   |   246   | 
|   8   |    61   | 
|   9   |    19   | 
|  10   |   140   | 
|  11   |     1   | 
|  12   |   834   | 
|  13   |    31   | 
|  14   |    93   | 
|  15   |    98   | 
|  16   |    71   | 
|  17   |   207   | 
|  18   |    13   | 
|  19   |    62   | 
|  20   |    18   | 
|  AVG  |   140   | 

The experiments using probability of crossocer like 0.3

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |   684   | 
|   2   |    13   |   
|   3   |    93   | 
|   4   |   119   | 
|   5   |     1   | 
|   6   |   384   | 
|   7   |    46   | 
|   8   |   139   | 
|   9   |    23   | 
|  10   |  1037   | 
|  11   |    21   | 
|  12   |   303   | 
|  13   |     1   | 
|  14   |   810   | 
|  15   |     2   | 
|  16   |   353   | 
|  17   |   610   | 
|  18   |    10   | 
|  19   |    37   | 
|  20   |   105   | 
|  AVG  |  239.6  | 

The experiments using always crossover and mutation

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

On average the algorithm using always crossover and mutation needs 12~13 generations to find the better solution


| Tried    |  50 chromosomes  |  100 chromosomes  |  500 chromosomes  |  1000 chromosomes  | 
| :------: | :------: |:------: |:------: |:------: |
|   1   |   1470    |   674    |     77    |     11    | 
|   2   |    855    |    34    |      1    |     87    |     
|   3   |     74    |    94    |      1    |     17    |   
|   4   |    168    |   200    |    159    |     33    |   
|   5   |    142    |   156    |     90    |     10    |   
|   6   |     13    |     1    |      8    |      1    |   
|   7   |      1    |   539    |     29    |     49    |   
|   8   |    859    |    38    |     19    |     18    |  
|   9   |   2077    |   157    |     12    |     19    |  
|  10   |     33    |    31    |     28    |     28    |  
|  11   |     69    |    12    |     31    |     13    |   
|  12   |    270    |    54    |      1    |     33    |   
|  13   |    198    |   163    |     61    |     1    |   
|  14   |    192    |   199    |     23    |     45    |   
|  15   |    428    |   193    |     22    |      7    |   
|  16   |     47    |    63    |     18    |      1    |   
|  17   |    124    |   334    |     19    |    144    |   
|  18   |     29    |  1019    |     38    |     27    |   
|  19   |   1825    |   288    |      1    |     21    |   
|  20   |    368    |    72    |     43    |     17    |   
|  AVG   |  462.1    |    216.1    |     34.1    |     20    |   





