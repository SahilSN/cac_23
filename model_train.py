from csv_to_dataset import df_use, df_gen
import numpy as np
from numpy import sqrt
import pandas as pd
# mlp for multiclass classification
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping

# load the dataset
# mlp for regression
from pandas import read_csv
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
'''
def train_dataset(df):
    # load the dataset
    if len(df.axes[1])==10:
        df_name='use_HO'
    elif len(df.axes[1])==14:
        df_name='gen_sol'
    else:
        return 'uh oh'

    df = read_csv('csv_data/'+df_name+'.csv', header=None,low_memory=False)
    #print(df.dtypes)


    # split into input and output columns
    X, y = df.values[:, :-1], df.values[:, -1]
    # split into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    X_train = np.asarray(X_train).astype(np.float32)
    y_train = np.asarray(y_train).astype(np.float32)
    X_test = np.asarray(X_test).astype(np.float32)
    y_test = np.asarray(y_test).astype(np.float32)
    # determine the number of input features
    n_features = X_train.shape[1]
    # define model
    model = Sequential()
    model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
    model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
    model.add(Dense(1))
    # compile the model
    model.compile(optimizer='adam', loss='mse')

    # fit the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

    # evaluate the model
    error = model.evaluate(X_test, y_test, verbose=0)
    print('MSE: %.3f, RMSE: %.3f' % (error, sqrt(error)))

    model.save('ml_models/'+df_name+'_model'+'.h5')

train_dataset(df_use)
print('use_HO training done and saved')
#train_dataset(df_gen)
#print('gen_sol training done and saved')
'''
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.metrics import mean_squared_error

from sklearn.metrics import accuracy_score


def train_dataset(df):
    # load the dataset
    if len(df.axes[1])==10:
        df_name='use_HO'
    elif len(df.axes[1])==14:
        df_name='gen_sol'
    else:
        return 'uh oh'

    df = read_csv('csv_data/'+df_name+'.csv', header=None,low_memory=False)
    # Step 1: Initialise and fit LightGBM multiclass model
    X, y = df.values[:, :-1], df.values[:, -1]
    # split into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)


    # defining parameters
    params = {
        'task': 'train',
        'boosting': 'gbdt',
        'objective': 'regression',
        'metric': {'mse'},
        'num_leaves': 200,
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
                     valid_sets=lgb_eval,
                     early_stopping_rounds=30)

    # prediction
    y_pred = model.predict(X_test)

    # accuracy check
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse**(0.5)
    print("MSE: %.2f" % mse)
    print("RMSE: %.2f" % rmse)

    #lgb.save(model,'ml_models/'+df_name+'_model.txt')
    #model.booster_.save_model('ml_models/'+df_name+'_model.txt')
    model.save_model('ml_models/'+df_name+'_model.txt')
    #model.save_model('ml_models/'+df_name+'_model.txt')

train_dataset(df_use)
print('use_HO train done')
train_dataset(df_gen)
print('gen_sol train done')