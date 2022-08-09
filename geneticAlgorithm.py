import numpy as np


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

def selection(population,scores):


    return parents


def runGA(n_iter,population):

    cont = 0
    while(cont<n_iter):

        scores = [fitFunction(i) for i in population]

        parents = [selection(population,scores) for _ in range(population.shape[0])]

        




        cont=cont+1

    return solution