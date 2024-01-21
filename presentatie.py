import matplotlib.pyplot as plt
import numpy as np


n_values = np.linspace(-1, 2, 200)
fn0_values = n_values**2
fn1_values = n_values*(5/6)

# Maak een plot)
plt.figure(figsize=(6, 5))
plt.plot(n_values, fn0_values, linestyle='-', color='b',label=r'$x^2$')
plt.plot(n_values, fn1_values, linestyle='-', color='r',label=r'$\frac{5}{6}x$')
plt.axhline(y=25/36, xmin=0.0, xmax=1.0, color='g', linestyle='-',label=r'$\frac{25}{36}$')
plt.grid(True)
plt.xlabel("val")
plt.ylabel(r"$sol_{s_0}^{M_{\sigma}}(val)$")
plt.legend()

# Toon de plot
plt.show()
