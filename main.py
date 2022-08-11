import geneticAlgorithm as ga
import funcaoCusto as fc


#### param para gerar população
popSize =50
ngenes =50
tipo = 'real'
#### com vmax igual a 25 e quantidade de usuários igual a 50, teremos no minimo um grupo com 2 
vmax = 25

# inicializando população
populacao =  ga.populationGenerator(popSize,ngenes,tipo,vmax)


#### Params do AG 
n_iter=100
population=populacao
crossRate =0.9
mutationRate=0.05
[best, best_eval] = ga.runGA(fc.sumDataRate, n_iter, population, crossRate, mutationRate)