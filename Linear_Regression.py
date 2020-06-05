# Author: Nikhil .V. Pachkor
#Linear Regression Python
import random
import numpy as np
import matplotlib.pyplot as plt
x = list(range(0, 100, 1))
y = list(2 * x[i] + 4 + random.randrange(1, 10) for i in range(len(x)))
p = np.polyfit(x, y, 1)
ynew = np.polyval(p, x)
t = np.subtract(ynew, y)
mse = sum(np.power(t, 2)) / len(y)
plt.plot(x, y, 'x', label='original')
plt.plot(x, ynew, 'g', label='predicted')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear regression')
plt.legend()
plt.show()
