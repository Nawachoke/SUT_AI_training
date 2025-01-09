import numpy as np
import matplotlib.pyplot as plt

data = np.array([[200,300,500,800,1000],
                 [100,200,350,500,600]])

coeff = np.polyfit(data[0], data[1], 1)
poly = np.poly1d(coeff)
x_line = np.linspace(min(data[0]), max(data[0]), 100)
y_line = poly(x_line)

plt.plot(x_line, y_line, color='r', label='best fit line')

plt.legend()
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('y')
plt.scatter(data[0], data[1])
plt.show()