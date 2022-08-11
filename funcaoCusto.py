import numpy as np
import allocacaoPotencia as ap

def dataRate(gamaUser,p_list,n_clusters):
    w =100
    B = 180*(10**3)
    N0 = 10**(-17.3)
    Pt = (10**4.6)*(10**-3)/n_clusters
    

    #### mudar a partir daqui (mudar primeiro essa função depois a próxima)
    num = p_list[index]*Pt*gamaUser

    p_list = p_list[index+1:]
    p_array = np.array(p_list)
    den_list = p_array*Pt*gamaUser

    den = np.sum(den_list)
    den = den+(w*N0*B)
    r = w*B*np.log2(1+(num/den))

    return r

def sumDataRate(cromossomo):

    alpha =0.3
    n_clusters = len(np.unique(cromossomo))

    gama = [] ### chamada de função de desvanecimento global 

    gamaClusters = []
    for i in np.unique(cromossomo):
        gamaClusters.append(gama[cromossomo==i].tolist())

    p_list =[ap.allocPower(i,alpha) for i in gamaClusters]
    

    data_rates=[]
    for ix, val in enumerate(gamaClusters):
        data_rates.append(dataRate(val,p_list[ix]),n_clusters)


####### alterar a partir daqui
    output = r_array[np.isfinite(r_array)]
    R_global = np.sum(output)

    return r_array,R_global