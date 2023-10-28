import pandas as pd
df=pd.read_csv('cac_code/csv_data/use_HO.csv')
#sorted_df = df.sort_values(by=["hour","time"], ascending=True)
df.loc[df['hour'] ==1 or df['hour'] ==23,'use_HO'] = df.loc[df['hour'] ==1 or df['hour']==23,'use_HO']*0
#df=sorted_df.sort_values(by=["time"], ascending=True)
print(df)