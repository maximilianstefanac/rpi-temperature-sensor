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
        humidity = db.Column(db.Float, nullable=False)

def read_temperature_and_humidity():
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        return { 'temperature':temperature, 'humidity':humidity }

if not os.path.exists(os.path.join(project_dir, "temperatures.db")):
        db.create_all()

sensor_data = read_temperature_and_humidity()
temperature = Temperature(timestamp = datetime.now(), temperature=sensor_data['temperature'], humidity=sensor_data['humidity'])

db.session.add(temperature)
db.session.commit()