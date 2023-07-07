
import pandas as pd
import os


#for dirname, _, filenames in os.walk('/kaggle/input'):
    #for filename in filenames:
        #print(os.path.join(dirname, filename))

df = pd.read_csv("HomeC.csv",low_memory=False)
#print(f'HomeC.csv : {df.shape}')
#print(df.head(3))

df.columns = [i.replace(' [kW]', '') for i in df.columns]
df['Furnace'] = df[['Furnace 1','Furnace 2']].sum(axis=1)
df['Kitchen'] = df[['Kitchen 12','Kitchen 14','Kitchen 38']].sum(axis=1)
df.drop(['Furnace 1','Furnace 2','Kitchen 12','Kitchen 14','Kitchen 38','icon','summary'], axis=1, inplace=True)
df[df.isnull().any(axis=1)]
df['cloudCover'].unique()
df[df['cloudCover']=='cloudCover'].shape
df['cloudCover'].replace(['cloudCover'], method='bfill', inplace=True)
df['cloudCover'] = df['cloudCover'].astype('float')
#pd.to_datetime(df['time'], unit='s')
df['time'] = pd.DatetimeIndex(pd.date_range('2016-01-01 05:00', periods=len(df),  freq='min'))
pd.set_option('display.max_columns', None)
print(df.iloc[[601]])
