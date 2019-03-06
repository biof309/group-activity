# Name
Samuel J. Magaziner

# Hobby
Fish keeping.

# Fun Fact
I have a virus named after myself (phiSM).  

# Programming Background
Pretty much nothing outside of learning basic linux syntax in order to run phylogenetics packages.

# Interesting Python code
```python
# %% This is a password guess algorithm employing a fitness function
# These are the initial variables
#Set the target variable using upper or lowecase letters, spaces, and !.
from datetime import datetime

letters = [chr(i+65) for i in range(26)]
LETTERS = [chr(i+97) for i in range(26)]
Exclam = [chr(33)]
space = [chr(32)]
geneSET = letters + LETTERS + Exclam + space
print(geneSET)
target = "What is it we value but Innovation Originality Novelty But most importantly timeliness I fear you may be too late my confused unfortunate friend"

#Generate a guess (here we are using the random function to generate a guess
#Note the use of list functions and package functions

import random
help(random)
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSET))
        genes.extend(random.sample(geneSET, sampleSize))
    return ''.join(genes)

#This is the fitness value
def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)

#Mutation engine
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSET, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

#making a display
import datetime
def display(guess):
    time_diff = datetime.datetime.now() - StartTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess, fitness, time_diff))

random.seed()
StartTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

#Key loop function
while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
```
