from flask import Flask, render_template, request 
import pickle 
import numpy as n
import traceback

app = Flask(__name__)

try:
    with open(r'C:\Users\smoks\house price prediction\models\housepriceprediction.pkl', 'rb') as file:
        model1 = pickle.load(file)
except Exception as e:
    print(f" Error loading model: {e}")
    model1 = None
@app.route("/")
def index():
  return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    try:
        d1= request.form['Property_Name']
        d2 = int(request.form['Location'])
        d3 = int(request.form['Region'])
        d4 = int(request.form['Property_Age'])
        d5 = int(request.form['Availability'])
        d6 = int(request.form['Area_Type'])
        d7 = int(request.form['Area(SqFt)'])
        d8 = int(request.form['Rate_Per_SqFt'])
        d9 = int(request.form['Floor'])
        d10 = int(request.form['Bedroom'])
        d11 = int(request.form['Bathroom'])
        
        if d7 <= 0 or d8 <= 0:
            predicted_price = 0
        else:
            predicted_price = d7 * d8

    except:
        predicted_price = 0

    return render_template("result.html", prediction_label=d1, prediction_text1=f"₹{predicted_price:,}")

if __name__ == '__main__':
    app.run(debug=True)