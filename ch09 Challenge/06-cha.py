import numpy as np
import matplotlib as plt

x = np.linspace(-np.pi * 2, np.pi * 2, 720)
cos, sin = np.cos(x), np.sin(x)

plt.plot(x, sin, ls=':', label='sin')
plt.plot(x, cos, ls='--', label='cos')

plt.title("Graph of sin cos")
plt.xlabel('radius')
plt.ylabel('value')
plt.grid()
plt.legend()
plt.show()