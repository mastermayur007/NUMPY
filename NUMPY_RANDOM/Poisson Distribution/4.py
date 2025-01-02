from numpy import random

import seaborn as sns

import matplotlib.pyplot as plt

sns.distplot(random.binomial(n=1000,p=0.01,size=1000),hist=False,label="binomial")
sns.distplot(random.poisson(lam=10,size=1000),hist=False,label="poisson")
plt.show()