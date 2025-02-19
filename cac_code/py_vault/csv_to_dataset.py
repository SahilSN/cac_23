'''
https://www.kaggle.com/code/koheimuramatsu/change-detection-forecasting-in-smart-home/notebook
Tutorial Notebook using HomeC.csv
'''
import pandas as pd

df = pd.read_csv("cac_code/csv_data/HomeC.csv", low_memory=False)
pd.set_option('display.max_columns', None)

#removing [kW] from the columns
df.columns = [i.replace(' [kW]', '') for i in df.columns]

#Making kitchen and furnace columnns simpler
df['Furnace'] = df[['Furnace 1','Furnace 2']].sum(axis=1)
df['Kitchen'] = df[['Kitchen 12','Kitchen 14','Kitchen 38']].sum(axis=1)
df.drop(['Furnace 1','Furnace 2','Kitchen 12','Kitchen 14','Kitchen 38','icon','summary'], axis=1, inplace=True)

#removes NaN row
df[df.isnull().any(axis=1)]
df = df[0:-1]

#some cloud cover datapoints are invalid, so replacing them
df['cloudCover'].replace(['cloudCover'], method='bfill', inplace=True)
df['cloudCover'] = df['cloudCover'].astype('float')

#converting time column to readable format
original_time=df['time']
df['time'] = pd.DatetimeIndex(pd.date_range('2023-01-01 01:00', periods=len(df),  freq='min'))

#extracting the year,month, etc for modeling purposes
df['year'] = df['time'].apply(lambda x : x.year)
df['month'] = df['time'].apply(lambda x : x.month)
df['day'] = df['time'].apply(lambda x : x.day)
df['weekofyear'] = df['time'].apply(lambda x : x.weekofyear)
df['hour'] = df['time'].apply(lambda x : x.hour)
df['minute'] = df['time'].apply(lambda x : x.minute)

#df['time'] = pd.to_numeric(original)
#setting the time of day based on the hour
def hours2timing(x):
    if x in [22,23,0,1,2,3]:
        timing = 4 #night
    elif x in range(4, 12):
        timing = 1 #morning
    elif x in range(12, 17):
        timing = 2 #afternoon
    elif x in range(17, 22):
        timing = 3 #evening
    else:
        timing = 'X'
    return timing
df['timing'] = df['hour'].apply(hours2timing)

#combining similar columns
df['use_HO'] = df['use']
df['gen_Sol'] = df['gen']
df.drop(['use','House overall','gen','Solar'], axis=1, inplace=True)
#print(df.head(3))
df_use=df.drop(columns=["Dishwasher","Barn","Well","temperature","humidity","visibility","pressure"
    ,"windSpeed","cloudCover","windBearing","precipIntensity","dewPoint","precipProbability","Furnace","Kitchen","year"
    ,"weekofyear","minute","timing","gen_Sol"])
df_gen=df.drop(columns=["Dishwasher", "Home office", "Fridge", "Wine cellar", "Garage door", "Barn", "Well",
                        "Microwave", "Living room", "Furnace", "Kitchen","year","day","weekofyear","minute","timing"
,"use_HO"])

#df_gen['gen_Sol'] = df_gen['gen_Sol'].apply(lambda x: x*0.5)

hours=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0]
#scalars=[0.005,0.005,0.005,0.005,0.006,0.008,0.008,0.008,0.008,0.006,0.005,0.005,0.005,0.005,0.005,0.005,0.006,0.007,0.009,0.009,0.009,0.006,0.005,0.005]
scalars=[0.09,0.009,0.009,0.01,0.01,0.011,0.011,0.01,0.009,0.008,0.008,0.007,0.007,0.007,0.008,0.008,0.009,0.009,0.011,0.011,0.011,0.01,0.009,0.009]

for i in range(len(hours)):
    df_use.loc[df_use['hour']==hours[i],'use_HO'] = df_use.loc[df_use['hour']==hours[i],'use_HO']*scalars[i]
    df_gen.loc[df_gen['hour']==hours[i],'gen_Sol'] = df_gen.loc[df_gen['hour']==hours[i],'gen_Sol']*0.1

df_use.to_csv('cac_code/csv_data/use_HO.csv',index=False)
df_gen.to_csv('cac_code/csv_data/gen_sol.csv',index=False)


