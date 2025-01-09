import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y = 5 + 4*x

y2 = 5 + 3*x - 7*x**2 + 5*x**3



titles = ['linear eq', 'polynomial']

p1 = [-6,-3]
p2 = [8,7]

def findM(p1, p2):
    m =  np.abs(p1[1]-p2[0]) / np.abs(p1[0]-p2[0])
    return m

m = findM(p1,p2)
c = p1[1] - m*p1[0]
xq = np.linspace(-6,8,100)
yq = c+m*xq

plt.xlabel('x')
plt.ylabel('y')
plt.subplot(1,3,1)
plt.title(titles[0])
plt.plot(x,y)
plt.subplot(1,3,2)
plt.title(titles[1])
plt.plot(x,y2)
plt.subplot(1,3,3)
plt.title('quiz')
plt.plot(xq, yq)
plt.show()