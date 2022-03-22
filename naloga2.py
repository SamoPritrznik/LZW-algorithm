

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
        R = (len(vhod)*12)/(len(izhod)*8)

    
     
    return (izhod, R)

def encode(vhod):
    izhod = []
    dict = {i: chr(i) for i in range(256)}
    N = ''
    i = 256
    for z in vhod:
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
    return 0
