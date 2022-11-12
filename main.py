# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:38:53 2022

@author: HP
"""


from fastapi import FastAPI
from  pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    Age : int
    Sex : int
    ChestPainType : int
    RestingBP : int
    Cholesterol : int
    FastingBS : int
    RestingECG : int
    MaxHR : int
    ExerciseAngina : int
    Oldpeak : float
    ST_Slope : int
    MajorVessels : int
    Thal : int
    
#Loading the saved model
heart_disease_model = pickle.load(open('heart_disease.sav', 'rb'))

@app.post('/heart_disease_predict')
def heart_disease_prediction(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['Age']
    sex = input_dictionary['Sex']
    cp = input_dictionary['ChestPainType']
    rbp = input_dictionary['RestingBP']
    cholesterol = input_dictionary['Cholesterol']
    fbs = input_dictionary['FastingBS']
    recg = input_dictionary['RestingECG']
    mhr = input_dictionary['MaxHR']
    angina = input_dictionary['ExerciseAngina']
    oldpeak = input_dictionary['Oldpeak']
    slope = input_dictionary['ST_Slope']
    mv = input_dictionary['MajorVessels']
    thal = input_dictionary['Thal']
    
    
    input_list = [age, sex, cp, rbp, cholesterol, fbs, recg, mhr, angina, oldpeak, slope, mv, thal]
    
    
    prediction = heart_disease_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'

