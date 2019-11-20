import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import Adafruit_DHT

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "temperatures.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Temperature(db.Model):
        timestamp = db.Column(db.DateTime, primary_key=True)
        temperature = db.Column(db.Float, nullable=False)

def read_temperature():
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

temperature = Temperature(timestamp = datetime.now(), temperature= 12.0)

db.session.add(temperature)
db.session.commit()