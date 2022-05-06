import joblib
import pandas as pd


class CreditModel():
    
    def __init__(self):
        self.model = joblib.load('xgb_model.joblib')
        self.encoder = joblib.load('OneHotencoder.joblib')
    
    def predict(self, FLAG_OWN_CAR, FLAG_OWN_REALTY, AMT_INCOME_TOTAL,
                NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, AGE):
        data_dict = {'FLAG_OWN_CAR':FLAG_OWN_CAR,
                     'FLAG_OWN_REALTY':FLAG_OWN_REALTY,
                     'AMT_INCOME_TOTAL':AMT_INCOME_TOTAL,
                     'NAME_EDUCATION_TYPE': NAME_EDUCATION_TYPE,
                     'NAME_FAMILY_STATUS': NAME_FAMILY_STATUS,
                     'AGE':AGE}
        df_pred = pd.DataFrame([data_dict])
        X_pred = self.encoder.transform(df_pred)
        credit_score = (self.model.predict_proba(X_pred)[0][0])*100
        return credit_score