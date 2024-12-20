"""Server for car app."""

from flask import (Flask,
    render_template,
    request,
    flash,
    session,
    redirect,
    jsonify,
    json,
    url_for, Response, make_response)
from model import connect_to_db, db, User, Trip, Rate, Favorite, Car, Booking
import crud
from jinja2 import StrictUndefined
import os
import requests
import hashlib
from dotenv import load_dotenv
from helper import convert_date, get_mpg, compare_dates, convert_datetime, check_card_expfrmt
from datetime import datetime, timedelta
import random
from flask_mail import Mail, Message



load_dotenv()
app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
apikey= os.environ['API']
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = os.environ['EMAIL'],
	MAIL_PASSWORD = os.environ['PASS']
)
mail = Mail(app)


#Google Map function

# address=
# url=
#request=requests.get(url)json()


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/test/route')
def test_route():
    return 'Welcome to'

@app.route("/")
def homepage():
    """View homepage."""
    cars = crud.get_cars()

    carousal_cars = ['homepage1.png', 'Tesla Model 3.png', '6home.png']

    suvs = Car.query.filter(Car.category.like('%SUV%')).all()[0:3]
    small_full_size = Car.query.filter(Car.category.like('%Small to Full Size%')).all()[0:3]
    luxury = Car.query.filter(Car.category.like('%Luxury & Convertibles%')).all()[0:3]

    cars = suvs + small_full_size + luxury

    fcars = []
    if (cars):
        for i in range(0, 5):
            car = random.choice(cars)
            if car not in fcars:
                fcars.append(car)

    return render_template("homepage.html",
                            fcars=fcars,
                            carousal_cars=carousal_cars,
                            suvs=suvs,
                            small_full_size=small_full_size,
                            luxury=luxury)

@app.route("/login")
def display_login():
    """View user login and registration."""
    users= crud.get_user()
    cars=crud.get_cars()
    return render_template("login.html", users=users, cars=cars)


@app.route("/login" ,methods= ["POST"])
def process_login():
    """Process user login."""

    #Return email entered in login form
    email= request.form.get("email")
    print(email)
    #Return password entered in login form
    password= request.form.get("password")
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    user=crud.get_user_by_email(email)
    print(user)
    fname=request.form.get("fname")
    if not user or user.password != hash_password or fname!=user.fname:
        flash ("The email, password, or the name you entered was incorrect.", 'error')
        return redirect("/")
    else:
        session["user_email"]= user.email
        session["fname"]= user.fname
        session["user_id"]= user.user_id
        flash (f"Welcome back, {user.fname}", 'success')
    return redirect ("/")


@app.route("/register")
def display_register():
    """Viewe can register"""
    return render_template("Register.html")

@app.route("/register" , methods=["POST"])
def signup_user():
    """Creates a new user."""
    fname=request.form.get("fname")
    lname = request.form.get('lname')
    email= request.form.get ("email")
    password= request.form.get("password")
    address = request.form.get("address")
    contact = request.form.get("contact")



    user= crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again", 'error')
        return redirect("/register")

    else:
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        crud.create_user(fname, lname, email, hash_password, address, contact)
        flash(f"Account created! Welcome {fname}. Please log in.", 'success')
        return redirect("/")


#create user log out, display only when user is logged in
@app.route("/logout", methods=["POST"])
def logout():
    """user must be logged in to logout."""
    user=session["user_email"]
    if user:
        session.pop("user_email", None)
        session.pop("fname", None)
        session.pop("user_id", None)
        session.clear()
        return redirect("/")
    else:
        return redirect("/")


