from datetime import datetime as dt
from datetime import timedelta
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
    def last_12(self,datetime,exception=False): #actual
        before_12_hr = (datetime - timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        now = datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_before = (self.gen_df['time'] <= now) & (self.gen_df['time'] >= before_12_hr)
        if exception:
            return mask_before
        return self.gen_df.loc[mask_before].time.values.tolist()
    def last_24(self,datetime,exception=False): #actual
        before_24_hr = (datetime - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        now = datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_before = (self.gen_df['time'] <= now) & (self.gen_df['time'] >= before_24_hr)
        if exception:
            return mask_before
        return self.gen_df.loc[mask_before].time.values.tolist()
        
    def next_12(self,exception=False): #predicted
        now = self.datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        next_12_hr = (self.datetime + timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_after = (self.gen_df['time'] >= now) & (self.gen_df['time'] <= next_12_hr)
        if exception:
            return mask_after
        return self.gen_df.loc[mask_after].time.values.tolist()
        #self.battery+=self.act_gen(str(now))
        
    def last_24_effiencies(self,datetime):
        appliance_list=['Home office','Fridge','Wine cellar', 'Garage door','Microwave','Living room']
        app_df=self.use_df.drop(columns=['apparentTemperature','month','day','hour','use_HO'])
        app_df = app_df.loc[self.last_24(datetime,True)]
        app_df=app_df.drop(columns=['time'])
        value_list=[]
        for column in app_df:
            value_list.append(app_df[column].sum())
        app_df=house.use_df.drop(columns=['time','apparentTemperature','month','day','hour','use_HO'])       
        avg_list=[]

    def next_days(self,days,exception=False): #predicted hourly
        now = self.datetime.strftime("%Y-%m-%d %H:%M:%S")[:-5]+'00:00'
        next_x_days = (self.datetime + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")[:-5]+'00:00'
        mask_after = (self.use_df['time'] >= now) & (self.use_df['time'] <= next_x_days)
        if exception:
            return mask_after
        times = self.use_df.loc[mask_after].time.values.tolist()
        return times[0::30]
    def next_hour(self,time,exception=False): # predicted hour
        time_dt = dt.strptime(time,"%Y-%m-%d %H:%M:%S")
        next_1_hour = (time_dt + timedelta(minutes=59)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_after = (self.use_df['time'] >= time) & (self.use_df['time'] <= next_1_hour)
        if exception:
            return mask_after
        times = self.use_df.loc[mask_after].time.values.tolist()
        return times

        for column in app_df:
            avg_list.append(app_df[column].sum()/503911)

        avg_list=[round(i/sum(avg_list)*100) for i in avg_list]
        value_list=[round(i/sum(value_list)*100) for i in value_list]
        good_rec_dict={}
        bad_rec_dict={}
        avg=[]
        for i in range(len(value_list)):
            diff=value_list[i]-avg_list[i]
            if diff >= 1:
                bad_rec_dict[appliance_list[i]]=diff
                avg.append(avg_list[i])
            if diff <=-1:
                good_rec_dict[appliance_list[i]]=diff

        bad_rec_dict=dict(sorted(bad_rec_dict.items(), key=lambda x:x[1], reverse=True))
        return bad_rec_dict, good_rec_dict,avg
    
house=House(0)
#print(house.last_24(dt.now()))
print(house.next_days(31,True))