import geneticAlgorithm as ga
import numpy as np


#### fit function para o problema do NOMA ######
def dataRate(gamaUser,p_list,index):
    w =100
    B = 180*(10**3)
    N0 = 10**(-17.3)
    Pt = (10**4.6)*(10**-3)
    
    num = p_list[index]*Pt*gamaUser

    p_list = p_list[index+1:]
    p_array = np.array(p_list)
    den_list = p_array*Pt*gamaUser

    den = np.sum(den_list)
    den = den+(w*N0*B)
    r = w*B*np.log2(1+(num/den))

    return r

def sumDataRate(gamaL,alpha):

    p_list = allocPower(gamaL,alpha)
    print("p_list: ",p_list)
    
    r_array = np.ones((7,1))
    r_array[:] = float(np.NaN)
    
    for ind in range(len(gamaL)):
        gamaUser = gamaL[ind]
        r = dataRate(gamaUser,p_list,ind)
        r_array[ind] = r

    output = r_array[np.isfinite(r_array)]
    R_global = np.sum(output)

    return r_array,R_global



#### param para gerar população
popSize =50
ngenes =12
tipo = 'real'
#### com vmax igal a 6 e quantidade de usuários igual a 12, teremos no minimo um grupo com 2 
vmax = 6

# inicializando população
populacao =  ga.populationGenerator(popSize,ngenes,tipo,vmax)


#### Params do AG 
n_iter=100
population=populacao
crossRate =0.9
mutationRate=0.05
[best, best_eval] = ga.runGA(dataRate, n_iter, population, crossRate, mutationRate)