import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 3))

sns.scatterplot(x=[1, 2, 3, 4, 5], y=[2, 4, 6, 8, 10])
plt.xlim(0, 6) 
plt.ylim(0, 12)

plt.savefig('plot1.png')
plt.show()

plt.figure(figsize=(8, 3))

sns.scatterplot(x=[2, 1, 7, 4, 5], y=[2, 4, 6, 8, 10])
plt.xlim(0, 6)
plt.ylim(0, 12)

plt.savefig('plot2.png')
plt.show()

plt.figure(figsize=(3, 8))
df = sns.load_dataset("penguins")
sns.barplot(data=df, x="island", y="body_mass_g")

plt.savefig('plot3.png')
plt.show()

plt.figure(figsize=(3, 8))
df = sns.load_dataset("penguins")
sns.barplot(data=df, x="island", y="body_mass_g")

plt.savefig('plot4.png')
plt.show()