@app.route("/profile")
def show_user_profile():
    """Displays users profile page."""
    user_email=session.get("user_email")

    if not user_email:
        return redirect(url_for('homepage'))

    user=crud.get_user_by_email(user_email)
    cars=crud.get_cars()
    user_id= session["user_id"]


    favorite_cars= crud.get_user_favorite_cars(user_id)

    trips = Trip.query.filter_by(user_id=user_id).all()
    active_trips = []
    past_trips = []
    future_trips = []
    date_now = datetime.now().date()
    for trip in trips:
        if trip.is_active:
            # present
            if date_now >= trip.pick_up_date:
                active_trips.append(trip)
            # future
            if date_now < trip.pick_up_date:
                future_trips.append(trip)
            # past
            if date_now > trip.drop_of_date:
                future_trips.append(trip)
        if not trip.is_active and trip.is_return:
            past_trips.append(trip)
        # if not trip.is_active:
        #     past_trips.append(trip)

    return render_template("profile/main.html",
                                        user=user,
                                        favorite_cars=favorite_cars ,
                                        cars=cars,
                                        active_trips=active_trips,
                                        past_trips=past_trips,
                                        future_trips=future_trips)


@app.route('/cancel-trip', methods=['POST'])
def cancel_trip():
    trip_id = request.form.get('trip_id')

    now = datetime.now()
    trip = Trip.query.filter_by(trip_id=trip_id).first()
    # after trip pickupdate

    '''
        # calculate and return days
        days = drop_of_date - pick_up_date
        days = days.days

        pickupdate - currentdate should be greater than one day
    '''

    days = trip.pick_up_date - now.date()
    print('----------->', days)
    if trip and days.days > 1:
    # after creation of trip
    # if trip and  now >= (trip.created_at + timedelta(days=1)):
        # print('----->', now)
        # print('----->', trip.pick_up_date + timedelta(days=1))
        trip.is_canceled = True
        trip.is_active = False
        db.session.commit()
        flash('Reservation canceled!', 'success')
        return redirect(url_for('show_user_profile'))
    else:
        flash('You can not cancel the reservation before 24 hours!', 'error')
        return redirect(url_for('show_user_profile'))



@app.route('/return-vehicle', methods=["POST"])
def return_vehicle():

    user_id =session.get('user_id')
    if not user_id:
        return redirect(url_for('homepage'))

    user = crud.get_user_by_id(user_id=user_id)

    trip_id = request.form.get('trip_id')
    car_id = request.form.get('car_id')
    trip = Trip.query.filter_by(trip_id=trip_id).one()

    is_rating = request.form.get('rating')

    if trip and trip.is_active:
        trip.is_return = True
        trip.is_active = False
        db.session.commit()

    if is_rating == 'true':
        score = request.form.get('rate')
        review = request.form.get('review')

        rating = Rate(score=score, rate=review, trip_id=trip.trip_id, user_id=user.user_id, car_id=car_id)
        db.session.add(rating)
        db.session.commit()
        flash('The car Returned sucessfully with your review! Thank you', 'success')
    else:
        flash('The car has been returned successfully! Thank you', 'success')


    return redirect(url_for('show_user_profile'))
    pass


@app.route("/cars")
def all_car():
    """View all cars."""
    cat = request.args.get('cat')

    if cat == 'suv':
        print('---------->', cat)
        cars= Car.query.filter(Car.category.like('%SUV%')).all()
        return render_template("all_vehicles.html", cars=cars)

    if cat == 'small-to-full':
        cars= Car.query.filter(Car.category.like('%Small to Full Size%')).all()
        return render_template("all_vehicles.html", cars=cars)

    if cat == 'luxury':
        cars= Car.query.filter(Car.category.like('%Luxury & Convertibles%')).all()
        return render_template("all_vehicles.html", cars=cars)

    if cat == 'all-cars':
        cars= crud.get_cars()
        print('------>', cars)
        return render_template("all_vehicles.html", cars=cars)

    cars= crud.get_cars()
    return render_template("all_vehicles.html", cars=cars)



