import pandas as pd
from datetime import datetime
import random
import csv
import lightgbm as lgb
pd.set_option('display.max_columns', None)
df=pd.read_csv('csv_data/gen_sol.csv')

df=df.drop(columns=['month','hour','gen_Sol'])
from something import return_dates

def add_row_gen(df):

    with open('csv_data/gen_sol.csv', "r", encoding="utf-8", errors="ignore") as scraped:
        last_date = scraped.readlines()[-1][:19]

    reference_dates=[i.replace("2023","2022") for i in return_dates(last_date)]

    for i in range(len(reference_dates)):
        row_list=df.loc[df['time'] == reference_dates[i]].values.flatten().tolist()
        time=row_list.pop(0)
        DATE_TIME_STRING_FORMAT = '%Y-%m-%d %H:%M:%S'
        timestamp = datetime.timestamp(datetime.strptime(time,DATE_TIME_STRING_FORMAT))
        #print(first_row_list)
        new_list=[timestamp,round(row_list[0]+random.uniform(-4,4),2),round(row_list[1]+random.uniform(-0.07,0.07),2),
                  round(row_list[2] + random.uniform(-1, 1), 2),round(row_list[3] + random.uniform(-3, 3),2),
                  round(row_list[4] + random.uniform(-20, 20), 2),round(row_list[5] + random.uniform(-1, 1),2),
                  round(row_list[6] + random.uniform(-0.1, 0.1), 2),round(row_list[7] + random.uniform(-20,20),2),
                  round(row_list[8] + random.uniform(-0.01, 0.01),2),round(row_list[9] + random.uniform(-3, 3), 2),
                  round(row_list[10] + random.uniform(-0.01, 0.01), 2),
                  int(time[5:7] if time[5]!=0 else time[6]),int(time[11:13] if time[11]!=0 else time[12])
                  ]

        model = lgb.Booster(model_file='ml_models/gen_sol_model.txt')
        predicted_gen=float(model.predict([new_list]))
        new_list.append(predicted_gen)
        new_list[0]=str(datetime.fromtimestamp(new_list[0]))

        with open('csv_data/future_data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_list)
        #csvfile.close()
    




add_row_gen(df)

#add_row(df)