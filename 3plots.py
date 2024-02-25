import matplotlib.pyplot as plt
import numpy as np


n_values = np.linspace(0, 1, 100)
fn0_values = (1 - n_values)
fn1_values = n_values

# Maak een plot)
plt.figure(figsize=(6, 5))
plt.plot(n_values, fn0_values, linestyle='-', color='b',label=r'$1-x$')
plt.plot(n_values, fn1_values, linestyle='-', color='r',label=r'$x$')
plt.axhline(y=2/3, color='g', linestyle='-',label=r'$\frac{2}{3}$')
plt.grid(True)
plt.xlabel("val")
plt.ylabel(r"$sol_{s_0}^{M_{\sigma}}(val)$")
plt.legend()

# Toon de plot
plt.show()
