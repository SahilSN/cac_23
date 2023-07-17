import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2, sharex=False, figsize=(10, 4))

fig.suptitle('Graphs thing')

data = [[10, 12, 13], [5, 2, 6], [13, 9, 3], [12, 5, 6], [16, 13, 9], [4, 19, 2], [10, 12, 13], [5, 2, 6], [13, 9, 3], [12, 5, 6], [16, 13, 9], [4, 19, 2], ]
data2 = [[10, 12, 13], [5, 2, 6], [13, 9, 3], [12, 5, 6], [16, 13, 9], [4, 19, 2], [10, 12, 13], [5, 2, 6], [13, 9, 3], [12, 5, 6], [16, 13, 9], [4, 19, 2], ]

df = pd.DataFrame(data=data, columns=['consumption', 'battery input', 'battery output'])
df2 = pd.DataFrame(data=data2, columns=['consumption', 'battery input', 'battery output'])

a = sns.lineplot(data=df, ax=ax[0], palette=['blue', 'green', 'red'])
b = sns.lineplot(data=df2, ax=ax[1], palette=['blue', 'green', 'red'], linestyle=None, legend=False)
b.tick_params(labelleft = False, left=False)

lines_left = ax[0].get_lines()
for line in lines_left:
    line.set_linestyle('-')

lines_right = ax[1].get_lines()
lines_right[0].set_linestyle('-')
lines_right[1].set_linestyle('-')
lines_right[2].set_linestyle('--') 

plt.subplots_adjust(wspace=0, hspace=0)
a.invert_xaxis()

plt.show()
