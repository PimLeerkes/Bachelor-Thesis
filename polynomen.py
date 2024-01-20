import numpy as np
import itertools
from collections import Counter

n = 20

def binary_combinations(n):
    # Genereer alle binair combinaties van grootte n
    binary_combinations = list(itertools.product([0, 1], repeat=n))
    return binary_combinations


def generate_coefs(bc):
    # genereer alle roots van afgeleiden van polynomen van type:
    # (1-x)(b_1*x^1 + b_2*x^2 + ... + b_n*x^n) met b_i in {0,1}

    #we loopen door alle binary strings
    coefs = []
    for b in bc:
        print(b)
        coef = dict()
        #print(b)
        #voor elke binary string creeer de bijbehorende coefficienten van het polynoom
        #en voeg toe aan de lijst van polynomen
        for i in reversed(range(len(b)+1)):
            if i == 0:
                coef[i] = b[i]*(i+1)
            elif i == len(b):
                coef[i] = b[i-1]*-(i+1)
            else:
                if i in coef:
                    coef[i] += -b[i-1]*(i+1)+b[i] * (i+1)
                else:
                    coef[i] = -b[i-1]*(i+1)+b[i] * (i+1)
        #print(root)
        coefs += [coef]
    return coefs


def generate_roots(coefs):
    roots = []
    for index,coef in enumerate(coefs):
        #print(list(np.roots(list(coef.values()))))
        roots += [list(np.roots(list(coef.values())))]
        print(len(coefs)-index)
    #print(roots)
    return roots
   
def zero_one(roots):
    zero_one_roots = []
    for root in roots:
        for r in root:
            if r > 0 and r < 1:
                if r.imag == 0:
                    zero_one_roots.append(r)
    return zero_one_roots

def count_duplicates(roots):
    teller = Counter(roots)
    
    # Filter de elementen die meer dan 1 keer voorkomen
    duplicaten = {element: count for element, count in teller.items() if count > 1}
    print(duplicaten)
    return len(duplicaten)


bc = binary_combinations(n)
coefs = generate_coefs(bc)
roots = generate_roots(coefs)
zero_one_roots = zero_one(roots)
print(zero_one_roots)
duplicates = count_duplicates(zero_one_roots)
print(duplicates)
