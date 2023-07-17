import pandas as pd
df=pd.read_csv('csv_data/incremented_use.csv')

for i, row in df.iterrows():
    # Check if the row should be deleted
    if str(row['time'])[14:15] not in ['00','15','30','45']:
        # Delete the row
        df.drop(i, inplace=True)
