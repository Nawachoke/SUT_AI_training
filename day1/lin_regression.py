import numpy as np
import matplotlib.pyplot as plt

data = np.array([[200,300,500,800,1000],
                 [100,200,350,500,600]])


plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('y')
plt.scatter(data[0], data[1])
plt.show()