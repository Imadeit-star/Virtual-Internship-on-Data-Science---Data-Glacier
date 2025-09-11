from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
#from sklearn.preprocessing import StandardScaler

# Creating a FastAPI Object
app = FastAPI()
#scaler = StandardScaler()

# Uing Pydantic lib, and defining the data types for all feature columns as inputs
class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    Blood_Pressure : int
    Skin_Thickness: int
    Insulin : int
    BMI : float
    Diabetes_Pedigree_Function: float
    Age: int

# loading saved model
Diabetes_Model_Prediction = pickle.load(open('Diabetics_Prediction.sav', 'rb'))

# Creating a Post Request to the API
@app.post('/Prediction')
def Diabetes_Predict(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    Preg = input_dictionary['Pregnancies']
    Glu = input_dictionary['Glucose']
    B_P = input_dictionary['Blood_Pressure']
    Skin = input_dictionary['Skin_Thickness']
    Insulin = input_dictionary['Insulin']
    BMI = input_dictionary['BMI']
    DPF = input_dictionary['Diabetes_Pedigree_Function']
    Age = input_dictionary['Age']
    
    input_list = [Preg, Glu, B_P, Skin, Insulin, BMI,  DPF, Age]
    #input_list = np.asarray(input_list).reshape(1,-1)
    #Std_Input_data = scaler.fit_transform(input_list)
    Diabetic_Prediction = Diabetes_Model_Prediction([input_list])
    if Diabetic_Prediction[0] == 0:
        return 'Person is Not Diabetic'
    else:
        return 'Person is Diabetic'

if __name__ == "__main__":
    uvivorn.run(app, host = '127.0.0.1', port=8000)
