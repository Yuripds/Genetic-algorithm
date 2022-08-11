import numpy as np
import allocacaoPotencia as ap

def dataRate(gamaUser,p_list,n_clusters):
    w =100
    B = 180*(10**3)
    N0 = 10**(-17.3)
    Pt = (10**4.6)*(10**-3)/n_clusters
    
    # ordenados na ordem crescente
    zipped_pairs = zip(gamaUser, p_list)
    plistSorted = [x for _, x in sorted(zipped_pairs)]
    gamaUserSorted = [_ for _, x in sorted(zipped_pairs)]

    r=[]
    for idx in range(len(gamaUserSorted)):
        num = plistSorted[idx]*Pt*gamaUserSorted[idx]

        plist_rest = plistSorted[idx+1:]
        p_array = np.array(plist_rest)
        den_list = p_array*Pt*gamaUserSorted[idx+1:]

        den = np.sum(den_list)
        den = den+(w*N0*B)


        r.append(w*B*np.log2(1+(num/den)))

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
        data_rates.append(dataRate(val,p_list[ix],n_clusters))

    R_global = []
    for m in data_rates:
        R_global.append(sum(m))

    return sum(R_global)