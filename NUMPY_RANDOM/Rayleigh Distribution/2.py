import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns

sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()