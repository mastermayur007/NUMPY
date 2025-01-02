from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=2,size=1000),kde=True)
plt.show()