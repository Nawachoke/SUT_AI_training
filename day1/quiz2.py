import numpy as np
import matplotlib.pyplot as plt

data = np.array([51, 47, 45, 42.5, 41, 38])

def simplePredcition(data, end_point):
    coeff = np.polyfit(np.arange(len(data)) ,data, 1)
    poly = np.poly1d(coeff)
    x_line = np.linspace(0, end_point, 8)
    y_line = poly(x_line)
    # print(y_line[-1]*1000)
    plt.scatter(x_line[-1], y_line[-1] )
    plt.plot(x_line, y_line, color='r', label='best fit line')
    plt.legend()
    plt.title('Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.scatter(np.arange(len(data)), data)
    plt.show()

simplePredcition(data, 8)