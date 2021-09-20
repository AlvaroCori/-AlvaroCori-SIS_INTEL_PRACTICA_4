# -AlvaroCori-SIS_INTEL_PRACTICA_4
Algoritmos genericos practica 4 de Sistemas Inteligentes

Experiments And Results
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



