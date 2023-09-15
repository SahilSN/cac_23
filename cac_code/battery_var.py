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

today='2023-07-14 22:12:00'

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


battery_df.to_csv('csv_data/battery_data.csv',index=False)