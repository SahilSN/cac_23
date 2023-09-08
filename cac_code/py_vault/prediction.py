from sklearn.datasets import make_classification
from tensorflow.keras.models import load_model
import lightgbm as lgb
#model = load_model('ml_models/use_HO_model.h5')
model = lgb.Booster(model_file='ml_models/use_HO.txt')
# evaluate the model

# make a prediction


use1 = model.predict([[0.044783333,0.0051,0.013066667,0.003216667,0.001683333,34.86,10,17,6]])

print(str(use1)+'--usePredicted: 0.419383333')
use2 = model.predict([[0.042066667,0.005133333,0.01315,0.003183333,0.001366667,28.97,12,13,6]])
print(str(use2)+'--usePredicted2: 0.284')
use3 = model.predict([[0.477066667,0.121866667,0.013216667,0.003183333,0.003583333,46.84,10,2,2]])
print(str(use3)+'--usePredicted3: 1.03275')
print('\n\n')

