import numpy as np
from random import randint
from random import random


def population_generator(popSize, ngenes, tipo, vmax=5):

    if tipo == 'bin':
        population = np.random.randint(2, size=(popSize, ngenes))
    else:
        population = np.random.randint(vmax, size=(popSize, ngenes))

    return population

# como meu objetivo é maximizar uma função troquei o sinal de '<' para '>' no escopo do IF
def selection(population, scores, k=2):
	selection_ix = np.random.randint(len(population))
	for ix in np.random.randint(len(population), size=k):
		if scores[ix] > scores[selection_ix]:
			selection_ix = ix
	return population[selection_ix]


def crossover(parent01, parent02, cross_rate):
    children01 = parent01.copy()
    children02 = parent02.copy()
    if random() > cross_rate:
        cross_point = abs(np.random.randint(len(parent01)-2, size=1)[0])
        children01 = parent01[:cross_point]+ parent02[cross_point:]
        children02 = parent02[:cross_point] + parent01[cross_point:]

    return [children01, children02]


def mutation(cromossomo, mutationRate):
    for i in range(len(cromossomo)):
        if random() > mutationRate:
            cromossomo[i] = abs(cromossomo[i]-1)
    return 0


def run(fitFunction, n_iter, population, crossRate, mutationRate,gama):

    cont = 0
    best = 0
    best_eval = fitFunction(population[0],gama)
    population = population.tolist()

    while (cont < n_iter):
	
        scores = [fitFunction(i,gama) for i in population]
        for i in range(len(population)):
            if scores[i] > best_eval:
                best, best_eval = population[i], scores[i]
                print(">%d, new best f(%s) = %.3f" % (cont ,  population[i], scores[i]))
        
        parents = [selection(population,scores) for _ in range(len(population))]

        # criandao a nova geração
        children = []
        for i in range(0, len(population), 2):
            parent01,parent02 = parents[i], parents[i+1]
            for c in crossover(parent01, parent02, crossRate):
                mutation(c, mutationRate)
                children.append(c)
        
        # subistitui população (estou na duvida se esse é o melhor metodo)
        population = children


        cont=cont+1

    return [best, best_eval]