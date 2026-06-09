import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data_box = np.random.randn(100, 5)
plt.boxplot(data_box)
plt.title('Boxplot')
plt.show()
