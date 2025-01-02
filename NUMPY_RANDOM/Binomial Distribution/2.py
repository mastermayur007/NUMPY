# Visualization of Binomial Distribution
# Visualization of Binomial Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a binomial distribution with n=10, p=0.5, and size=1000
data = random.binomial(n=10, p=0.5, size=1000)

# Create a histogram plot of the binomial distribution
sns.displot(data, kde=False, color='blue')

# Display the plot
plt.show()
