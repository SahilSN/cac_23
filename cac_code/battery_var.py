import pandas as pd
from datetime import datetime
from home_class import house
import random
#df=pd.Dataframe()
#df['time']=df_use['time']
#df.to_csv('../csv_data/battery_data.csv',index=False)

use_df=pd.read_csv('cac_code/csv_data/use_HO.csv')
gen_df=pd.read_csv('cac_code/csv_data/gen_sol.csv')
battery_df=pd.read_csv('cac_code/csv_data/battery_data.csv')
first='2023-08-20 21:21:00'
last='2023-08-20 23:21:00'
start='2023-08-20 22:21:00'

battery_df.waste=0.0
battery_df.battery=0.0
datetimes=use_df.time.tolist()
battery_list=[]
waste_list=[]
battery = 0.029383361
waste = 0

datetimes_before=datetimes[:datetimes.index(start)]
datetimes_after=datetimes[datetimes.index(start):]
#print(datetimes_before)
#print(datetimes_after)
for datetime in datetimes_before:
    print(datetime)
    battery += gen_df.loc[gen_df['time'] == datetime, 'gen_Sol'].iloc[0]
    battery -= use_df.loc[use_df['time'] == datetime, 'use_HO'].iloc[0]
    if battery<=0:
        waste+=abs(battery)

        battery=0
    waste_list.append(waste)
    battery_list.append(battery)

for datetime in datetimes_after:
    #print('afterr')
    print(datetime)
    battery += gen_df.loc[gen_df['time'] == datetime, 'gen_Sol'].iloc[0]
    battery -= random.uniform(house.pred_cons(datetime)[0]-0.1,house.pred_cons(datetime)[0]+0.1)
    if battery<=0:
        waste+=abs(battery)

        battery=0
    waste_list.append(waste)
    battery_list.append(battery)


battery_df['battery'] = battery_list
battery_df['waste'] = waste_list
#print(battery_list)
#print('\n\n\n')
#print(waste_list)
battery_df.to_csv('cac_code/csv_data/battery_data.csv',index=False)
