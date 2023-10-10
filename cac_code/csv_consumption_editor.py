import pandas as pd
df=pd.read_csv('cac_code/csv_data/battery_data.csv')
df['Battery'] = [round(i,2) for i in df['Battery'].values.tolist()]
df['waste'] = [round(i,2) for i in df['waste'].values.tolist()]
df.to_csv('cac_code/csv_data/battery_data.csv',index=None)