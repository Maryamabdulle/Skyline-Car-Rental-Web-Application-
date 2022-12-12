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

#model.db.session.add_all(cars_in_db)
#mode.dbsession.commit()


cars_in_db= model.Car.query.all()

print(cars_in_db)

for n in range(10):
    email=f'user{n}@test.com'
    password='test'

    fname= f'username{n}'
    lname= f'userlastname{n}'
    address=f'homeaddress{n}'
    contact= f'phonenumber{n}'

    user=crud.create_user(fname, lname, email, password, address, contact )
    model.db.session.add(user)
    #create trips to commit (here)
    model.db.session.commit()

    # for _ in range(2):
    #     random_car=choice(cars_in_db)
    #     scoresList = [1, 2, 3, 4, 5]
    #     reviewList = ['bad experience', 'not recommended', 'average', 'good', 'recommended']
    #     selection = randint(0, 4)
    #     score=scoresList[selection]
    #     feedback= reviewList[selection]

    #     trip = crud.create_trip(user_id=user.user_id, car_id=random_car.car_id)

    #     booking = crud.create_booking(trip_id=trip.trip_id)
    #     model.db.session.add(booking)
        
    #     rate= crud.create_review(user_id=user.user_id, car_id=random_car.car_id, score=score, rate=feedback, trip_id=trip.trip_id)
    #     model.db.session.add(rate)

    #     fav = crud.create_favourite(user_id=user.user_id, car_id=random_car.car_id)
    #     model.db.session.add(fav)

model.db.session.commit()







