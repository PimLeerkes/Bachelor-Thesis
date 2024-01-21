import matplotlib.pyplot as plt
from sympy.ntheory.factor_ import totient
import numpy as np

#we count for the first 100 f(n)'s
for n in range(1, 100):
    total = 0
    for i in range(2, n+1):
        total += totient(i)
    print(f"f({n}) = {total}")

# Initialiseer lege lijsten om de waarden van n en f(n) op te slaan
n_values = []
fn_values = []

# We tellen de eerste 100 f(n)'s
total = 0
for n in range(1, 100):
    total += totient(n)
    n_values.append(n)
    fn_values.append(total)

# Maak een plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, fn_values, marker='o', linestyle='-', color='b')
plt.ylabel(r"$\Sigma_{i=2}^n\varphi(i)$")
plt.xlabel(r"$n$")
plt.grid(True)

# Toon de plot
plt.show()
