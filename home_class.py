from datetime import datetime as dt
import pandas as pd
import lightgbm as lgb


class House:
    use_df=[]
    gen_df=[]
    def __init__(self,battery,datetime=dt.now()):
        self.battery=battery
        self.datetime=datetime
        self.use_df=pd.read_csv('csv_data/use_HO.csv')
        self.gen_df=pd.read_csv('csv_data/gen_sol.csv')
        self.use_model=lgb.Booster(model_file='ml_models/use_HO_model.txt')
        self.gen_model=lgb.Booster(model_file='ml_models/gen_sol_model.txt')
    def battery(self):
        return self.battery
    def date_time(self):
        return self.datetime
    def time_stamp(self):
        return dt.timestamp(self.datetime)
    def pred_cons(self,cons_data): #predicted consumption
        return self.use_model.predict([cons_data])
    def act_cons(self,datetimes): #actual consumption
        if type(datetimes) == str:
            datetimes = [datetimes]
        act_use_list = [self.use_df.loc[self.use_df['time'] == i].use_HO.values.flatten().tolist()[0] for i in datetimes]
        return act_use_list
    def pred_gen(self,weather_data): #predicted generation
        return self.gen_model.predict([weather_data])
    def act_gen(self,datetimes): #actual generation
        if type(datetimes)==str:
            datetimes=[datetimes]
        act_gen_list=[self.gen_df.loc[self.gen_df['time'] == i].gen_Sol.values.flatten().tolist()[0] for i in datetimes]
        return act_gen_list
    def weather_list(self): #list of all the weather stuff
        return self.gen_df.drop(columns=["month","hour","gen_sol"])
    def use_HO(self): #returns pandas df
        return self.use_df
    def gen_sol(self): #returns pandas df
        return self.gen_df



house=House(456)
print(house.act_cons('2023-01-01 05:03:00'))
print(house.act_cons(['2023-01-01 05:03:00']))
print(house.act_cons(['2023-01-01 05:03:00','2023-01-01 05:06:00']))


