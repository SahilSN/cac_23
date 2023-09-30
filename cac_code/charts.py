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

# Creates Main Line Graph
main_line_df = df_gen[["time", "gen_Sol"]]
main_line_df=main_line_df.rename(columns={"time": "Time", "gen_Sol": "Energy Generation"})
main_line_df["Energy Consumption"] = df_use["use_HO"]
main_line_df["Battery"] = df_battery["battery"].astype("float64")

### Filters results to past 12 hours
#(df_gen['time'] >= before_12_hr) & (df_gen['time'] <= now)
main_line_filter_df_before = main_line_df.loc[house.last_12(True)]

### time_list for next 12 hours
time_list=house.next_12()
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
line_df=pd.concat([main_line_filter_df_before, df_after], axis=0)

### Generates line graph with the parameters
line = generate_line(line_df, 0, 1, None, "Energy Consumption, Generation, and Battery 12 Hours Before and After")

#pie chart (distribution of consumption by appliance last twelve hours)
appliance_list=['Home Office','Fridge','Wine Cellar', 'Garage Door','Microwave','Living Room']
app_df=house.use_df.drop(columns=['apparentTemperature','month','day','hour','use_HO'])
app_df = app_df.loc[house.last_12(True)]
app_df=app_df.drop(columns=['time'])
value_list=[]


for column in app_df:
  value_list.append(app_df[column].sum())
print(value_list)
d={
    'appliance':appliance_list,
    'values':value_list
    }
pie_df=pd.DataFrame(data=d)
pie = generate_pie(pie_df, "pie")