@app.route("/vehicle-cat-ajx", methods=['POST'])
def vehicle_cat_ajx():
    """View all cars."""
    cat = request.form.get('cat')
    cars = []

    if cat == 'suv':
        print('---------->', cat)
        cars= Car.query.filter(Car.category.like('%SUV%')).all()

    if cat == 'small-to-full':
        cars= Car.query.filter(Car.category.like('%Small to Full Size%')).all()

    if cat == 'luxury':
        cars= Car.query.filter(Car.category.like('%Luxury & Convertibles%')).all()

    json_cars = []

    for item in cars:
        car = {
            'car_id':item.car_id,
            'vehicle_type': item.vehicle_type,
            'vehicle_name': item.vehicle_name,
            'seats': item.seats,
            'doors': item.doors,
            'Transmission': item.Transmission,
            'mpg': item.mpg,
            'per_day_charges': item.per_day_charges,
            'category': item.category,
            'car_img': item.car_img.strip()
        }
        json_cars.append(car)

    response = make_response(jsonify(json_cars), 200)
    print(json_cars)
    return response


@app.route("/cars/search")
def cars_search():
    price = request.args.get('price')
    mpg = request.args.get('mpg')
    seats = request.args.get('seats')

    price_cars = []
    mpg_cars = []
    seats_cars = []
    searched_cars = []
    
    cars= crud.get_cars()

    if not price or len(price) <= 0 or not mpg or len(mpg) < 0 or not seats and len(seats) < 0:
        return render_template("cars_search.html", cars=cars)

    price_range = price.split('-')
    for car in cars:
        car_ppd = float(car.per_day_charges.strip()[1:])
        if car_ppd >= float(price_range[0]) and car_ppd <= float(price_range[1]):
            price_cars.append(car)

    for car in price_cars:
        car_mpg = car.mpg.strip().split('-')
        print(car.mpg)
        if type(car_mpg) == list:
            try:
                if float(mpg) >= float(car_mpg[0]) and float(mpg) <= float(car_mpg[1]):
                    mpg_cars.append(car)
            except:
                pass

    for car in mpg_cars:
        print('here')
        seats_db = int(car.seats.strip().split(' ')[0])
        if seats_db == int(seats):
            seats_cars.append(car)

    seats_cars = seats_cars
    return render_template("cars_search.html", cars=seats_cars)


@app.route('/vehicle-sort')
def vehicle_sort():

    cat = request.args.get('cat')

    cars = []
    if cat == 'suv':
        cars = Car.query.filter(Car.category.like('%SUV%')).all()
    elif cat == 'small-to-full':
        cars = Car.query.filter(Car.category.like('%Small to Full Size%')).all()
    elif cat == 'luxury':
        cars = Car.query.filter(Car.category.like('%Luxury & Convertibles%')).all()
    else:
        cars = crud.get_cars()

    sort_type = request.args.get('sort')
    if not sort_type or len(sort_type) < 1:
        return redirect(url_for('all_car'))

    if sort_type == 'price':
        sorted_cars = sorted(cars, key=lambda x: float(x.per_day_charges.strip()[1:]))
    if sort_type == 'seats':
        sorted_cars = sorted(cars, key=lambda x: float(x.seats.strip().split(' ')[0]), reverse=True)
    if sort_type == 'mpg':
        sorted_cars = sorted(cars, key=lambda x: get_mpg(x), reverse=True)
    
    return render_template("all_vehicles.html", cars=sorted_cars)



