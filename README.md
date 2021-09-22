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
### First we use a crossover that cut the information of both chromosomes by the middle.
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

The experiments without mutations is imposible if we cut the information of crossover by the middle, because if we compare all the cases and anyone have
only max numbers in the parts we can't take the goal of the max fitness.


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

The next table show the algorithm with the same values in probabilities, but the initial populations changes:

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


This experiment is seeing a random example that requires more than 100 generations, and show the best fitness in every generation

| Generation    |  Best Fitness  | 
| :------: | :------: |
|  1 |  16 |
|  2 |  16|
|  3 |  17|
|  4 |  17|
|  5 |  16|
|  6 |  16|
|  7 |  16|
|  8 |  16|
|  9 |  16|
|  10 |  16|
|  11 |  16|
|  12 |  16|
|  13 |  16|
|  14 |  16|
|  15 |  16|
|  16 |  16|
|  17 |  16|
|  18 |  16|
|  19 |  16|
|  20 |  16|
|  21 |  16|
|  22 |  16|
|  23 |  16|
|  24 |  16|
|  25 |  16|
|  26 |  16|
|  27 |  16|
|  28 |  16|
|  29 |  16|
|  30 |  16|
|  31 |  16|
|  32 |  16|
|  33 |  16|
|  34 |  16|
|  35 |  16|
|  36 |  16|
|  37 |  16|
|  38 |  16|
|  39 |  17|
|  40 |  17|
|  41 |  17|
|  42 |  17|
|  43 |  17|
|  44 |  17|
|  45 |  17|
|  46 |  17|
|  47 |  17|
|  48 |  17|
|  49 |  17|
|  50 |  17|
|  51 |  17|
|  52 |  17|
|  53 |  17|
|  54 |  17|
|  55 |  17|
|  56 |  17|
|  57 |  17|
|  58 |  17|
|  59 |  17|
|  60 |  17|
|  61 |  17|
|  62 |  17|
|  63 |  17|
|  64 |  17|
|  65 |  17|
|  66 |  17|
|  67 |  17|
|  68 |  17|
|  69 |  17|
|  70 |  17|
|  71 |  17|
|  72 |  17|
|  73 |  17|
|  74 |  17|
|  75 |  17|
|  76 |  17|
|  77 |  17|
|  78 |  17|
|  79 |  17|
|  80 |  17|
|  81 |  17|
|  82 |  17|
|  83 |  17|
|  84 |  17|
|  85 |  17|
|  86 |  17|
|  87 |  17|
|  88 |  17|
|  89 |  17|
|  90 |  17|
|  91 |  17|
|  92 |  17|
|  93 |  17|
|  94 |  17|
|  95 |  17|
|  96 |  17|
|  97 |  17|
|  98 |  18|
|  99 |  18|
|  100 |  18|

### Then we use a crossover that cut the information of both chromosomes in a randomic position index_random(1, n-2) where n is the quantity of information.

By the case we use a probability of crossover of 0.0 and a probability of mutation 0.001 is equal in results than the cut in crossover because we don't use
the crossover, the results are similar only with a little difference because the random values.

For the 3 next tables we use a poblation of 100 chromosomes and 20 spaces of information for each chromosomes.

In this case we use a probability of crossover of 0.7 and a probability of mutation 0.01.

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |    21    | 
|   2   |    29    |   
|   3   |    22    | 
|   4   |    55    | 
|   5   |    28    | 
|   6   |    25    | 
|   7   |    29    | 
|   8   |    28    | 
|   9   |    15    | 
|  10   |    16    | 
|  11   |    23    | 
|  12   |    16    | 
|  13   |    33    | 
|  14   |    47    | 
|  15   |    20    | 
|  16   |    18    | 
|  17   |    17    | 
|  18   |    11    | 
|  19   |    27    | 
|  20   |    12    | 
|  AVG   |  24.6   |

