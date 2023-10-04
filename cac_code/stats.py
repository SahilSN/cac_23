from home_class import house
from datetime import timedelta
df_use=house.use_df
df_gen=house.gen_df
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
