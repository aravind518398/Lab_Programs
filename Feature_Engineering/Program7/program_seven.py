import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(scale=2, size=1000)
print(data)
plt.hist(data, bins=50)
plt.show()