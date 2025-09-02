import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

# Initializing Flask App
app = Flask(__name__)

# Loading the pre-trained model
filename = "Model/Model_rfc.sav"
model = pickle.load(open(filename, "rb"))

# Set up the main route
@app.route('/', methods=["GET", "POST"])
def main():

    if request.method == "POST":
        # Extract the input from the form
        LIMIT_BAL = request.form.get("LIMIT_BAL")
        SEX = request.form.get("SEX")
        EDUCATION = request.form.get("EDUCATION")
        MARRIAGE = request.form.get("MARRIAGE")
        AGE = request.form.get("AGE")
        PAY_1 = request.form.get("PAY_1")
        PAY_2 = request.form.get("PAY_2")
        PAY_3 = request.form.get("PAY_3")
        PAY_4 = request.form.get("PAY_4")
        PAY_5 = request.form.get("PAY_5")
        PAY_6 = request.form.get("PAY_6")
        BILL_AMT1 = request.form.get("BILL_ATM1")
        BILL_AMT2 = request.form.get("BILL_ATM2")
        BILL_AMT3 = request.form.get("BILL_ATM3")
        BILL_AMT4 = request.form.get("BILL_ATM4")
        BILL_AMT5 = request.form.get("BILL_ATM5")
        BILL_AMT6 = request.form.get("BILL_ATM6")
        PAY_AMT1 = request.form.get("PAY_AMT1")
        PAY_AMT2 = request.form.get("PAY_AMT2")
        PAY_AMT3 = request.form.get("PAY_AMT3")
        PAY_AMT4 = request.form.get("PAY_AMT4")
        PAY_AMT5 = request.form.get("PAY_AMT5")
        PAY_AMT6 = request.form.get("PAY_AMT6")
    
        # Create DataFrame based on input
        input_variables = pd.DataFrame([[LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,
                                        BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]],
                                       columns=["LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE","PAY_1","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6",
                                               "BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6",
                                               "PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6"],
                                       dtype=int,
                                       index=['input'])

        # Get the model's prediction
        # Given that the prediction is stored in an array we simply extract by indexing
        prediction = model.predict(input_variables)[0]
    
        # We now pass on the input from the from the prediction to the index page
        return render_template("index.html",
                                     original_input={'LIMIT_BAL':LIMIT_BAL,
                                                     'SEX':SEX,
                                                     'EDUCATION':EDUCATION,
                                                    'MARRIAGE':MARRIAGE,
                                                    'AGE':AGE,
                                                     'PAY_1':PAY_1, 'PAY_2':PAY_2, 'PAY_3':PAY_3, 'PAY_4':PAY_4, 'PAY_5': PAY_5, 'PAY_6':PAY_6,
                                                    'BILL_AMT1':BILL_AMT1, 'BILL_AMT2':BILL_AMT2, 'BILL_AMT3':BILL_AMT3,
                                                    'BILL_AMT4':BILL_AMT4, 'BILL_AMT5':BILL_AMT5, 'BILL_AMT6':BILL_AMT6,
                                                    'PAY_AMT1':PAY_AMT1, 'PAY_AMT2':PAY_AMT2, 'PAY_AMT3':PAY_AMT3, 'PAY_AMT4':PAY_AMT4,
                                                    'PAY_AMT5': PAY_AMT5, 'PAY_AMT6':PAY_AMT6},
                                     result = prediction
                                     )
    # If the request method is GET
    return render_template("index.html")
