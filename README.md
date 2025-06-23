House Price Prediction 🏠

This repository contains a machine learning model to predict house prices based on location, number of bedrooms, and area (in sq.ft). It includes a Flask web app for user interaction and predictions.
Dataset Description 📊

The dataset includes the following features for each property:

•	Property_Name

•	Location

•	Region
•	Property_Age

•	Availability

•	Area_Tpye

•	Area_SqFt

•	Rate_SqFt

•	Floor_No

•	Bedroom

•	Bathroom

•	Price_Lakh

Datasets used:

•	Final_Project.csv

•	Mumbai_Property.csv

Project Structure 📁

	app.py: Flask web application for prediction

	Mumbai property jupter.ipynb: Jupyter notebook for model training and testing

	Models:

•	housepriceprediction.pkl: Saved machine learning model

	templates:

•	index.html: Web form to input property details

•	result.html: Displays the predicted price

	dataset : Contains the CSV files used for training

Getting Started 🚀

•	Clone the repository git clone https://github.com/Moksha-07/house-price-prediction.git cd house-price-prediction

•	Install required packages (You may want to use a virtual environment) pip install flask pandas scikit-learn

•	Run the web app python app.py

•	Open your browser Go to http://localhost:5000 and enter house details to get predictions.

Output Example 🧮

Input : 

Property_Name : Venus Villas  

Location : ECR  

Region : North  

Property_Age : 5  

Availability : Available  

Area_Type : Commercial  

Area(SqFt) : 1500  

Rate_Per_SqFt : 3000  

Floor : 5  

Bedroom : 3  

Bathroom : 2

Output : 

Venus Villas is: ₹4,500,000
