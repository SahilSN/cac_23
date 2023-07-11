from sklearn.datasets import make_classification
from tensorflow.keras.models import load_model
import lightgbm as lgb
#model = load_model('ml_models/use_HO_model.h5')
model = lgb.Booster(model_file='ml_models/use_HO_model.txt')
# evaluate the model

# make a prediction


use1 = model.predict([[0.044783333,0.0051,0.013066667,0.003216667,0.001683333,34.86,10,17,6]])

print(str(use1)+'--usePredicted: 0.419383333')
use2 = model.predict([[0.042066667,0.005133333,0.01315,0.003183333,0.001366667,28.97,12,13,6]])
print(str(use2)+'--usePredicted2: 0.284')
use3 = model.predict([[0.477066667,0.121866667,0.013216667,0.003183333,0.003583333,46.84,10,2,2]])
print(str(use3)+'--usePredicted3: 1.03275')
print('\n\n')
model = lgb.Booster(model_file='ml_models/gen_sol_model.txt')

gen1 = model.predict([[31.68,0.65,9.82,22.32,1002.18,12.12,0.27,301.0,0.0,21.36,0.0,1,1]])
print(str(gen1)+'--genPredicted: 0.003466667')
gen2 = model.predict([[71.01,0.81,9.35,71.01,1018.11,7.85,0.0,42.0,0.0008,64.86,0.01,8,18]])
print(str(gen2)+'--genPredicted2: 0.36295')
gen3 = model.predict([[32.15,0.86,9.07,27.72,1015.67,4.52,0.03,308.0,0.0,28.37,0.0,10,23]])
print(str(gen3)+'--genPredicted3: 0.004266667')
''''
[0.37868208]--usePredicted: 0.419383333
[0.34955731]--usePredicted2: 0.284
[1.0499925]--usePredicted3: 1.03275



[0.0035675]--genPredicted: 0.003466667
[0.35523186]--genPredicted2: 0.36295
[0.00341044]--genPredicted3: 0.004266667'''
