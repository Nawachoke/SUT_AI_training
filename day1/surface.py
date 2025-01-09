import numpy as np
import matplotlib.pyplot as plt

x3 = np.linspace(-5,5,100)
y3 = np.linspace(-5,5,100)
x3,y3 = np.meshgrid(x3, y3)

z = 1 + 2*x3 +3*y3

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(x3,y3,z)
plt.show()