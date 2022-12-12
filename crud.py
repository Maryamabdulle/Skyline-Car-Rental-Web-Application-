from model import db, User, Car, Favorite,Trip, Rate, connect_to_db, Booking


"""CREATE FUNCTIONS"""

def create_user(fname, lname, email, password, address, contact):
    """Create and return a new user."""
    user= User(
        fname=fname,
        lname=lname,
        email=email, 
        password=password,
        address=address,
        contact=contact
    )

    db.session.add(user)
    db.session.commit()


    return user 


def create_car(vehicle_type, vehicle_name, seats, Doors, Transmission, large_bag, small_bag, ac, per_day_charges, category, images):
    """Create a new car"""
    car = Car(vehicle_type= vehicle_type,
        vehicle_name= vehicle_name,
        seats= seats,
        Doors= Doors,
        Transmission= Transmission,
        large_bag= large_bag,
        small_bag= small_bag,
        ac= ac,
        per_day_charges=per_day_charges,
        category= category,
        images=images)

    db.session.add(car)
    db.session.commit()

    return car 

#add trip 



def get_trips_by_car_id(car_id):
    """getting car_id to show trips"""
    return Trip.query.filter(car_id=car_id)




def get_trips():
    """Return all trips."""
    return Trip.query.all()


def get_trip_by_id(trip_id):
    """Return a trip by primary key."""
    return Trip.query.get(trip_id)

#Don't return 
# send one car 


#for users 
def get_user():
    """Return all users."""
    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""
    return User.query.get(user_id)


def get_user_by_email(email):
    """Get a user by email."""
    return User.query.filter(User.email==email).first()

#for cars
def get_cars():
    """Return all cars."""
    return Car.query.all()


def get_car_by_id(car_id):
    """Return a car by primary key."""
    return Car.query.get(car_id)

# for favoriting cars
def add_favorite_car(car_id,user_id):
    """Create and return a new favorite."""
    favorite= Favorite(car_id=car_id, user_id=user_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite



def get_user_favorite_cars(user_id):
    """Return all favorite cars a user favorited. """
    return Favorite.query.filter_by(user_id=user_id).all()


def check_if_car_in_favorites(car_id, user_id):
    """Return True if a car exists in favorites table or else return false."""
    return True if Favorite.query.filter_by(car_id=car_id, user_id=user_id).first() else False 


def remove_favorite_car(car_id, user_id):
    """Delete a favorite car a user 'unfavorited'"""

    favorited_car= Favorite.query.filter_by(car_id=car_id, user_id=user_id).one()
    db.session.delete(favorited_car)
    db.session.commit()
    return " "


# create Trip
def create_trip(user_id, car_id):
    from datetime import datetime, timedelta
    trip = Trip(
        user_id=user_id,
        car_id=car_id,
        pick_up_location='pickuplocation',
        drop_of_location='dropofflocation',
        pick_up_date=datetime.now().date(),
        drop_of_date=datetime.now().date()+timedelta(days=2),
        pick_up_time=datetime.now(),
        drop_of_time=datetime.now()+timedelta(days=2),
        created_at = datetime.now(),
        is_active=False,
        is_canceled=False,
        is_return=True
    )
    db.session.add(trip)
    db.session.commit()
    return trip

# create favourites
def create_favourite(user_id, car_id):
    fav = Favorite(
        user_id=user_id,
        car_id=car_id
    )
    return fav


def create_booking(trip_id):

    card_number = ''
    card_code = ''
    import random
    for _ in range(16):
        card_number += str(random.randint(0, 9))

    for _ in range(3):
        card_code += str(random.randint(1, 9))

    booking = Booking(
        card_number=card_number,
        card_code=card_code,
        card_exp='02/25',
        is_canceled=False,
        is_confirmed=True,
        trip_id=trip_id
    )
    return booking


#for rating and feedback
def create_review(user_id,car_id, score, rate, trip_id):
    """Create and retur a car rating."""

    rate=Rate(user_id=user_id, car_id=car_id, score=score, rate=rate, trip_id=trip_id)
    return rate


def get_all_rates():
    """Get ratings by id."""
    return Rate.query.all()

def updating_score(rate_id, new_score):
    """create and return a car score."""
    rating=Rate.query.get(rate_id)
    rating.score=new_score


def calculating_avg(car_id):
    """Calculating the avg of the score for a car"""
    car=Car.query.get(car_id)
    sum=0
    len=0
    for car in car.rates:
        sum +=car.score
        len +=1

    avg=int(sum/len)



def add_feedback(rate_id, new_rate):
    """Create and return a car feedback."""
    rate=Rate.query.get(rate_id)
    rate.score=new_rate



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    