@app.route('/vehicle-sort-ajx', methods=['POST'])
def vehicle_sort_ajx():


    cat = request.form.get('cat')

    cars = []
    if cat == 'suv':
        cars = Car.query.filter(Car.category.like('%SUV%')).all()
    elif cat == 'small-to-full':
        cars = Car.query.filter(Car.category.like('%Small to Full Size%')).all()
    elif cat == 'luxury':
        cars = Car.query.filter(Car.category.like('%Luxury & Convertibles%')).all()
    else:
        cars = crud.get_cars()


    sort_type = request.form.get('sort')

    if sort_type == 'price':
        sorted_cars = sorted(cars, key=lambda x: float(x.per_day_charges.strip()[1:]))
    if sort_type == 'seats':
        sorted_cars = sorted(cars, key=lambda x: float(x.seats.strip().split(' ')[0]), reverse=True)
    if sort_type == 'mpg':
        sorted_cars = sorted(cars, key=lambda x: get_mpg(x), reverse=True)
    
    json_cars = []

    for item in sorted_cars:
        car = {
            'car_id':item.car_id,
            'vehicle_type': item.vehicle_type,
            'vehicle_name': item.vehicle_name,
            'seats': item.seats,
            'doors': item.doors,
            'Transmission': item.Transmission,
            'mpg': item.mpg,
            'per_day_charges': item.per_day_charges,
            'category': item.category,
            'car_img': item.car_img.strip()
        }
        json_cars.append(car)

    response = make_response(jsonify(json_cars), 200)
    print(json_cars)
    return response
    pass



@app.route('/get-cars-ajx', methods=['POST'])
def get_cars_ajx():
    if request.form.get('msg') == 'getAll':
        cars = list(crud.get_cars())
        json_cars = []

        for item in cars:
            car = {
                'car_id':item.car_id,
                'vehicle_type': item.vehicle_type,
                'vehicle_name': item.vehicle_name,
                'seats': item.seats,
                'doors': item.doors,
                'Transmission': item.Transmission,
                'mpg': item.mpg,
                'per_day_charges': item.per_day_charges,
                'category': item.category,
                'car_img': item.car_img.strip()
            }
            json_cars.append(car)
        response = make_response(jsonify(json_cars), 200)
        print(json_cars)
        return response
    pass


@app.route("/favourite-cars")
def favourite_cars():
    if not session.get('user_email'):
        flash('Please login to view/add your favourite cars', 'error')
        return redirect(url_for('all_car'))
    """View favourites cars."""
    cars= crud.get_cars()
    favourite_cars = []
    for car in cars:
        if car.check_if_car_in_favorites(session.get('user_id')):
            favourite_cars.append(car)

    return render_template("favourite_cars.html", cars=favourite_cars)



@app.route("/cars/<car_id>")
def show_car(car_id):
    """Show details on a particular car."""

    car= crud.get_car_by_id(car_id)
    cars= crud.get_cars()

    ratings = []
    for c in car.trips:
        # note each trip should only have one review
        for t in c.rates:
            ratings.append(t)
    print(ratings)

    return render_template("vehicle_details.html", cars=cars , car=car, ratings=ratings)

#-----------------------------BOOKING PAGE---------------
@app.route("/trip")
def show_trip_form():
    cars= crud.get_cars()
    import os
    baseDir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(baseDir, 'data/map.json')
    with open(data_file, "r") as read_file:
        data1 = json.load(read_file)

    data_file = os.path.join(baseDir, 'data/returnlocations.json')
    with open(data_file, 'r') as read_file:
        data2 = json.load(read_file)
    """Show the reservation template"""
    return render_template("reservations.html", apikey=apikey, trip_page=True, cars=cars, data1=data1, data2=data2)
#show form in this route



# ajax request for checking user login
@app.route('/is-logged-in', methods=['POST'])
def is_logged_in():
    if session.get('user_id') and session.get('user_email'):
        return Response('logged', status=200, mimetype='text/html')
    else:
        return Response('error', status=400, mimetype='text/html')


