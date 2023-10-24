from home_class import house
from datetime import timedelta
df_use=house.use_df
df_gen=house.gen_df
print(df_use.time)
now=house.datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
last_hour = (house.datetime - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
datetimes=df_use.time.values.tolist()
x=datetimes.index(now)
y=x
while x < len(datetimes):
  if datetimes[x][-8:]=='12:00:00':
    break
  x-=1
y=datetimes.index(now)

period=datetimes[x:y]
#print(period)
"""
total_generated=0
total_consumed=0
battery_left=0
generation_efficiency=0
 
for datetime in period:
  total_generated += house.act_gen(datetime)[0]
  total_consumed += house.act_cons(datetime)[0]
  generation_efficiency=((house.act_gen(datetime)/house.pred_gen(datetime))*100)[0]
hour_avg=((total_consumed)/len(period))*60

total_generated=round(total_generated)
total_consumed=round(total_consumed)
generation_efficiency=round(generation_efficiency)
hour_avg=round(hour_avg)
"""

### Note: Same processing as in charts.py -- is there a way to make this more efficient?
## Predicted savings line
print("hello")
df_savings=df_use.loc[house.next_days(7,True)][["time","use_HO"]]
df_savings["use_HO_save"] = df_savings["use_HO"]*0.92
df_savings_sum=df_savings.loc[::60] # gets every hour

for time in df_savings_sum["time"]: # iterates through each hour and appends the sum of usage to the df_savings_sum
  mask = house.next_hour(time,True)
  df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO"] = df_savings.loc[mask]["use_HO"].sum()
  df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO_save"] = df_savings.loc[mask]["use_HO_save"].sum()

# finds dif between the estimated energy usage of user (based on the trend of base house) and the energy saved if using product
df_savings_dif=df_savings_sum["use_HO"]-df_savings_sum["use_HO_save"] 
est_energy_savings = df_savings_dif.sum()

## Data: https://css.umich.edu/publications/factsheets/sustainability-indicators/carbon-footprint-factsheet
## Data: https://www.usda.gov/media/blog/2015/03/17/power-one-tree-very-air-we-breathe

# 0.857 lbs CO2e per 1 kWh
est_co2e_savings = est_energy_savings*0.857
# 1 mile (car) per 0.77 lb CO2 emission
est_car_miles = est_co2e_savings/0.77
# 1 mile (plane) per 0.75 CO2e emission
est_plane_miles = est_co2e_savings/0.75
# 1 tree absorbs 48 lbs of CO2 per year --> converts to lb per 7 days
est_trees = est_co2e_savings/((48/365)*7)

est_energy_savings = round(est_energy_savings)
est_co2e_savings = round(est_co2e_savings)
est_car_miles = round(est_car_miles)
est_plane_miles = round(est_plane_miles)
est_trees = round(est_trees)


# finds the estimated money saved by user based on the energy saved

# in the past, estimated energy usage vs what they actually used (should see it being under the line, how much energy that they have saved?)


# for time in df_savings_sum["time"]: # iterates through each hour and appends the sum of usage to the df_savings_sum
#   mask = house.next_hour(time,True)
#   df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO"] = df_savings.loc[mask]["use_HO"].sum()
#   df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO_save"] = df_savings.loc[mask]["use_HO_save"].sum()
