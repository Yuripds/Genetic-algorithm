def alloc_power(gamaL,alpha):
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[0])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[0])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list
