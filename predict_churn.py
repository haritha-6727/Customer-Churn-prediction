# predict_churn.py

import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder


model = joblib.load(r'C:\\Users\\user\\Desktop\\customer_churn\\churn_model.pkl')


def predict_churn(input_dict):
    
    input_df = pd.DataFrame([input_dict])


    le = LabelEncoder()

    
    for col in input_df.select_dtypes(include='object').columns:
        input_df[col] = le.fit_transform(input_df[col])

    
    churn_prob = model.predict_proba(input_df)[:, 1][0]
    return churn_prob
