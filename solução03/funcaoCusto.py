import numpy as np
import allocacaoPotencia as ap

def data_rate(gama_user,p_list,n_clusters):
    w =100
    B = 180*(10**3)
    N0 = 10**(-17.3)
    pt = (10**4.6)*(10**-3)/n_clusters
    
    ############# mudar as coisas a partir daqui #################
    # ordenados na ordem crescente
    zipped_pairs = zip(gama_user, p_list)
    plist_sorted = [x for _, x in sorted(zipped_pairs)]
    gama_user_sorted = sorted(gama_user)

    r=[]
    for idx in range(len(gama_user_sorted)):
        num = plist_sorted[idx]*pt*gama_user_sorted[idx]

        plist_rest = plist_sorted[idx+1:]
        p_array = np.array(plist_rest)
        den_list = p_array*pt*gama_user_sorted[idx+1:]

        den = np.sum(den_list)
        den = den+(w*N0*B)


        r.append(w*B*np.log2(1+(num/den)))

    return r



def sum_data_rate(cromossomo_01,cromossomo_02,gama):

    
    n_clusters = len(np.unique(cromossomo_01))


    gama_clusters = []
    potencia_users =[]
    for i in np.unique(cromossomo_01):
        gama_clusters.append(gama[cromossomo_01==i].tolist())
        potencia_users.append(cromossomo_02[cromossomo_01==i].tolist())


    data_rates=[]
    for ix, val in enumerate(gama_clusters):
        data_rates.append(data_rate(val,potencia_users[ix],n_clusters))

    r_global = []
    for m in data_rates:
        r_global.append(sum(m))

    return sum(r_global)