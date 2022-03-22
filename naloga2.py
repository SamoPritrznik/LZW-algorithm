

def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    """
    Izvedemo kodiranje ali dekodiranje z algoritmom LZW.
    Zacetni slovar vsebuje vse 8-bitne vrednosti (0-255). 
    Najvecja dolzina slovarja je 4096.

    Parameters
    ----------
    vhod : list
        Seznam vhodnih znakov: bodisi znaki abecede
        (ko kodiramo) bodisi kodne zamenjave 
        (ko dekodiramo).
    nacin : int 
        Stevilo, ki doloca nacin delovanja: 
            0: kodiramo ali
            1: dekodiramo.

    Returns
    -------
    (izhod, R) : tuple[list, float]
        izhod : list
            Ce je nacin = 0: "izhod" je kodiran "vhod"
            Ce je nacin = 1: "izhod" je dekodiran "vhod"
        R : float
            Kompresijsko razmerje
    """

    izhod = []

    if(nacin == 0): 
        izhod = encode(vhod)
        R = (len(izhod)*12)/(len(vhod)*8)
    elif(nacin == 1): 
        izhod = decode(vhod)
        R = round((len(vhod)*12)/(len(izhod)*8), 5)
     
    return (izhod, R)

def encode(vhod):
    izhod = []
    dict = {i: chr(i) for i in range(256)}
    N = ''
    i = 256
    for z in vhod:
        if(i == 4096): break
        if((N+z) in dict.values()): N = N+z
        else:
            key = [k for k, v in dict.items() if v == N][0]
            izhod.append(key)
            dict.update({i: (N+z)})
            N = z
            i = i + 1
    key = [k for k, v in dict.items() if v == N][0]
    izhod.append(key)
    return izhod

def decode(vhod):
    izhod = []
    dict = {i: chr(i) for i in range(256)}
    k = vhod.pop(0)
    N = dict.get(k)
    izhod.append(N)
    K = N
    i = 256

    for a in vhod:
        k = a
        if(k in dict): N = dict.get(k)
        else: N = K+K[0]
        for l in N: izhod.append(l)
        dict.update({i: K+N[0]})
        i = i +1
        K = N

    return izhod
