""" Models for car app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User object."""
    #Set table name as `users` for User objects
    __tablename__= "users"
    user_id = db.Column(db.Integer, primary_key= True,  autoincrement = True)
    fname = db.Column(db.String(25), nullable = False)
    email = db.Column(db.String(100),nullable = False)
    password= db.Column(db.String(30),nullable = False)

    #cars= db.relationship("Car",backref= "user")
    rates= db.relationship('Rate', backref= "users")
    #Added 
    trips=db.relationship('Trip', backref= 'user')
    # Method to identify each User instance by user_id
    def __repr__ (self):
        return f"<User id= {self.user_id} fname= {self.fname}>"
  

class Car(db.Model):
    """Car objects."""
 #set table name as `cars` for plant objects
    __tablename__= "cars"
    car_id= db.Column(db.Integer, primary_key= True,  autoincrement= True)
    vehicle_type = db.Column(db.String, nullable = False)
    vehicle_name=db.Column(db.String, nullable = False)
    seats= db.Column(db.String, nullable = False)
    doors= db.Column(db.String, nullable = False)
    Transmission= db.Column(db.String, nullable = False)
    large_bag= db.Column(db.String, nullable = False)
    small_bag= db.Column(db.String, nullable = False)
    ac = db.Column(db.String, nullable = False)
    mpg= db.Column(db.String, nullable = False)
    per_day_charges= db.Column(db.String, nullable = False)
    category=db.Column(db.String, nullable = False)
    car_img= db.Column(db.String)
    #status= 
    #Added
    trips=db.relationship('Trip', backref= 'car')


# Method to identify ear car instance by car_id and vehicle_type
    def __repr__ (self):
        return f"<Car car_id= {self.car_id},vehicle_type= {self.vehicle_type}>"


#Create SQLAlchemy relationship bettween cars and users
    #user= db.relationship("User",backref="cars")



class Trip(db.Model):
    """ Trip object belonging to User."""
    __tablename__= "trips"
    trip_id=  db.Column(db.Integer, primary_key= True,  autoincrement= True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    car_id= db.Column(db.Integer, db.ForeignKey("cars.car_id"), nullable =False)
    pick_up_location= db.Column(db.String, nullable = False)
    drop_of_location= db.Column(db.String, nullable = False)
    pick_up_date= db.Column(db.Date, nullable = False)
    drop_of_date= db.Column(db.Date, nullable = False)
    pick_up_time= db.Column(db.DateTime, nullable = False)
    drop_of_time= db.Column(db.DateTime, nullable = False)



#Method to identidy each trips instance by trip_id, car_id, and user_id
    def __repr__ (self):
        return f'<Trips trip_id={self.trip_id} car_id={self.car_id} user_id={self.user_id}>'     

    #def is_car_available(self):
        #within_another_trip_time=db.session.query(Trip).filter(Trip.car_id==self.car_id,
            #Trip.pick_up_time <= self.pick_up_time,Trip.drop_of_time>=self.drop_of_time).count()

    #if within_another_trip_time>0:
        #return {"result": False, "reason": "This car has already been booked "}




class Rate(db.Model):
    """Rating cars."""
    __tablename__= "rates"
    rate_id= db.Column(db.Integer, primary_key= True,  autoincrement= True)
    score = db.Column(db.Integer)
    feedback= db.Column(db.Text)
    trip_id= db.Column(db.Integer, db.ForeignKey("trips.trip_id"), nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    car_id= db.Column(db.Integer, db.ForeignKey("cars.car_id"), nullable=False)
#Create SQLALchemy relationship between trips and rate
    trip= db.relationship("Trip",backref="rates")


    def __repr__ (self):
        return f'<Rate rate_id{self.rate_id} score={self.score}>'
 


class Favorite(db.Model):
    """A favorite car objecr which is the cars that user 'favorites'."""
    __tablename__= "favorites"

    favorites_id= db.Column(db.Integer, primary_key= True,  autoincrement= True)
    car_id= db.Column(db.Integer, db.ForeignKey("cars.car_id"), nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


#Adding relationship
    car= db.relationship("Car", backref= "favorites")
    user= db.relationship("User", backref= "favorites")


    def __repr__ (self):
        return f'<Favorite car_id= {self.car_id}user_id= {self.user_id}>'


def connect_to_db(flask_app, db_uri= "postgresql:///cars", echo=False ):
    """Connect the database to Flask app."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")
    

def test_data():
    """Create some sample data."""
    #In case this is run more than once, empty out existing data
    User.query.delete()
    Car.query.delete()

#Exmaple data for users, cars
test_user= User(user_id=1,
            email= "user1@test.com",
            password= "testing",
            fname= "usertest")

# Economy = Car(car_id=1,
#            vehicle_name= "Ford Fiesta",
#            vehicle_type= "Economy",
#            seats= "5 Seats",
#            doors= "4 Doors",
#            Transmission= "Automati Transmission",
#            large_bag= "1 Large Bag",
#            small_bag= "1 Small Bag",
#            AC= "A/C",
#            mpg= "27/35 27-35",
#            per_day_charges= "$145",
#            category= "Small to Full Size",
#            car_img= "Ford_Fiesta.png")



# Intermediate_SUV = Car(car_id=2,
#            vehicle_name= "Mazda CX-5",
#            vehicle_type= "Intermediate SUV",
#            seats= "5 Seats",
#            doors= "4 Doors",
#            Transmission= "Automati Transmission",
#            large_bag= "1 Large Bag",
#            small_bag= "1 Small Bag",
#            AC= "A/C",
#            mpg= "27/35 27-35 mpg",
#            per_day_charges= "$189",
#            category= "SUVs",
#            car_img= "Mazda_CX-5.png")

# Premium = Car(car_id=3,
#            vehicle_name= "Volkswagen Passat",
#            vehicle_type= "Premium",
#            seats= "5 Seats",
#            doors= "4 Doors",
#            Transmission= "Automati Transmission",
#            large_bag= "2 Large Bag",
#            small_bag= "2 Small Bag",
#            AC= "A/C",
#            mpg= "18-29 mpg",
#            per_day_charges= "$198",
#            category= "Luxury & Convertibles",
#            car_img= "Volkswagen_ Passat .png")

#db.session.add_all([test_user, Economy,Intermediate_SUV,Premium])
#db.session.commit()


if __name__ == "__main__":
    from server import app

    connect_to_db(app) 
    db.create_all()
    