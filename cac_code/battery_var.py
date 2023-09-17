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

start='2023-08-20 22:21:00'

datetimes=use_df.time.tolist()
battery_list=[]
waste_list=[]
battery = 0.029383361
waste = 0

datetimes_before=datetimes[:datetimes.index(start)]
datetimes_after=datetimes[datetimes.index(start):]

for datetime in datetimes_before:
    
    battery += gen_df.loc[gen_df['time'] == datetime, 'gen_Sol'].iloc[0]
    battery -= use_df.loc[use_df['time'] == datetime, 'use_HO'].iloc[0]
    if battery<=0:
        waste+=abs(battery)

        battery=0
    waste_list.append(waste)
    battery_list.append(battery)

for datetime in datetimes_after:
    
    battery += gen_df.loc[gen_df['time'] == datetime, 'gen_Sol'].iloc[0]
    battery -= house.pred_cons(datetime)
    if battery<=0:
        waste+=abs(battery)

        battery=0
    waste_list.append(waste)
    battery_list.append(battery)


battery_df['battery'] = battery_list
battery_df['waste'] = waste_list
battery_df.to_csv('cac_code/csv_data/battery_data.csv',index=False)

""" today='2023-07-14 22:12:00'

battery=0
waste=0
x=0
battery_df['waste']=''
while x <= use_df.loc[use_df['time']==today].index.values[0]:
    battery+=gen_df.loc[x].gen_Sol
    battery-=use_df.loc[x].use_HO
    if battery<=0:
        waste+=battery
        battery=0

  
    battery_df.loc[x,'battery']=battery

    battery_df.loc[x, 'waste'] = round(waste,2)
    x+=1



while x >= use_df.loc[use_df['time']==today].index.values[0]:
    battery+=gen_df.loc[x].gen_Sol
    battery-=random.uniform(house.pred_cons(use_df.loc[x].time)-0.1, house.pred_cons(use_df.loc[x].time)+0.1)
    if battery<=0:
        waste+=battery
        battery=0

    battery_df.loc[x,'battery']=battery

    battery_df.loc[x, 'waste'] = round(waste,2)
    x+=1


battery_df.to_csv('csv_data/battery_data.csv',index=False) """