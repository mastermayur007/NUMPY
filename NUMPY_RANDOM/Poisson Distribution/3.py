from numpy import random

import seaborn as sns

import matplotlib.pyplot as plt

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50,size=1000),hist=False,label="poisson")
plt.show()