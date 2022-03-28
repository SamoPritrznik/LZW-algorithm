

def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    
    izhod = []

    if(nacin == 0): 
        izhod = encode(vhod)
        R = (len(izhod)*12)/(len(vhod)*8)
    elif(nacin == 1): 
        izhod = decode(vhod)
        R = ((len(vhod)+1)*12)/((len(izhod ) )*8)
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
            if(i < 409): 
                dict.update({i: (N+z)})
                i = i + 1
            N = z
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
