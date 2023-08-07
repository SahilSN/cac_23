import pandas as pd
from datetime import datetime
#df=pd.Dataframe()
#df['time']=df_use['time']
#df.to_csv('../csv_data/battery_data.csv',index=False)

use_df=pd.read_csv('csv_data/use_HO.csv')
gen_df=pd.read_csv('csv_data/gen_sol.csv')
battery_df=pd.read_csv('csv_data/battery_data.csv')


today=datetime.now()
today=today.replace(microsecond=0).replace(second=0).strftime('%Y-%m-%d %H:%M:%S')
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

    print('battery: '+str(battery))
    print('waste: '+str(waste))
    battery_df.loc[x,'battery']=battery

    battery_df.loc[x, 'waste'] = round(waste,2)
    x+=1

print(battery_df.loc[300000])
battery_df.to_csv('csv_data/battery_data.csv',index=False)