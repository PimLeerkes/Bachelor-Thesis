import numpy as np
import itertools
from collections import Counter

# Generate all binary string combinations of size n
def binary_combinations(n):
    binary_combinations = list(itertools.product([0, 1], repeat=n))
    return binary_combinations


# Generates the list of polynomials
def generate_coefs(bc):

    coefs = []
    for b in bc:
        print(b)
        coef = dict()
        #print(b)
        #For each binary string create the corresponging coefficients for the polynomial and add to the list
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

# Calculates all roots and returns them in a list
def generate_roots(coefs):
    roots = []
    for index,coef in enumerate(coefs):
        #print(list(np.roots(list(coef.values()))))
        roots += [list(np.roots(list(coef.values())))]
        print(len(coefs)-index)
    #print(roots)
    return roots

# Make sure all roots are between 0 and 1
def zero_one(roots):
    zero_one_roots = []
    for root in roots:
        for r in root:
            if r > 0 and r < 1:
                if r.imag == 0:
                    zero_one_roots.append(r)
    return zero_one_roots

# Count how many times a root is shared between two or more polynomials
def count_duplicates(roots):
    teller = Counter(roots)
    duplicaten = {element: count for element, count in teller.items() if count > 1}
    print(duplicaten)
    return len(duplicaten)


# genereer alle roots van afgeleiden van polynomen van type:
# (1-x)(b_1*x^1 + b_2*x^2 + ... + b_n*x^n) met b_i in {0,1}
n = 20
bc = binary_combinations(n)
coefs = generate_coefs(bc)
roots = generate_roots(coefs)
zero_one_roots = zero_one(roots)
print(zero_one_roots)
duplicates = count_duplicates(zero_one_roots)
print(duplicates)
