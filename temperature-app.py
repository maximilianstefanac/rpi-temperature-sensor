import os
import json

from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "temperatures.db"))



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

api = Api(app)

db = SQLAlchemy(app)

def convert_temperature_to_dictionary_array(temperatures):
    temperatures_array = []
    for temperature in temperatures:
        temperatures_array.append({'timestamp': temperature.timestamp.strftime('%Y.%m.%d, %H:%M:%S.%f'), 'temperature': temperature.temperature})
    return temperatures_array

class Temperature(db.Model):
        timestamp = db.Column(db.DateTime, primary_key=True)
        temperature = db.Column(db.Float, nullable=False)


class Temperatures(Resource):
    def get(self):
       return convert_temperature_to_dictionary_array(Temperature.query.order_by(Temperature.timestamp.desc()).limit(10).all())

api.add_resource(Temperatures, '/')

def create_database():
    if not os.path.exists(os.path.join(project_dir, "temperatures.db")):
         db.create_all()

if __name__ == '__main__':
    create_database()
    app.run(debug=True, host='0.0.0.0')
    