#################################################
# 1. Import Dependencies
#################################################
import os

import csv

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#################################################
# 2. Database Setup & Configuration 
#################################################

### Flask Config
app = Flask(__name__)

#################################################
# 3. Routes
#################################################
# WEBSITE (HTML + CSS/JS) ROUTE Endpoints
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/machine_learning/")
def machine_learning():
    """Return the homepage."""
    return render_template("machine-learning.html")

@app.route("/why/")
def whyCode():
    with open('./data/data.csv') as file:
        reader = csv.DictReader(file)
        chemicals = []
        for row in reader:
            chemicals.append({key: value for key, value in row.items()})
        print(chemicals)
    """Return the homepage."""
    return render_template("why.html", chemicals=chemicals)

@app.route("/aboutUs/")
def aboutUs():
    """Return the homepage."""
    return render_template("aboutUs.html")

if __name__ == "__main__":
    app.run()