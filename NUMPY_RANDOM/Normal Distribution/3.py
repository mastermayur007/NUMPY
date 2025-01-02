from numpy import random
import seaborn as sns

import matplotlib.pyplot as plt

sns.distplot(random.normal(size=1000),hist=False)
plt.show()