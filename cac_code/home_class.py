from datetime import datetime as dt
import pandas as pd
import lightgbm as lgb
#from battery_var import battery

class House:
    use_df=[]
    gen_df=[]
    def __init__(self,battery,datetime=dt.now()):
        self.battery=battery
        self.datetime=datetime.replace(microsecond=0).replace(second=0)
        self.use_df=pd.read_csv('cac_code/csv_data/use_HO.csv')
        self.gen_df=pd.read_csv('cac_code/csv_data/gen_sol.csv')
        self.use_model=lgb.Booster(model_file='cac_code/ml_models/use_HO_model.txt')
        self.gen_model=lgb.Booster(model_file='cac_code/ml_models/gen_sol_model.txt')
    #def battery(self):
       # return self.battery
    def date_time(self):
        return self.datetime
    def time_stamp(self):
        return dt.timestamp(self.datetime)
    def pred_cons(self,datetime): #predicted consumption
        cons_data = self.use_df.loc[self.use_df['time'] == str(datetime)]
        cons_data = cons_data.values.flatten().tolist()[1:-1]
        return self.use_model.predict([cons_data])
    def act_cons(self,datetimes): #actual consumption
        if type(datetimes) == str:
            datetimes = [datetimes]
        act_use_list = [self.use_df.loc[self.use_df['time'] == i].use_HO.values.flatten().tolist()[0] for i in datetimes]
        return act_use_list
    def pred_gen(self,datetime): #predicted generation
        weather_data=self.gen_df.loc[self.gen_df['time']==str(datetime)]
        weather_data=weather_data.values.flatten().tolist()[1:-1]
        return self.gen_model.predict([weather_data])
    def act_gen(self,datetimes): #actual generation
        if type(datetimes)==str:
            datetimes=[datetimes]
        #print(datetimes)
        act_gen_list=[self.gen_df.loc[self.gen_df['time'] == i].gen_Sol.values.flatten().tolist()[0] for i in datetimes]
        return act_gen_list
    def weather_list(self): #list of all the weather stuff
        return self.gen_df.drop(columns=["month","hour","gen_sol"])
    def use_HO(self): #returns pandas df
        return self.use_df
    def gen_sol(self): #returns pandas df
        return self.gen_df
    def update_battery(self):
        #print(self.datetime)
        now=self.datetime
        #self.battery+=self.act_gen(str(now))


house=House(0)

