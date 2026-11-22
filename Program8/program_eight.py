import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(scale=2, size=1000)
log_data = np.log(data)
print(log_data)
plt.figure(figsize=(10,8))
plt.hist(log_data,bins=50, label="log-transformed data".title(), facecolor="yellow", edgecolor="black")
plt.legend()
plt.show()