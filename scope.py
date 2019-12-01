import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1)
x = np.random.randn(10000)
axes[0].hist(x, bins=100)

y = np.random.rand(10000)
axes[1].hist(y, bins=100)

plt.show()
