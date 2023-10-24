import pandas as pd
import numpy as np
from home_class import house
from datetime import datetime as dt, timedelta
import random
use_df=house.use_df
gen_df=house.gen_df

now = dt.now().replace(microsecond=0).replace(second=0)


dt_list=use_df.time.values.tolist()[335361:]
modeled_use=[]
percent_saved=[]

for datetime in dt_list:
  
  act_use=house.act_cons(datetime)[0]
  d=act_use
  bad_rec_dict,good_rec_dict,avg_list=house.last_24_effiencies(dt.strptime(datetime,'%Y-%m-%d %H:%M:%S'))
  loss_list=[]

  counter=0
  for i in bad_rec_dict:
    
    appliance=i
    value=bad_rec_dict[i]
    
    value_percent=(100-random.uniform(0,value))/100
    
    chunk=act_use*(100-avg_list[counter])/100
    
    act_use-=chunk
    act_use+=chunk*value_percent
    counter+=1
  percent=str(round(((d-act_use)/d)*100,2))+'%'
  print(datetime, '\t\t',percent)
  modeled_use.append(round(act_use,4))
  percent_saved.append(percent)


act_list=[round(house.act_cons(i)[0],4) for i in dt_list]
pred_list=[round(house.pred_cons(i)[0],4) for i in dt_list]

pred_acc=[]
for i in range(len(act_list)):
  pred_acc.append(str(round(100-(abs(act_list[i]-pred_list[i])/act_list[i])*100,2))+"%")
df=pd.DataFrame(data={
  'time':dt_list,
  'actual_consumption':act_list,
  'ml_predicted_consumption':pred_list,
  'improved_consumption':modeled_use,
  'percent_saved':percent_saved,
  'prediction_accuracy':pred_acc,
})

df.to_csv("cac_code/csv_data/modeled_use.csv",index=None)

  
