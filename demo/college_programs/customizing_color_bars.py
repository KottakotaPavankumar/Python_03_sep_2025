import numpy as np
import matplotlib.pyplot as plt

plt.figure()
x_mesh, y_mesh = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
z_mesh = np.sin(np.sqrt(x_mesh ** 2 + y_mesh ** 2))
plt.pcolormesh(x_mesh, y_mesh, z_mesh, cmap='viridis')
plt.colorbar()
plt.title('Customized Color Bar')
plt.show()
