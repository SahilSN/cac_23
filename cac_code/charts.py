import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from cac_code import app
from cac_code.charts_class import generate_line,generate_pie
from datetime import datetime, timedelta
from cac_code.home_class import house

import warnings
warnings.filterwarnings("ignore")


df_use=house.use_df
df_gen=house.gen_df


#line-chart (consumption, generation, battery 12 hrs bfr and 12 after)
df_battery = pd.read_csv("cac_code/csv_data/battery_data.csv")




# Get relevant timestamps
dt_now = datetime.now()
before_12_hr = (dt_now - timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00' #second by second NOT in data
next_12_hr = (dt_now + timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
now = dt_now.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'

# Creates Main Line Graph
### Takes generated solar energy, consumption, and battery level
main_line_df = df_gen[["time", "gen_Sol"]]
main_line_df=main_line_df.rename(columns={"time": "Time", "gen_Sol": "Energy Generation"})
main_line_df["Energy Consumption"] = df_use["use_HO"]
main_line_df["Battery"] = df_battery["battery"].astype("float64")

### Filters results to past 12 hours
mask_before = (df_gen['time'] >= before_12_hr) & (df_gen['time'] <= now)
main_line_filter_df_before = main_line_df.loc[mask_before]

### time_list for next 12 hours
time_list=df_use['time'].values.tolist()

time_list=time_list[time_list.index(now):time_list.index(next_12_hr)]


###creating datafram for next 12 hours
#pred_cons=[]
#pred_gen=[]
#for time in time_list:
  #pred_cons.append(house.pred_cons(t))

pred_cons_list=[house.pred_cons(t) for t in time_list]
pred_gen_list=[house.pred_gen(t) for t in time_list]

from numpy import nan 
battery=[]
df_after=pd.DataFrame({
  'Time':time_list,
  'Energy Generation':pred_gen_list,
  'Energy Consumption':pred_cons_list,
})
df_after['Time']=df_after['Time'].astype(str)
df_after['Energy Generation']=df_after['Energy Generation'].astype(float)
df_after['Energy Consumption']=df_after['Energy Consumption'].astype(float)
df_after = df_after.assign(Battery = None)
#df_after['time']=time_list
#df_after['gen_Sol']=pred_gen
#df_after['use_HO']=pred_cons
#df_after['battery'] = battery
line_df=pd.concat([main_line_filter_df_before, df_after], axis=0)
print(line_df.info())
print(line_df)
### Generates line graph with the parameters
line = generate_line(line_df, 0, 1, None, "Energy Consumption, Generation, and Battery 12 Hours Before and After")

#pie chart (distribution of consumption by appliance last twelve hours)

