import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 1000)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig("test.png")
plt.show()