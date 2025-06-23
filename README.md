House Price Prediction 🏠
This repository contains a machine learning model to predict house prices based on location, number of bedrooms, and area (in sq.ft). It includes a Flask web app for user interaction and predictions.

Dataset Description 📊
The dataset includes the following features for each property:

Location: Name of the locality in Mumbai (e.g., Andheri, Borivali)

BHK: Number of bedrooms, hall, kitchen units (e.g., 1 BHK, 2 BHK)

Area (sq.ft): Total built-up area of the property

Price: The actual market price of the property in INR (target variable)

Datasets used:

Final_Project.csv

Mumbai_Property.csv

Project Structure 📁
app.py: Flask web application for prediction

Mumbai property jupter.ipynb: Jupyter notebook for model training and testing

models/housepriceprediction.pkl: Saved machine learning model

templates/:

index.html: Web form to input property details

result.html: Displays the predicted price

dataset/: Contains the CSV files used for training

Getting Started 🚀
Clone the repository
git clone https://github.com/Moksha-07/house-price-prediction.git
cd house-price-prediction

Install required packages
(You may want to use a virtual environment)
pip install flask pandas scikit-learn

Run the web app
python app.py

Open your browser
Go to http://localhost:5000 and enter house details to get predictions.

Output Example 🧮
Input:

Location: Andheri

BHK: 2

Area: 1000 sq.ft

Output:

Predicted Price: ₹1.15 Crores

## 📁 Project Structure
dataset/
 ├── Final_Project.csv
 └── Mumbai_Property.csv
 models/
 └── housepriceprediction.pkl # Trained ML model
 templates/
 ├── index.html
 └── result.html
 app.py # Flask web app
 Mumbai property jupter.ipynb # Jupyter Notebook for model training

 ML Model
- Algorithm used: (e.g., Linear Regression / Random Forest)
- Features considered: Area, Location, Bedrooms, etc.
- Target: House price