# ajax request
@app.route('/validate_dates', methods=['POST'])
def validate_dates():
    car_id = request.form.get('car_id')
    pickDate = request.form.get('pickDate')
    dropDate = request.form.get('dropDate')

    pick_up_date = convert_date(pickDate)
    drop_of_date = convert_date(dropDate)

    # pickup or dropoff should not be in past date
    now = datetime.now()
    if pick_up_date.date() < now.date() or drop_of_date.date() < now.date():
        # flash('booking dates should not be in the past dates', 'error')
        return Response("datePast", status=400, mimetype='text/html')

    # check form dates
    # pickup date should be less than dropoff date
    if not compare_dates(pick_up_date, drop_of_date):
        # flash('Pickup date cannot be greater than drop off date', 'error')
        return Response("cmpDate", status=400, mimetype='text/html')

    # get old trip dates for this car
    trips= Trip.query.filter_by(car_id=car_id).all()

    for t in trips:
        if t.is_active:
            # new booking dates should not be between old active booking
            if pick_up_date.date() <= t.pick_up_date or pick_up_date.date() <= t.drop_of_date:
                # flash('Dates already booked.', 'error')
                return Response("bookedDate", status=400, mimetype='text/html')

    # calculate and return days
    days = drop_of_date - pick_up_date
    days = days.days

    return Response(f"okDate,{days}", status=200, mimetype='text/html')
    pass


# create booking ajax
@app.route('/create-booking', methods=['POST'])
def create_booking():

    car_id = request.form.get('carId')
    user_id = session.get('user_id')

    if not user_id:
        flash('Login required', 'error')
        return redirect(url_for('display_login'))

    pick_up_location= request.form.get("pickLoc")
    drop_of_location= request.form.get("dropLoc")

    pick_up_date= request.form.get("pickDate")
    drop_of_date= request.form.get("dropDate")

    pick_up_time= convert_datetime(f"{pick_up_date} {request.form.get('pickTime')}:00")
    drop_of_time= convert_datetime(f"{drop_of_date} {request.form.get('dropTime')}:00")

    pick_up_date = convert_date(pick_up_date)
    drop_of_date = convert_date(drop_of_date)


    card_number = request.form.get('cardNumber')
    card_code = request.form.get('cardCode')
    card_exp = request.form.get('cardExp')

    user = User.query.filter_by(user_id=user_id).first()
    car = Car.query.filter_by(car_id=car_id).first()

    print(car)

    # get old trip dates for this car
    trips= Trip.query.filter_by(car_id=car_id).all()

    for t in trips:
        if t.is_active:
            # new booking dates should not be between old active booking
            if pick_up_date.date() <= t.pick_up_date or pick_up_date.date() <= t.drop_of_date:
                return Response('booked', status=400, mimetype='text/html')

    trip = Trip(
        user_id= user.user_id,
        car_id= car.car_id,
        pick_up_location= pick_up_location,
        drop_of_location= drop_of_location,
        pick_up_date= pick_up_date,
        drop_of_date= drop_of_date,
        pick_up_time= pick_up_time,
        drop_of_time= drop_of_time,
        is_active = True
    )
    db.session.add(trip)
    db.session.commit()

    booking = Booking(
        card_number=card_number,
        card_code=card_code,
        card_exp=card_exp,
        trip_id=trip.trip_id
    )
    db.session.add(booking)
    db.session.commit()

    return Response("ok", status=200, mimetype='text/html')


# @app.route("/trip" , methods= ["POST"])
# def car_reservation():

#     # if not logged in
#     if not session.get('user_id') or not session.get('user_email'):
#         flash('please log into the system first', 'error')
#         return redirect(url_for('car_reservation'))


#     """User can book a car"""
#     car_id=request.form.get("car")
#     pick_up_location= request.form.get("pickLocation")
#     drop_of_location= request.form.get("dropLocation")

#     pick_up_date= request.form.get("pick_up_date")
#     drop_of_date= request.form.get("drop_of_date")

#     pick_up_time= convert_datetime(f"{pick_up_date} {request.form.get('pick_up_time')}:00")
#     drop_of_time= convert_datetime(f"{drop_of_date} {request.form.get('drop_of_time')}:00")

#     pick_up_date = convert_date(pick_up_date)
#     drop_of_date = convert_date(drop_of_date)

#     # pickup or dropoff should not be in past date
#     now = datetime.now()
#     if pick_up_date.date() < now.date() or drop_of_date.date() < now.date():
#         flash('booking dates should not be in the past dates', 'error')
#         return redirect(url_for('show_trip_form'))

