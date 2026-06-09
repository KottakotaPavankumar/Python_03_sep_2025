
import numpy as np
import matplotlib.pyplot as plt

x, y1, y2 = [1, 2, 3, 4, 5], [1, 4, 1, 3, 1], [1, 2, 1, 2, 1]
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.legend(title='Legend', loc='upper left', fontsize='small')
plt.title('Customized Legend')
plt.xlabel('X-axis'), plt.ylabel('Y-axis')
plt.show()
