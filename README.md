# -AlvaroCori-SIS_INTEL_PRACTICA_4
Algoritmos genericos practica 4 de Sistemas Inteligentes

Alvaro Bryan Cori Sanchez <br>
Omar Christian Arias Chavez

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
The table to experiments running the algorithm 20 times and see all the results and in which generation finds the better solution is the next, trying with different values on the probabilities of crossover.

| Tried    |   Best Generation   |    Best Generation  |    Best Generation  |    Best Generation  |
| :------: | :------: | :------: | :------: |  :------: |
|       | C: 0.7 ; M:0.001 | C: 0.9 ; M:0.001 | C: 0.3 ; M:0.001 | C: 0 ; M:0.001 |
|   1   |    406    |    189   |    684  |   1051    | 
|   2   |    119    |    250   |    13   |    537    |    
|   3   |     86    |    290   |    93   |    305    |  
|   4   |     24    |     10   |   119   |     10    | 
|   5   |     63    |   137    |     1   |   6091    |  
|   6   |    251    |     30   |   384   |     10    | 
|   7   |   1755    |    246   |    46   |   2124    | 
|   8   |     39    |    61    |   139   |    261    | 
|   9   |    158    |     19   |    23   |    173    |  
|  10   |     81    |    140   |  1037   |   7717    | 
|  11   |    113    |      1   |    21   |    527    |  
|  12   |     60    |    834   |   303   |      6    |  
|  13   |     23    |     31   |     1   |      8    | 
|  14   |    106    |     93   |   810   |    694    | 
|  15   |    128    |     98   |     2   |     20    |  
|  16   |     63    |     71   |   353   |   2569    |  
|  17   |   1029    |    207   |   610   |    397    | 
|  18   |     19    |     13   |    10   |   1695    | 
|  19   |    190    |     62   |    37   |    337    |  
|  20   |    829    |     18   |   105   |    133    |  
|  AVG  |    277.1  |    140   |  239.6  |   1233.3  |  

The experiments without mutations is imposible if we cut the information of crossover by the middle, because if we compare all the cases and anyone have
only max numbers in the parts we can't take the goal of the max fitness.

The best result have the crossover with a probability of 0.9

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

This is an extra experiment to see to see this possibility, and we were surprised by the good results.

The next table show the algorithm with the same values in probabilities (Crossover = 0.7, mutation = 0.001), but the initial populations changes:

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

The best result is the population of 1000 chromosomes.

This experiment is seeing a random example that requires more than 100 generations, and show the best fitness in every generation

![grafic_2](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/grafico2.png)

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

The best result is the test that we do more crossover (0.999).

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
|  seg.   |  85.45    |    60.41    |     53.02    |     175.47    | 

The next grafics are independient of table values, the grafics demostrate the evolution of fitness in each population. 

## POPULATION OF 50
![grafic_pop1](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/graficopopulation1.png)
### From matplotlib.pyplot library

## POPULATION OF 100
![grafic_pop2](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/graficopopulation2.png)
### From matplotlib.pyplot library

## POPULATION OF 500
![grafic_pop3](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/graficopopulation3.png)
### From matplotlib.pyplot library

## POPULATION OF 1000
![grafic_pop4](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/graficopopulation4.png)
### From matplotlib.pyplot library

The best result is the population of 500 chromosomes.

Now we use:
Probability of crossover: 0.7
Probability of mutation: 0.001
Size of information for chromosome: 20
Poblation:  100
And we will take until the 100° generation.


![grafic_1](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/grafico1.png)
### From matplotlib.pyplot library

#### Beans
We try to implement an algorithm where we calculate an approximation to the number 1 where the most distant numbers have a lower fitness.
First we tried subtracting them at least 11 numbers more small have bigger fitness. 
Second tried to implement the same step but for a more noticeable difference using the factorial, however both cases fail.

The aleatority of the mutation can't take a well number into 0 to 9. The algorithm go to a result where all the chromosomes have the same quantity of information and in this
case the crossover is unusuable.  When a chromosome mutate if get less fitness the crossover copy to the others and the chromosome returns to a state as it was before mutual if the fitness is better is rarely because the algorithm take a long time to adapted the algorithm, only in the first and second methods we get the best fitness by a population of 6 chromosomes.

### The search of the best fitness using the first fitness function
![grafic_3](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/grafico3.png)
### From matplotlib.pyplot library
In this case the max fitness is 200.

By the third intent we get a teacher feedback to adjust some exercise parameters.

In the third intent we implement a fitness function that only sum 10 if the gen of the chromosome be 1 for other numbers (0,2,3,4,5,6,7,8,9) the result is 0, the function get best results only if the probability of mutation be high (0.7).

Then we tried new cases by the next values:

