import pandas as pd
import numpy as np
df_use=pd.read_csv('csv_data/use_HO.csv',low_memory=False)
df_gen=pd.read_csv('csv_data/gen_sol.csv',low_memory=False)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=4, ncols=1)

def ahh(monthday,df_use,df_gen):
    df_use["monthdate"]=[str(i[5:10]) for i in df_use.time.tolist()]


    df_use=df_use.loc[df_use['monthdate'] == monthday]
    df_use = df_use.reset_index(drop=True)
    use_list=[]

    use_list=[]
    for i in np.array_split(df_use,24):
        counter=0
        for j in i.use_HO:
            counter+=j
        use_list.append(counter)

    hour_list=[]
    for i in range(len(use_list)):
        hour_list.append(i)






    df_gen["monthdate"]=[str(i[5:10]) for i in df_gen.time.tolist()]


    df_gen=df_gen.loc[df_gen['monthdate'] == monthday]
    df_gen = df_gen.reset_index(drop=True)
    gen_list=[]

    for i in np.array_split(df_gen,24):
        counter=0
        for j in i.gen_Sol:
            counter+=j
        gen_list.append(counter)

    axes[0].plot(hour_list, use_list)
    axes[0].set_title('uses')
    axes[1].plot(hour_list, gen_list)
    axes[1].set_title('gens')

    return gen_list,use_list

super_gen_list=[]
super_use_list=[]
#print(df_use['time'])
thing = [i[5:10] for i in df_use['time']]
from collections import OrderedDict
thing = list(OrderedDict.fromkeys(thing))

#print(thing)
for i in thing:


    #print(i)
    gen_list,use_list=ahh(i,df_use,df_gen)
    super_gen_list.append(gen_list)
    super_use_list.append(use_list)

add_use_list = list()
for j in range(0, len(super_use_list[0])):
    tmp = 0
    for i in range(0, len(super_use_list)):
        tmp = tmp + super_use_list[i][j]
    add_use_list.append(tmp)
add_gen_list = list()
for j in range(0, len(super_gen_list[0])):
    tmp = 0
    for i in range(0, len(super_gen_list)):
        tmp = tmp + super_gen_list[i][j]
    add_gen_list.append(tmp)

add_use_list = list(map(lambda x: x / len(super_use_list), add_use_list))
add_gen_list = list(map(lambda x: x / len(super_gen_list), add_gen_list))
print(add_use_list)
print(add_gen_list)
print(len(super_use_list))
print(len(super_gen_list))





hour_list=[]
for i in range(len(add_gen_list)):
    hour_list.append(i)
print(hour_list)
import matplotlib.pyplot as plt
x=hour_list
y1=add_use_list
y2=add_gen_list
axes[2].plot(x, y1, label="use")
axes[2].plot(x, y2, label="gen")
axes[2].set_title('averages')



plt.legend()
# Add a legend
plt.show()


