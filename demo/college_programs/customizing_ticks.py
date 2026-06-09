import numpy as np
import matplotlib.pyplot as plt

# Define data for the plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.xticks(np.arange(0, 11, step=2))
plt.yticks(np.arange(-1, 1.5, step=0.5))
plt.title('Customized Ticks')
plt.show()