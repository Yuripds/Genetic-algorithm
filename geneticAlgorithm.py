import numpy as np
from random import randint
from random import random


def populationGenerator(popSize,ngenes,type,vmax=5):
    
    if type=='bin':
        population = np.random.randint(2, size=(popSize,ngenes))
    else:
        population = np.random.randint(vmax, size=(popSize,ngenes))


    return population


def fitFunction(cromossomo):

    ##### trocar essa função pela funçaõ de taxa de transmissão
    score = cromossomo**2

    return score


### não entendi esse k igual a 2
### como meu objetivo é maximizar uma função troquei o sinal de '<' para '>' no escopo do IF
def selection(population,scores,k=2):
	selection_ix = np.random.randint(len(population))
	for ix in np.random.randint(len(population),size=k):
		if scores[ix] > scores[selection_ix]:
			selection_ix = ix
	return population[selection_ix]



def crossover(parent01,parent02,crossRate):
    children01 = parent01.copy()
    children02 = parent02.copy()
    if random() > crossRate:
        crossPoint = np.random.randint(len(parent01)-2,size=1)
        children01 = parent01[0][:crossPoint].tolist() + parent02[0][crossPoint:].tolist()
        children02 = parent02[0][:crossPoint].tolist()+ parent01[0][crossPoint:].tolist()
		

    return [children01, children02]



def mutation(cromossomo,mutationRate):
    for i in range(len(cromossomo)):
        if random() > mutationRate:
            cromossomo[i]=1-cromossomo[i]
    return 0 

def runGA(n_iter,population):

    cont = 0
    while(cont<n_iter):

        scores = [fitFunction(i) for i in population]

        parents = [selection(population,scores) for _ in range(population.shape[0])]

        




        cont=cont+1

    return solution