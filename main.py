import geneticAlgorithm as ga

popSize =100
ngenes =12
tipo = 'bin'


# inicializando população
populacao =  ga.populationGenerator(popSize,ngenes,tipo)


n_iter=100
population=populacao
crossRate =0.6
mutationRate=0.6
[best, best_eval] = ga.runGA(ga.fitFunction, n_iter, population, crossRate, mutationRate)