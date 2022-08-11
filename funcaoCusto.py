import numpy as np
import allocacaoPotencia as ap

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