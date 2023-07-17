import pandas as pd
import random
import csv
pd.set_option('display.max_columns', None)
df=pd.read_csv('csv_data/gen_sol.csv')

df=df.drop(columns=['month','hour','gen_Sol'])


def add_row(df):
    first_row = df.iloc[0]

    first_row_list = first_row.tolist()

    #time
    #2022-07-16 05:00:00
    #2023-07-01 03:29:00
    time=first_row_list[0]
    new_list=[]
    #temp
    new_list.append(round((first_row_list[0]+random.uniform(-4,4)),2))  #humidity
    new_list.append(round(first_row_list[1] + random.uniform(-0.07, 0.07),2))
    #visibility
    new_list.append(round(first_row_list[2] + random.uniform(-1, 1),2))
    #appTemp
    new_list.append(round(first_row_list[3] + random.uniform(-3, 3),2))
    #pressure
    new_list.append(round(first_row_list[4] + random.uniform(-20, 20),2))
    #windSpeed
    new_list.append(round(first_row_list[5] + random.uniform(-1, 1),2))
    #cloudCover
    new_list.append(round(first_row_list[6] + random.uniform(-0.1, 0.1),2))
    #windBearing
    new_list.append(round(first_row_list[7] + random.uniform(-20,20),2))
    #precipIntensity
    if first_row_list[8]==0:
        new_list.append(0)
    else:
        new_list.append(round(first_row_list[8] + random.uniform(-0.01, 0.01),2))
    #dewPoint
    new_list.append(round(first_row_list[9] + random.uniform(-3, 3),2))
    #precipProb
    if first_row_list[10] == 0:
        new_list.append(0)
    else:
        new_list.append(round(first_row_list[8] + random.uniform(-0.01, 0.01),2))
    print(new_list)
    print(type(new_list))
    with open('csv_data/future_data.csv', 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_list)
        #csvfile.close()


add_row(df)
#add_row(df)