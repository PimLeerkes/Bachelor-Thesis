import matplotlib.pyplot as plt
import numpy as np


n_values = np.linspace(0, 1, 100)
fn0_values = (1 - n_values) * n_values
fn1_values = (1 - n_values) * n_values**2
fn2_values = (1 - n_values) * n_values**3
fn3_values = (1 - n_values) * n_values**4

# Maak een plot)
plt.figure(figsize=(6, 5))
plt.plot(n_values, fn0_values, linestyle='-', color='b',label=r'$(1-x)x$')
plt.plot(n_values, fn1_values, linestyle='-', color='r',label=r'$(1-x)x^2$')
plt.plot(n_values, fn2_values, linestyle='-', color='g',label=r'$(1-x)x^3$')
plt.plot(n_values, fn3_values, linestyle='-', color='darkmagenta',label=r'$(1-x)x^4$')
plt.grid(True)
plt.xlabel("val")
plt.ylabel(r"$sol_{s_0}^{M_{\sigma}}(val)$")
plt.legend()

# Toon de plot
plt.show()
