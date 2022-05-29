import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


car_data = pd.read_csv('CarPrice_Assignment.csv')
car_data = car_data.drop('car_ID', axis = 1)

brand = car_data.CarName.apply(lambda s: s.split()[0])
car_data.insert(3,"CarBrandName", brand)
car_data.drop(['CarName'],axis=1,inplace=True)
name_correction = {'toyouta': 'toyota',
                  'Nissan': 'nissan',
                  'maxda': 'mazda',
                  'vokswagen': 'volkswagen',
                  'vw':'volkswagen',
                  'porcshce': 'porsche'}
car_data.CarBrandName = car_data.CarBrandName.apply(lambda s: name_correction[s] if s in name_correction else s)


car_data['mpg'] = (0.60 * car_data.citympg) + (0.40 * car_data.highwaympg)
# drop the original variables
car_data.drop(['citympg', 'highwaympg'], axis = 1, inplace = True)


car_data_new = car_data[[ 'wheelbase','carlength','carwidth','curbweight','fueltype','enginesize',
                         'boreratio','horsepower','mpg','enginetype','fueltype','carbody', 
                         'aspiration','cylindernumber','drivewheel','price']]





X = car_data_new.drop('price', axis =1)
y = car_data_new['price']
X = pd.get_dummies(X, columns= ['enginetype','fueltype','carbody','aspiration','cylindernumber','drivewheel'], drop_first= True)





from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)
# print(X_train.shape, X_test.shape)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
from sklearn.metrics import r2_score
# print("Train Accuracy:",r2_score(lr.predict(X_train), y_train))
# print("Test Accuracy:", r2_score(lr.predict(X_test), y_test))
variable = X.columns
coeff = lr.coef_.round(2)
var_coeff = pd.DataFrame(list(zip(variable, coeff)),
               columns =['Variable', 'Coefficients'])

import pickle
# using the dump() function to save the model using pickle
saved_model = pickle.dumps(lr)
# loading that saved model
lr_from_pickle = pickle.loads(saved_model)
# use this to make predictions
lr_from_pickle.predict(X_test)
print(lr.predict([[109.1,188.8,68.8,3049,141,3.78,160,21.4,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1]]))