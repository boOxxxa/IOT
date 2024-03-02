import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (np.sin(2*x)**2)*np.exp(((x+2)/10)**2)
x=np.linspace(-10,10,1000)
y=f(x)
plt.plot(x, y)

plt.figure(figsize=(8,3))
plt.grid(lw=0.5, ls='--')

plt.show()
plt.plot(x,y, lw = 4.0, #толщина линии
 color=(0.3,0.1,0.7))
