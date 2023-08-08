import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV files
gendf = pd.read_csv('csv_data/gen_sol.csv')
consdf = pd.read_csv('csv_data/use_HO.csv')

# Select relevant columns
gen = gendf[['time', 'gen_Sol']]
cons = consdf[['time', 'use_HO']]

def thinger(rangez):
    if rangez == 'jan':
        start_date = '2023-01-01'
        end_date = '2023-01-31'
    elif rangez == 'feb':
        start_date = '2023-02-01'
        end_date = '2023-02-28'  
    elif rangez == 'mar':
        start_date = '2023-03-01'
        end_date = '2023-03-31'
    elif rangez == 'apr':
        start_date = '2023-04-01'
        end_date = '2023-04-30'
    elif rangez == 'may':
        start_date = '2023-05-01'
        end_date = '2023-05-31'
    elif rangez == 'jun':
        start_date = '2023-06-01'
        end_date = '2023-06-30'
    elif rangez == 'jul':
        start_date = '2023-07-01'
        end_date = '2023-07-31'
    elif rangez == 'aug':
        start_date = '2023-08-01'
        end_date = '2023-08-31'
    elif rangez == 'sep':
        start_date = '2023-09-01'
        end_date = '2023-09-30'
    elif rangez == 'oct':
        start_date = '2023-10-01'
        end_date = '2023-10-31'
    elif rangez == 'nov':
        start_date = '2023-11-01'
        end_date = '2023-11-30'
    elif rangez == 'dec':
        start_date = '2023-12-01'
        end_date = '2023-12-31'

    combined_data = gen.merge(cons, on='time')

    combined_data['time'] = pd.to_datetime(combined_data['time'])

    monthly_data = combined_data[(combined_data['time'] >= start_date) & (combined_data['time'] <= end_date)]

    hourly_avg = monthly_data.groupby(monthly_data['time'].dt.hour).mean()

    return hourly_avg

fig, axs = plt.subplots(6, 2, figsize=(12, 9))
data = thinger("jan")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[0, 0])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[0, 0])
data = thinger("feb")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[0, 1])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[0, 1])
data = thinger("mar")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[1, 0])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[1, 0])
data = thinger("apr")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[1, 1])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[1, 1])
data = thinger("may")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[2, 0])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[2, 0])
data = thinger("jun")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[2, 1])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[2, 1])
data = thinger("jul")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[3, 0])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[3, 0])
data = thinger("aug")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[3, 1])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[3, 1])
data = thinger("sep")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[4, 0])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[4, 0])
data = thinger("oct")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[4, 1])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[4, 1])
data = thinger("nov")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[5, 0])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[5, 0])
data = thinger("dec")

sns.lineplot(data=data, x=data.index, y='gen_Sol', ax = axs[5, 1])
sns.lineplot(data=data, x=data.index, y='use_HO', ax = axs[5, 1])

plt.show()
