import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from home_class import house
from io import BytesIO
import numpy as np
import datetime as dt
now=dt.datetime.now().replace(microsecond=0).replace(second=0)
dates_before=[]
dates_after=[]
for i in range(13):
    time_before = now - dt.timedelta(hours=i)
    dates_before.append(str(time_before))
    time_after=now + dt.timedelta(hours=i)
    dates_after.append(str(time_after))
print(dates_before)
print(dates_after)

data_before=[[house.act_cons(i)[0],house.act_gen(i)[0],i] for i in dates_before]
data_after=[[house.act_cons(i)[0],house.act_gen(i)[0],i] for i in dates_after]
print(data_before)
print(data_after)

fig, ax = plt.subplots(1, 2, sharex=False, figsize=(8, 3))

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

main_plt=plt
main_plt.savefig('static/images/line_chart2.png')

