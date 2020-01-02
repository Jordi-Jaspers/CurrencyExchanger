"""
App.py Module for Flask CurrencyExchanger Webapp 

This script allows the user to Convert different currency by using an API from RapidAPI
and the combination of a Database with all the different countries. On the website you 
only have to choose what you would like to convert and everything will change automaticaly

When there is a currency that isn't mentioned in the API it will give a notification.

This script requires the full 'requirement.txt'  to be installed within the Python
environment you are running this script in. Installing modules in python are done by using

"Pip3 install requirements.txt -r"

This file ccontains the following

Classes:
    * Currency(mysql.Model) - Gets all the Data listed in the database
    * Form(FlaskForm) - Lists all the choices of currencies in form of the HTML-page

Functions:
    * CurrencyExchanger() - returns the view needed for the reroute of the HTML-page with its variables

References
    ----------
    All References are Mentioned in the README.MD   
"""

from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_sqlalchemy import SQLAlchemy

import os
import numpy as np


# Create Flask Application
app = Flask(__name__)

# Initializing Database Variables
SECRET_KEY = os.urandom(32)

DATABASE_HOST   = 'mysql'
DATABASE_USER   = 'root'
DATABASE_PASS    = 'root'
DATABASE_PORT   = '3306'
DATABASE_DB        = 'currencies'

DATABASE_URI = ('mysql+mysqlconnector://' +
DATABASE_USER + ':' +
DATABASE_PASS + '@' +
DATABASE_HOST + ':' +
DATABASE_PORT + '/' +
DATABASE_DB
)

# Create Secret key for Flaskform
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MYSQL_HOST'] = DATABASE_HOST
app.config['MYSQL_USER'] = DATABASE_USER
app.config['MYSQL_PASSWORD'] = DATABASE_PASS
app.config['MYSQL_PORT'] = DATABASE_PORT
app.config['MYSQL_DB'] = DATABASE_DB

# Configure the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
mysql = SQLAlchemy(app)   


class Currency(mysql.Model):
    """
    A class used to get all the data listed in the MySQL database.

    Attributes
    ----------
    code : int
        ID-key in the database
    name : str
        the name of the currency
    symbol : str
        the symbol of the currency

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    code = mysql.Column(mysql.String(3), primary_key=True)
    name = mysql.Column(mysql.String(25))
    symbol = mysql.Column(mysql.String(6))

class Form(FlaskForm):
    """
    A class used to provide the html page with the correct data of the Database.

    Parameters
    ----------
    FlaskForm : flask
        The flask module

    Attributes
    ----------
    currencyFrom : str[]
        A list of possible currencies to convert from
    currencyTo : str[]
        A list of possible currencies to convert from
    """

    currencyFrom = SelectField('currencyFrom', choices=[])
    currencyTo = SelectField('currencyTo', choices=[])

# Route and create the different data requisistions
@app.route('/CurrencyExchanger')
def CurrencyExchanger():
    """
    Returns the view needed for the reroute of the HTML-page with its variables

    Parameters
    ----------
    currencyFrom : str[]
        A list of possible currencies to convert from (See Class Form())
    currencyTo : str[]
        A list of possible currencies to convert from (See Class Form())

    Returns
    -------
    render_template
        Returns the template needed for the reroute with the correct variables.  
    """

    form = Form()
    form.currencyFrom.choices = [(currencyFrom.code, currencyFrom.name + ", " + currencyFrom.code) for currencyFrom in Currency.query.all()]
    form.currencyTo.choices = [(currencyTo.code, currencyTo.name + ", " + currencyTo.code) for currencyTo in Currency.query.all()]

    return render_template('index.html', form = form)

# Run The Application and restart if any changes have been made   
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')