In this case we use a probability of crossover of 0.7 and a probability of mutation 0.0.

| Tried    |  Generation  | 
| :------: | :------: |
|   1   |    25    | 
|   2   |    24    |   
|   3   |    14    | 
|   4   |    20    | 
|   5   |    30    | 
|   6   |    21    | 
|   7   |    34    | 
|   8   |    27    | 
|   9   |    32    | 
|  10   |    36    | 
|  11   |    27    | 
|  12   |    27    | 
|  13   |    34    | 
|  14   |    14    | 
|  15   |     8    | 
|  16   |    22    | 
|  17   |    31    | 
|  18   |    43    | 
|  19   |    31    | 
|  20   |    32    | 
|  AVG   |  26.6   |


We compare many cases with different probability of crossover.
Probability of mutation for all cases: 0.001
Cromosomes of all cases:   100 

| Prob. Crossover    |  0.9  |  0.3  |  0.1 |  0.999  | 
| :------: | :------: |:------: |:------: |:------: |
|   1   |   22    |   34    |     1690    |     18    | 
|   2   |    16    |    68    |    1913    |     18   |     
|   3   |    21    |   640    |    809    |     22    |   
|   4   |    44    |   31    |     153    |     35    |   
|   5   |    17    |   364    |    100    |     25    |   
|   6   |     27    |    204    |     797    |     10    |   
|   7   |    34    |   42    |     871    |     8    |   
|   8   |    20    |    149    |     26    |     24    |  
|   9   |   22    |   54    |     57    |     17    |  
|  10   |     26    |    273    |     933    |     11    |  
|  11   |     27   |    25    |     92    |     24    |   
|  12   |    29    |    24    |     357    |     22    |   
|  13   |    572    |   39    |     1590    |     23   |   
|  14   |    29    |   177    |     74    |     31    |   
|  15   |    18    |   601    |     684    |      23   |   
|  16   |     29    |    197    |     908    |      20    |   
|  17   |    19    |   31    |     154    |    27    |   
|  18   |     58    |  187    |     28    |     12   |   
|  19   |   20    |   22    |     425    |     24    |   
|  20   |    17    |    1002    |     961    |     29    |   
|  AVG   |  53.35    |    208.2    |     631.1    |     21.15    |   
|  seg.   |  21.63    |    252.41    |     332.41    |     5.15    |   

We variate the poblation in order to get differents results.

| Tried    |  50 chromosomes  |  100 chromosomes  |  500 chromosomes  |  1000 chromosomes  | 
| :------: | :------: |:------: |:------: |:------: |
|   1   |   35    |   27    |     18    |     12    | 
|   2   |    1628    |    8    |     13    |     83    |     
|   3   |    4420    |    21    |     15    |     14    |   
|   4   |    538    |   24    |     15    |     14    |   
|   5   |    62    |   16    |     18    |     16    |   
|   6   |     31    |    14    |      8    |     18    |   
|   7   |    201    |   20    |     20    |     11    |   
|   8   |    23    |    30    |     16    |     18    |  
|   9   |   338    |   24    |     11    |     13    |  
|  10   |     729    |    31    |     13    |     16    |  
|  11   |     421   |    29    |     8    |     12    |   
|  12   |    3996    |    30    |     11    |     14    |   
|  13   |    18187    |   195    |     15    |     12   |   
|  14   |    28    |   33    |     20    |     44    |   
|  15   |    37    |   45    |     10    |      9   |   
|  16   |     19    |    17    |     13    |      18    |   
|  17   |    1470    |   80    |     8    |    18    |   
|  18   |     19    |  18    |     7    |     9    |   
|  19   |   33    |   26    |     15    |     24    |   
|  20   |    2605    |    18    |     17    |     11    |   
|  AVG   |  1741.0    |    35.3    |     13.5    |     14.3    |   
|  seg.   |  85.45    |    60.41    |     110.36    |     120.47    | 
