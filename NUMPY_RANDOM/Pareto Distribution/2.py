import matplotlib.pyplot as plt

from numpy import random

import seaborn as sns

sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()