#     # check form dates
#     # pickup date should be less than dropoff date
#     if not compare_dates(pick_up_date, drop_of_date):
#         flash('pickup date cannot be greater than drop off date', 'error')
#         return redirect(url_for('show_trip_form'))

#     # get old trip dates for this car
#     trips= Trip.query.filter_by(car_id=car_id).all()

#     for t in trips:
#         if t.is_active:
#             # new booking dates should not be between old active booking
#             if pick_up_date.date() <= t.pick_up_date or pick_up_date.date() <= t.drop_of_date:
#                 flash('Dates already booked.', 'error')
#                 return redirect(url_for('show_trip_form'))

#     # if everything is good
#     # booking data
#     car = Car.query.filter(Car.car_id==car_id).first()
#     user = User.query.filter(User.user_id==session['user_id']).first()
#     days = drop_of_date - pick_up_date
#     booking = {
#         'user': user.user_id,
#         'fname': user.fname,
#         'car': car.car_id,
#         'car_ppd': car.per_day_charges,
#         'car_name': car.vehicle_name,
#         'pick_location': pick_up_location,
#         'drop_location': drop_of_location,
#         'pick_date': pick_up_date.date().strftime('%Y-%m-%d'),
#         'drop_date': drop_of_date.date().strftime('%Y-%m-%d'),
#         'pick_time': pick_up_time.time().strftime('%I:%M:%S'),
#         'drop_time': drop_of_time.time().strftime('%I:%M:%S'),
#         'total_days': days.days,
#         'amount': days.days * float(car.per_day_charges[1:])
#     }

#     # store is session
#     session['booking'] = booking

#     return render_template("booking_confirmation.html", booking=booking, trip_page=True)



# @app.route('/confirm-booking', methods=['POST', 'GET'])
# def confirm_booking():

#     car_id = request.form.get('car_id')
#     user_id = request.form.get('user_id')

#     pick_up_location= request.form.get("pick_location")
#     drop_of_location= request.form.get("drop_location")

#     pick_up_date= request.form.get("pick_date")
#     drop_of_date= request.form.get("drop_date")

#     pick_up_time= convert_datetime(f"{pick_up_date} {request.form.get('pick_time')}")
#     drop_of_time= convert_datetime(f"{drop_of_date} {request.form.get('drop_time')}")

#     pick_up_date = convert_date(pick_up_date)
#     drop_of_date = convert_date(drop_of_date)

#     # payment info
#     confirm_btn = request.form.get('confirm')

#     card_number = request.form.get('cardNumber')
#     card_code = request.form.get('cardCode')
#     card_exp = request.form.get('cardExp')


#     if len(card_number) < 16 or len(card_code) != 3 or not check_card_expfrmt(card_exp) or confirm_btn != '1':
#         # dont process
#         if session.get('booking') and len(session.get('booking'))>0:
#             flash('please fill the payment info in correct format', 'error')
#             return render_template("booking_confirmation.html", booking=session.get('booking'), trip_page=True)
#         else:
#             return redirect(url_for('show_trip_form'))


#     user = User.query.filter_by(user_id=user_id).first()
#     car = Car.query.filter_by(car_id=car_id).first()

#     # get old trip dates for this car
#     trips= Trip.query.filter_by(car_id=car_id).all()

#     for t in trips:
#         if t.is_active:
#             # new booking dates should not be between old active booking
#             if pick_up_date.date() <= t.pick_up_date or pick_up_date.date() <= t.drop_of_date:
#                 flash('Dates already booked.', 'error')
#                 return redirect(url_for('show_trip_form'))

#     trip = Trip(
#         user_id= user.user_id,
#         car_id= car.car_id,
#         pick_up_location= pick_up_location,
#         drop_of_location= drop_of_location,
#         pick_up_date= pick_up_date,
#         drop_of_date= drop_of_date,
#         pick_up_time= pick_up_time,
#         drop_of_time= drop_of_time,
#         is_active = True
#     )
#     db.session.add(trip)
#     db.session.commit()

