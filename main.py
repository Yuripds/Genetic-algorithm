import geneticAlgorithm as ga
import funcaoCusto as fc
import numpy as np

# !pip install -U git+https://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@github.com/Yuripds/Coeficiente-de-desvanecimento-global.git@main
from coeficienteDesvanecimento_GlobalLib import coeficiente_desvanecimento



def desvanecimento_global_usuarios(qtd_usuarios):
  cg_obj = coeficiente_desvanecimento.Coeficiente_de_Desvanecimento()
  d=np.random.uniform(500,2000,qtd_usuarios)
  dGlobal=[]
  for i in range(qtd_usuarios):
    dGlobal.append(abs(cg_obj.desvanecimentoGlobal(d=d[i],LOS=False,NN=20,tamanho=10**3,seed=i,fc=2.0*(10**9))[0][0]))

  arr_dGlobal = np.array(dGlobal)
  return arr_dGlobal


#### param para gerar população
popSize =100
ngenes =50
tipo = 'real'
#### com vmax igual a 25 e quantidade de usuários igual a 50, teremos no minimo um grupo com 2 
vmax = 25

# inicializando população
populacao =  ga.population_generator(popSize,ngenes,tipo,vmax)

#### Ganho de canal
gama = desvanecimento_global_usuarios(ngenes)

#### Params do AG 
n_iter=100
population=populacao
crossRate =0.9
mutationRate=0.01
[best, best_eval] = ga.run(fc.sum_data_rate, n_iter, population, crossRate, mutationRate,gama)