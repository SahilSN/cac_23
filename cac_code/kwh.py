import pandas as pd
from home_class import house
from charts_class import generate_line

df_use=house.use_df
df_gen=house.gen_df
df_use['time']= pd.to_datetime(df_use['time'])
df_use['gen_Sol']=df_gen['gen_Sol']
g = df_use.groupby(pd.Grouper(key='time', freq='M'))

dfs = [group.filter(['time','use_HO','gen_Sol'], axis=1) for _,group in g]

use=[]
gen=[]
months=[]

for i in dfs:
  i['time']=i['time'].astype(str)
  df_savings_sum=i.loc[::60] # gets every hour

  for time in df_savings_sum["time"]: # iterates through each hour and appends the sum of usage to the df_savings_sum
    mask = house.next_hour(time,True)
    df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO"] = i.loc[mask]["use_HO"].sum()
    df_savings_sum.loc[df_savings_sum["time"]==time,"gen_Sol"] = i.loc[mask]["gen_Sol"].sum()
  
  month=i.iloc[0]["time"][5:7]
  months.append(int(month))
  use.append(df_savings_sum["use_HO"].sum())
  gen.append(df_savings_sum["gen_Sol"].sum())

line_df=pd.DataFrame(data={
  'month':months,
  'use_kwh':use,
  'gen_kwh':gen,
})
main_line = generate_line(line_df, 0, 1, None, 
                          "KwH per month",
                          ["#7DA1FB","#7DFB89"]
                        )


