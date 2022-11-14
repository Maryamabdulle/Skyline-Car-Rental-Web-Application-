"""Seed the database"""


import os
import json
from random import choice, randint
from csv import DictReader
#from datetime import datetime 

import crud
import model
import server


os.system('dropdb cars')
os.system('createdb cars')


model.connect_to_db(server.app) #, echo= False
model.db.create_all()


def create_cars():
    """Parase CSV."""
    with open('data/vehicle.csv' , newline= "") as f:
        reader = DictReader(f)
        for row in reader:
            car=model.Car(
            vehicle_type=row["vehicle_type"],
            vehicle_name= row["vehicle_name"],
            seats=row["seats"],
            doors= row["doors"],
            Transmission= row["Transmission"],
            large_bag= row["large_bag"],
            small_bag= row["small_bag"],
            ac=row ["ac"],
            per_day_charges=row["per_day_charges"],
            category= row["category"],
            car_img=row["car_img"],
            mpg=row["mpg"]
            )
            model.db.session.add(car)
    model.db.session.commit()

create_cars()
            






