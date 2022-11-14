from model import db, User, Car, Favorite, connect_to_db


"""CREATE FUNCTIONS"""

def create_user(fname, email,password):
    """Create and return a new user."""
    user= User(fname=fname, email=email, password=password)

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


"""GET FUNCTIONS"""

def get_user():
    """Return all users."""
    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""
    return User.query.get(user_id)


def get_user_by_email(email):
    """Get a user by email."""
    return User.query.filter(User.email==email).first()


def get_cars():
    """Return all cars."""
    return Car.query.all()


def get_car_by_id(car_id):
    """Return a car by primary key."""
    return Car.query.get(car_id)

def add_favorite_car(car_id,user_id):
    """Create and return a new favorite."""
    favorite= Favorite(car_id=car_id, user_id=user_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_user_favorite_cars(user_id):
    """Return all favorite cars a user favorited. """
    return Favorite.query.filter_by(user_id=user_id).all()


def check_if_car_in_favorites(car_id):
    """Return True if a car exists in favorites table or else return false."""
    return True if Favorite.query.filter_by(car_id=car_id).first() else False 


def remove_favorite_car(car_id):
    """Delete a favorite car a user 'unfavorited'"""

    favorited_car= Favorite.query.filter_by(car_id=car_id).one()
    db.session.delete(favorited_car)
    db.session.commit()
    return " "



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    