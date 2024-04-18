import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2

x = np.linspace(-2*np.pi,2*np.pi,3000)
y = f(x)
print(y)
plt.plot(x,y)
plt.show()


