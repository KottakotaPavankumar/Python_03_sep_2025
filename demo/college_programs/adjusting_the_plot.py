import numpy as np
import matplotlib.pyplot as plt

# Define the data
x = np.linspace(0, 10, 500)
y = np.sin(x)

plt.figure()
plt.plot(x, y, color='red', linestyle='dashed', linewidth=2, label='sin(x)')
plt.xlim(0, 10)
plt.ylim(-1, 1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Adjusted Plot')
plt.legend()
plt.show()