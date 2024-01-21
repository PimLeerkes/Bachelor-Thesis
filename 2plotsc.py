import matplotlib.pyplot as plt
import numpy as np


n_values = np.linspace(0, 1, 100)
fn0_values = ((16/729)/(4/27))*(1 - n_values) * n_values**2
fn1_values = (1 - n_values)**2 * n_values**4

# Maak een plot)
plt.figure(figsize=(6.3, 5.3))
plt.plot(n_values, fn0_values, linestyle='-', color='b',label=r'$\frac{\frac{16}{729}}{\frac{4}{27}}(1-x)x^2$')
plt.plot(n_values, fn1_values, linestyle='-', color='r',label=r'$(1-x)^2x^4$')
plt.grid(True)
plt.xlabel("val")
plt.ylabel(r"$sol_{s_0}^{M_{\sigma}}(val)$")
plt.legend()

# Toon de plot
plt.show()
