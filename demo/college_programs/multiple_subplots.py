import numpy as np
import matplotlib.pyplot as plt

# Define data for plots
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Subplot 1')

plt.subplot(2, 2, 2)
plt.scatter(x_scatter, y_scatter)
plt.title('Subplot 2')
plt.show()