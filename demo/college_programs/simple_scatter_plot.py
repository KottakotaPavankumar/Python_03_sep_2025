import numpy as np
import matplotlib.pyplot as plt

plt.figure()
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.scatter(x_scatter, y_scatter, marker='o', color='blue')
plt.title('Simple Scatter Plot')
plt.show()