poblation     100<br>
fitness       200<br>
P. Crossover  0.7<br>
P. Mutation   0.1

In the fourth intent we tried the next function:

For a gen equal a 0 the fitness is 9<br>
For a gen equal a 1 the fitness is 10<br>
For a gen equal a 2 until 9 the fitness is 4

The results are:<br>
Chromosome with the best fitness in the generation 7237<br>
422.85 seg -> printing fitness and gens.

In the fifth intent we tried the next function:

For a gen equal a 0 the fitness is 9<br>
For a gen equal a 1 the fitness is 10<br>
For a gen equal a 2 until 5 the fitness is 4<br>
For a gen equal a 6 until 9 the fitness is 2

The results are:
Chromosome with the best fitness in the generation 2459<br>
159.2 seg -> printing fitness and gens.

In the sixth intent we tried the next function:

For a gen equal a 0 the fitness is 6<br>
For a gen equal a 1 the fitness is 10<br>
For a gen equal a 2 until 4 the fitness is 6<br>
For a gen equal a 5 until 7 the fitness is 4<br>
For a gen equal a 8 and 9 the fitness is 2

The results are:
Chromosome with the best fitness in the generation 2521<br>
135.82 seg -> printing fitness and gens.<br>
In other intent the time was:<br>
83.47 seg -> without print fitness and gens.

Using the sixt intent, we tried a intent with a mutation probability of 0.01.

The results are:<br>
Chromosome with the best fitness in the generation 14452<br>
209.38 seg -> without printing fitness and gens.

Using the sixt intent, we tried with two intents with a mutation probability of 0.001.

The results are:<br>
Chromosome with the best fitness in the generation 249397<br>
5055.04 seg or 84.25 min or 1.40 hours -> without printing fitness and gens.<br>
Chromosome with the best fitness in the generation 172653<br>
1726.53 seg or 28.78 min or 0.48 hours -> without printing fitness and gens.

### The search of the best function with the sixth fitness function
![grafic_4](https://github.com/AlvaroCori/-AlvaroCori-SIS_INTEL_PRACTICA_4/blob/main/img/grafico4.png)
### From matplotlib.pyplot library

We get the best fitness using the sixth fitness function.



### Conclusions
The genetic algorithm is well aplicable for the inteligence artificial, because this let that a input change and the most efficiencial cases can arrive at the output.

If we compare crossover cutting experiments in half with those that are randomly cut we can see a big difference, in conclusion the random cut selection is more efficient because it allows more combinations than just cutting in half. There are even experiments in cutting in half where the best fitness is not found before reaching the generation limit, see the 100 generation limit experiment. Incluse a algorithm in middle cut take more of 4 minutes for get the best fitness while the random cut take
less than 1 minutes mayoritarity in get the best fitness. 

The means obtained by doing various tests have a lot to do with the crossover and the mutation. For example, when we do not use the crossover we can take a long time to find the best fitness by using only a small chance of mutation.

When we do not make the mutation, in the case of crossover cutting in half it is very impossible to get the highest fitness because in all crossover combinations can not have all the digits in 1. When we make the random cut in the crossover we have more combinations to find the chromosome with the greatest fitness and you can find it, however it is also considerable that it cannot be found because for example if no chromosome has the digit 1 in a specific position you will not be able to find the greatest fitness even making all the combinations.

We can also see that chromosomes that perform more crossover are more likely to leave a legacy with greater fitness in younger generations.

If we compare the population, we can see that the larger the population the result of obtaining the best fitness appears in earlier generations, however when we compare the time it takes a little longer than those with a smaller population. The reason why older populations are more efficient is because we have many potential chromosomes and being able to choose in the selection the most likely to do the crossover can get faster the best fitness see the figure about the populations even though it takes longer to process in the large population.

When we compare the worst and best fitness in a range of 100 generations the worst fitness is usually the first or at least in the first generations being the best fitness that appears after a few generations and at the end usually maintain the highest fitness.

When we use numbers from 0 to 9 instead of bools we can get to a situation where the next generations have identical chromosomes between them and it is very difficult to improve when there is mutual value that raises fitness. When ee place the highest value to the number with the highest fitness (1) and place weights between ranges being the closest to 1 with the highest fitness the function is more effective, The optimal fitness fuction found works well with a high mutation probability but we only realize 2 tries with a very low mutation probability (0.001) because the function take a couple of hours to find the optimal solution. 

## Bibliografy
### Random choice<br>
https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html

### Boolean random python<br>
https://www.kite.com/python/answers/how-to-get-a-random-boolean-in-python

### Reduce function<br>
https://www.geeksforgeeks.org/reduce-in-python/

### Aleatory algorithm and grafics<br>
https://dcain.etsin.upm.es/~pablo/oye/simulaciones.html

### Matplotlyb.pyplot<br>
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
