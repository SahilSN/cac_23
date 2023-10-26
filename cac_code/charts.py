import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
#from app import app
from charts_class import generate_line,generate_bar,generate_pie,generate_heatmap
from datetime import datetime as dt, timedelta
from home_class import house
import random
import warnings
warnings.filterwarnings("ignore")

now = dt.now().replace(microsecond=0).replace(second=0)

df_use=house.use_df
df_gen=house.gen_df


#line-chart (consumption, generation, battery 12 hrs bfr and 12 after)
df_battery = pd.read_csv("cac_code/csv_data/battery_data.csv",)

#df_battery["battery"]=df_battery["battery"].astype(float)
# Creates Main Line Graph
main_line_df = df_gen[["time", "gen_Sol"]]
main_line_df=main_line_df.rename(columns={"time": "Time", "gen_Sol": "Energy Generation"})
main_line_df["Energy Consumption"] = df_use["use_HO"]
main_line_df["battery"] = df_battery["battery"]
#print(main_line_df.info())
#print(main_line_df)
### Filters results to past 12 hours
#(df_gen['time'] >= before_12_hr) & (df_gen['time'] <= now)
main_line_filter_df_before = main_line_df.loc[house.last_12(now,True)]

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
df_after = df_after.assign(battery = None)
line_df=pd.concat([main_line_filter_df_before, df_after], axis=0)
line_df=line_df.drop(columns=["battery"])
### Generates line graph with the parameters
main_line = generate_line(line_df, 0, 1, None, 
                          "Energy Consumption, Generation, and Battery 12 Hours Before and After",
                          ["#7DA1FB","#7DFB89"]
                        )

#pie chart (distribution of consumption by appliance last twelve hours)
appliance_list=['Home office','Fridge','Wine cellar', 'Garage door','Microwave','Living room']
app_df=house.use_df.drop(columns=['apparentTemperature','month','day','hour','use_HO'])
app_df = app_df.loc[house.last_12(now,True)]
app_df=app_df.drop(columns=['time'])

value_list=[]


for column in app_df:
  value_list.append(app_df[column].sum())
#print(value_list)
d={
    'appliance':appliance_list,
    'values':value_list
    }
pie_df=pd.DataFrame(data=d)

colors=['#7DFB89','#7DFBD7','#7DE0FB','#7DA1FB','#987DFB','#D77DFB']

pie = generate_pie(pie_df,colors)

bad_rec_dict,good_rec_dict,avg=house.last_24_effiencies(now)
#DO NOT TOUCH the () and [] around the percentage values; they are used in jinja (html) for coloring the percentages
bad_statements=[
  lambda i,j:"You used {} [{}%] more than average, remember to turn off lights or running appliances.".format(i,j),
  lambda i,j:"You used {} [{}%] more than yesterday, try to limit your energy consumption.".format(i,j),
  lambda i,j:"Next time, try to limit your consumption for the {}, you used it [{}%] more than normal.".format(i,j)
]
good_statements=[
  lambda i,j:"Great job, you used {} ({}%) less than average.".format(i,j),
  lambda i,j:"Nice! you used {} ({}%) less than last week.".format(i,j),
  lambda i,j:"Keep up the good work! {} was used ({}%) less than normal.".format(i,j)
]
rec_list=[]
for i in bad_rec_dict:
  try:
    rec_list.append(bad_statements.pop(0)(i,bad_rec_dict[i]))
  except:
    print('not enough bad recommendation options')
for i in good_rec_dict:
  try:
    rec_list.append(good_statements.pop(0)(i,abs(good_rec_dict[i])))
  except:
    print('not enough good recommendation options')


## second optimization chart
use_list=df_use[['time',"Home office","Fridge","Wine cellar","Garage door","Microwave","Living room"]]
use_list=use_list.loc[house.last_12(now,True)]
#(print(use_list)
cons_over_time=generate_line(use_list,0,1,None,"Consumption Over Last Twelve Hours",
              ['#7DFB89','#7DFBD7','#7DE0FB','#7DA1FB','#987DFB','#D77DFB'],[0,0.5])




##correleation heatmap
df_corr=df_gen.drop(columns=['time'])
df_matrix=df_corr.corr()
colors=[[0,"rgba(125,251,137,255)"],[0.5,'white'],[1.0,"rgba(125,224,251,255)"]]
corr_heatmap=generate_heatmap(df_matrix,colors)

## Predicted savings line
print("hello")
df_savings=df_use.loc[house.next_days(7,True)][["time","use_HO"]]
df_savings["use_HO_save"] = df_savings["use_HO"]*0.92
df_savings_sum=df_savings.loc[::60] # gets every hour

for time in df_savings_sum["time"]: # iterates through each hour and appends the sum of usage to the df_savings_sum
  mask = house.next_hour(time,True)
  df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO"] = df_savings.loc[mask]["use_HO"].sum()
  df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO_save"] = df_savings.loc[mask]["use_HO_save"].sum()

compare_bar=generate_bar(df_savings_sum,0,1,None,"Predicted energy saved Comparison")

### Code for bar graph over time of predicted energy saved
# df_savings_dif = df_savings_sum[["time","use_HO"]]
# df_savings_dif["use_HO"] = df_savings_sum["use_HO"]-df_savings_sum["use_HO_save"]
# savings_bar=generate_bar(df_savings_dif,0,1,None,"Predicted energy saved")
