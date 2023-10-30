from home_class import house
from datetime import datetime as dt, timedelta
import random
df_use=house.use_df
df_gen=house.gen_df
now=house.datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
now2 = dt.now().replace(microsecond=0).replace(second=0) # should be same as now
last_hour = (house.datetime - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
print('test')
#print(df_use)
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
total_generated=0
total_consumed=0
battery_left=0
generation_efficiency=0



mask_before = (df_gen['time'] <= now)
avg_list = df_gen.loc[mask_before].gen_Sol.values.tolist()
avg=sum(avg_list)/len(avg_list)

for datetime in period:
  total_generated += house.act_gen(datetime)[0]
  total_consumed += house.act_cons(datetime)[0]
generation_efficiency=((house.act_gen(now)[0]/avg)*100)
hour_avg=((total_consumed)/len(period))*60

num_hours = len(period)/60
print(num_hours)

total_generated *= num_hours
total_consumed *= num_hours

total_generated=round(total_generated, 3)
total_consumed=round(total_consumed, 3)
generation_efficiency=round(generation_efficiency)
hour_avg=round(hour_avg, 3)


### Note: Same processing as in charts.py -- is there a way to make this more efficient?
## Predicted savings line
print("hello")
df_savings=df_use.loc[house.next_days(7,True)][["time","use_HO"]]
df_savings["use_HO_save"] = df_savings["use_HO"]*random.uniform(0.88,0.94)
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
## Data: www.newfoodmagazine.com/article/153960/food-waste-climate

# 0.857 lbs CO2e per 1 kWh
est_co2e_savings = est_energy_savings*0.857
# 1 mile (car) per 0.77 lb CO2 emission
est_car_miles = est_co2e_savings/0.77
# 1 mile (plane) per 0.75 CO2e emission
est_plane_miles = est_co2e_savings/0.75
# 1 tree absorbs 48 lbs of CO2 per year --> converts to lb per 7 days
est_trees = est_co2e_savings/((48/365)*7)
# 1 kg of food saves 2.5 kg of co2 --> multiply co2 saved by 1/2.5
est_lb_food = est_co2e_savings/2.5

est_energy_savings = round(est_energy_savings)
est_co2e_savings = round(est_co2e_savings)
est_car_miles = round(est_car_miles)
est_plane_miles = round(est_plane_miles)
est_trees = round(est_trees)
est_lb_food = round(est_lb_food)

def get_current_usages():
  now2 = dt.now().replace(microsecond=0).replace(second=0) # should be same as now
  appliance_list, value_list, avg_list = house.last_24_efficiencies(now2)
  today = {}
  yesterday = {}
  for index, appliance in enumerate(appliance_list):
    today[appliance] = value_list[index]
    yesterday[appliance] = avg_list[index]
  print(value_list)
  print(avg_list)
  msg = "Percentage of energy usage by location in the format {Location: Percentage} for today is " + str(today) + ". Percentage of energy usage by location in the format {Location: Percentage} for yesterday is " + str(yesterday) + ". Do not repeat any advice that you have given me in the past."

  return msg
  # Percentage of energy usage by location in the format {Location: Percentage} for today is 
  # {Home office: 25, Fridge: 33, Wine cellar: 17, Garage door: 9, Microwave: 5, Living room: 12}. 
  # Percentage of energy usage by location in the format {Location: Percentage} for yesterday is 
  # {Home office: 33, Fridge: 26, Wine cellar: 17, Garage door: 6, Microwave: 4, Living room: 14}.


# finds the estimated money saved by user based on the energy saved

# in the past, estimated energy usage vs what they actually used (should see it being under the line, how much energy that they have saved?)


# for time in df_savings_sum["time"]: # iterates through each hour and appends the sum of usage to the df_savings_sum
#   mask = house.next_hour(time,True)
#   df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO"] = df_savings.loc[mask]["use_HO"].sum()
#   df_savings_sum.loc[df_savings_sum["time"]==time,"use_HO_save"] = df_savings.loc[mask]["use_HO_save"].sum()
