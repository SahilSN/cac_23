import os
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
from py_vault.csv_to_dataset import df_gen
import numpy as np
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.metrics import mean_squared_error


def train_dataset(df):
    # load the dataset

    if len(df.axes[1])==11:
        df_name='use_HO'
    elif len(df.axes[1])==15:
        df_name='gen_sol'
    else:
        return 'uh oh'

    print(df_name)

    df = pd.read_csv('csv_data/'+df_name+'.csv',low_memory=False)

    DATE_TIME_STRING_FORMAT = '%Y-%m-%d %H:%M:%S'
    df['time']=datetime.timestamp(datetime.strptime(df['time'],DATE_TIME_STRING_FORMAT))
    print(df.head(3))
    # Step 1: Initialise and fit LightGBM multiclass model
    X, y = df.values[:, :-1], df.values[:, -1]
    # split into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    '''
    testing num-leaves for accuracy
    100:
    0.3794404
    0.0367150
    200:
    0.3430730
    0.0331533
    300:
    0.3279075
    0.0324600   
    400:
    0.3215256
    0.0320629
    500:
    0.3127692
    0.0319091
    700:
    0.3074441
    0.0315535
    900:
    0.3019604
    0.0313094
    1000:
    0.3013428
    0.0316533
    '''


    # defining parameters
    params = {
        'task': 'train',
        'boosting': 'gbdt',
        'objective': 'regression',
        'metric': {'mse'},
        'num_leaves': 900,
        'max_depth':20,
        'drop_rate': 0.05,
        'learning_rate': 0.1,
        'seed': 0,
        'feature_fraction': 1.0,
        'bagging_fraction': 1.0,
        'bagging_freq': 0,
        'min_child_samples': 5
    }

    # laoding data
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    # fitting the model
    model = lgb.train(params,
                     train_set=lgb_train,
                     valid_sets=lgb_eval)

    # prediction
    y_pred = model.predict(X_test)

    # accuracy check
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** (0.5)
    rmspe = np.sqrt(np.mean(np.square(((y_test - y_pred) / y_test)), axis=0)) * 100
    accuracy = 1 - mse / np.var(y_test)

    # sklearn_evaulation metric
    from sklearn.metrics import r2_score
    score = r2_score(y_test, y_pred)

    print("The accuracy(sk) of our model is {}%".format(round(score, 2) * 100))

    print("MSE: %.2f" % mse)
    print("RMSE: %.2f" % rmse)
    print("RMSPE: %.9f" % rmspe)
    print("accuracy: %.9f" % accuracy)


    # visualizing in a plot
    x_ax = range(len(y_test))
    plt.figure(figsize=(20, 6))
    plt.plot(x_ax, y_test, label="original")
    plt.plot(x_ax, y_pred, label="predicted")
    plt.title("test and predicted data")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='best', fancybox=True, shadow=True)
    plt.grid(True)
    #plt.show()

    #lgb.save(model,'ml_models/'+df_name+'_model.txt')
    #model.booster_.save_model('ml_models/'+df_name+'_model.txt')
    model.save_model('ml_models/'+df_name+'_model.txt')
    #model.save_model('ml_models/'+df_name+'_model.txt')





train_dataset(df_gen)
print('use_HO train done')


