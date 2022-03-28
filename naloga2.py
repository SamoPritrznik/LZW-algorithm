#--------Glavna funkcija---------------------------------------------------------------------------------------------------------------------------------------------#

def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    
    izhod = []

    # Nacin 0 je kodiranje, nacin 1 pa dekodiranje. 

    if(nacin == 0): 
        izhod = encode(vhod)
        R = (len(izhod)*12)/(len(vhod)*8)
    elif(nacin == 1): 
        izhod = decode(vhod)
        R = ((len(vhod)+1)*12)/((len(izhod))*8)
    return (izhod, R)

#---------Kodiranje--------------------------------------------------------------------------------------------------------------------------------------------------#

def encode(vhod):
    izhod = []

    # Deklaracija slovarja znakov od 0 do 255.

    dict = {i: chr(i) for i in range(256)}
    N = ''
    i = 256

    # Zanka za sprehajanje po vhodu.

    for z in vhod:
        if((N+z) in dict.values()): N = N+z # V primeru da je N+z v slovarju, nastavimo da je vrednost N-ja enaka N+z.
        else: # V primeru da je ni, najdemo ključ znaka v slovarju in ga vpišemo v izhod, slovarju dodamo niz N+z, v primeru da slovar ni poln.
            key = [k for k, v in dict.items() if v == N][0]
            izhod.append(key)
            if(i < 4096): 
                dict.update({i: (N+z)})
                i = i + 1
            N = z # Nastavimo vrednosti N je z.
    key = [k for k, v in dict.items() if v == N][0]
    izhod.append(key)
    return izhod

#-----dekodiranje----------------------------------------------------------------------------------------------------------------------------------------------------#

def decode(vhod):
    izhod = []

    # Deklaracija slovarja znakov od 0 do 255.

    dict = {i: chr(i) for i in range(256)}
    i = 256

    # Spremenljivki k nastavimo vrednost prvega elementa vhoda (in ga odstranimo z vhoda), ter dodamo v izhod N, ki pa je element z ključom k.

    k = vhod.pop(0)
    N = dict.get(k)
    izhod.append(N)
    K = N

    # Zanka za sprehajanje po vhodu.

    for k in vhod:

        # V primeru, da je k v slovarju, potem nastavimo N vrednost elementa na ključu k.
        # V primeru, da k ni v slovarju, potem nastavimo N vrednost K plus prvi element K.

        if(k in dict): N = dict.get(k)
        else: N = K+K[0] 

        # Za vsak znak v N-ju, izpisemo imenovan znak na izhod.

        for l in N: izhod.append(l) 
        
        # Posodobimo slovar, tako da dodamo nov element K+N[0] z ključem i.

        dict.update({i: K+N[0]}) 
        i = i +1
        K = N

    return izhod

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#