import numpy as np
import matplotlib.pyplot as plt

# Define data for the plot
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.text(2, 0.5, 'Annotation', fontsize=12, color='red')
plt.title('Text and Annotation')
plt.show()