#     booking = Booking(
#         card_number=card_number,
#         card_code=card_code,
#         card_exp=card_exp,
#         trip_id=trip.trip_id
#     )
#     db.session.add(booking)
#     db.session.commit()

#     # redirect based on sessions
#     booking = session.get('booking')
#     if booking:
#         session.pop('booking', None)
#         if session.get('booking'):
#             del session['booking']
#         # redirect to that car page
#         flash('Booking successfull', 'success')
#         return render_template('booking_success.html', booking=booking, trip_page=True)
#     return redirect(url_for('show_trip_form'))

#show certain dates when cars are books for the dates the user selected
# @app.route('trip/')
# def dates_unavailable():
#     """User can't book a specific car. """



# #let users be able to cancle a booking
# @app.route('/trip')
# def cancel_booking():
    """"User can cancel reservation."""



@app.route("/favorite_action/<car_id>", methods=["POST"])
def update_favorite(car_id):
    """Allows user to save a car to their profile."""
    #create a variable representing user in a session
    user_email= session.get("user_email")

    if not user_email:
        flash('Please login to favorite cars!', 'error')
        return redirect(url_for('show_car', car_id=car_id))
#('show_car', car_id=car_id))
#return redirect(url_for('homepage'))
    # get the car object
    car=crud.get_car_by_id(car_id)
    user_id= session["user_id"]

    user = User.query.filter_by(user_id=user_id, email=user_email).one()


    #if current user is logged in
    if user:
        #If user has already saved the car, remove favorite.
        #Function from crud will return true/flase
        response= crud.check_if_car_in_favorites(car_id, user.user_id)
        pageName = request.form.get('pageName')
        if response:
            #unfill the fav button and remove from session.
            crud.remove_favorite_car(car_id, user.user_id)

            # page_name = request.form.get('page')
            # print(page_name)
            # if page_name == 'fav':
            #     flash('car removed from favourites', 'success')
            #     # return redirect(url_for('favourite_cars'))
            # else:
            #     flash('car removed from favourites', 'success')
                # return redirect(url_for('all_car'))
            
            flash('Car removed from favorites', 'success')
            if pageName == 'homepage':
                return redirect(url_for('homepage'))
            if pageName == 'favourites':
                return redirect(url_for('favourite_cars'))
            if pageName == 'details':
                return redirect(url_for('show_car', car_id=car_id))
            if pageName == 'cars':
                return redirect(url_for('all_car'))

        #Otherwise, create new fav for user.
        else:
            user_id= session["user_id"]
            favorite =crud.add_favorite_car(car_id, user_id)
            flash('Car added to favorites', 'success')

            if pageName == 'homepage':
                return redirect(url_for('homepage'))
            if pageName == 'favourites':
                return redirect(url_for('favourite_cars'))
            if pageName == 'details':
                return redirect(url_for('show_car', car_id=car_id))
            if pageName == 'cars':
                return redirect(url_for('all_car'))



@app.route("/check_favorites/<car_id>")
def check_favorite_car(car_id):
    """Check if user saved car to profile"""
    response = crud.check_if_car_in_favorites(car_id)
    if response == True:
        return json.dumps(True)
    else:
        return json.dumps(False)


@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/handle-email', methods=['POST'])
def handle_email():
    client_email = request.form.get('email')
    client_msg = request.form.get('msg')

    your_recieving_email_account = os.environ['RECIEVER']

    try:
        msg = Message("MESSAGE",
        sender="test",
        recipients=[your_recieving_email_account])
        msg.body = f"sender: {client_email}\nmessage: {client_msg}"
        mail.send(msg)


        flash('Your message has been sent!', 'success')
        return redirect(url_for('homepage'))
    except:
        flash('can not send email at the moment', 'error')
        return redirect(url_for('homepage'))






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
