import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.random.randn(1000)
plt.hist(data, bins=20, alpha=0.7, color='green')
plt.title('Histogram')
plt.show()
