from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_sqlalchemy import SQLAlchemy

import os

# Create Flask Application
app = Flask(__name__)

# Database Variables
SECRET_KEY = os.urandom(32)

DATABASE_HOST   = '127.0.0.1'
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
    code = mysql.Column(mysql.String(3), primary_key=True)
    name = mysql.Column(mysql.String(25))
    symbol = mysql.Column(mysql.String(6))

class Form(FlaskForm):
    currencyFrom = SelectField('currencyFrom', choices=[])
    currencyTo = SelectField('currencyTo', choices=[])

# Route and create the different data requisistions
@app.route('/CurrencyExchanger')
def CurrencyExchanger():
    form = Form()
    form.currencyFrom.choices = [(currencyFrom.code, currencyFrom.name + ", " + currencyFrom.code) for currencyFrom in Currency.query.all()]
    form.currencyTo.choices = [(currencyTo.code, currencyTo.name + ", " + currencyTo.code) for currencyTo in Currency.query.all()]

    return render_template('index.html', form = form)

# Run The Application and restart if any changes have been made   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')