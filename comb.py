from kaijo import *

def comb(n,k):
    return int(kaijo(n)/kaijo(n-k)/kaijo(k))

print(comb(8,4))