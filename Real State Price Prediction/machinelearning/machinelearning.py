import pandas as pd
import numpy as np
import joblib
model=joblib.load("machinelearning/housecost")
data=pd.read_csv("machinelearning/cols.csv")
data = data.iloc[:, 1:]


class Predict:
    def predict_price(location,sqft,bath,bhk):    
        loc_index = np.where(data.columns==location)[0][0]
    
        x = np.zeros(len(data.columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
    
        return model.predict([x])[0]


