"""Server for car app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, json
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os 




app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


 # Add routes and view functions!




@app.route("/")
def homepage():
    """View homepage."""

    cars= crud.get_cars()
    return render_template("homepage.html", cars=cars)

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
    user=crud.get_user_by_email(email)
    print(user)
    if not user or user.password != password:
        flash ("The email or password you entered was incorrect.")
        return redirect("/")
    else: 
        session["user_email"]= user.email
        session["fname"]= user.fname
        session["user_id"]= user.user_id
        flash (f"Welcome back, {user.fname}")
    return redirect ("/")


@app.route("/register")
def display_register():
    """Viewe can register"""
    return render_template("Register.html")

@app.route("/register" , methods=["POST"])
def signup_user():
    """Creates a new user."""
    fname=request.form.get("fname")
    email= request.form.get ("email")
    password= request.form.get("password")


    user= crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again")
        return redirect("/login")

    else: 
        crud.create_user(fname, email,password)
        flash(f"Account created! Welcome{fname}.Please log in.")
        return redirect("/")


#create user log out, display only when user is logged in 
@app.route("/logout", methods=["POST"])
def logout():
    """user must be logged in to logout."""
    user=session["user_email"]
    if user:
        session.pop("user_email", None)
        session.pop("fname", None)
        return redirect("/")
    else:
        return redirect("/")
    

@app.route("/profile")
def show_user_profile():
    """Displays users profile page."""
    user_email=session["user_email"]
    user=crud.get_user_by_email(user_email)
    cars=crud.get_cars()
    user_id= session["user_id"]


    favorite_cars= crud.get_user_favorite_cars(user_id)
   #print(favorite_cars)

    return render_template("profile.html", user=user, favorite_cars=favorite_cars , cars=cars)


@app.route("/cars")
def all_car():
    """View all cars."""
    cars= crud.get_cars()
    print (cars)
    return render_template("all_vehicles.html", cars=cars)



@app.route("/cars/<car_id>")
def show_car(car_id):
    """Show details on a particular car."""

    car= crud.get_car_by_id(car_id)
    cars= crud.get_cars()

    return render_template("vehicle_details.html", cars=cars , car=car)

#-----------------------------BOOKING PAGE---------------
access=os.environ["access_token"]

avis=os.environ("/avis_token")
avis_url="https://www.avis.com/webapi/locations/suggestions/mesa/en_US"

#@app.route("/access/", methods=["POST"])


@app.route("/access")
def send_api_token():
    "sends api token."
    return access



@app.route('/trip/' , methods= ["POST","GET"])
def car_reservation():
    """User can book a car"""
    pick_up_location= request.form.get("pick_up_location")
    drop_of_location= request.form.get("drop_of_location")
    pick_up_date= request.form.get("pick_up_date")
    drop_of_date= request.form.get("drop_of_date")
    pick_up_time= request.form.get("pick_up_time")
    drop_of_time= request.form.get("drop_of_time")


    
 #list1
    return render_template("reservations.html", pick_up_location=pick_up_location,drop_of_location= drop_of_location,  pick_up_date= pick_up_date,drop_of_date= drop_of_date, pick_up_time= pick_up_time, drop_of_time=drop_of_time )
    # return render_template("reservations.html")
 


@app.route("/favorite_action/<car_id>", methods=["POST"])
def update_favorite(car_id):
    """Allows user to save a car to their profile."""
    #create a variable representing user in a session
    user= session["user_email"]

    # get the car object
    car=crud.get_car_by_id(car_id)
    user_id= session["user_id"]


    #if current user is logged in
    if user:
        #If user has already saved the car, remove favorite.
        #Function from crud will return true/flase
        response= crud.check_if_car_in_favorites(car_id)
        if response:
            #unfill the fav button and remove from session.
            crud.remove_favorite_car(car_id)
            return "Removed car"


        #Otherwise, create new fav for user.
        else: 
            user_id= session["user_id"]
            favorite =crud.add_favorite_car(car_id, user_id)
            return "Added car"

@app.route("/check_favorites/<car_id>")
def check_favorite_car(car_id):
    """Check if user saved car to profile"""
    response = crud.check_if_car_in_favorites(car_id)
    if response == True:
        return json.dumps(True)
    else:
        return json.dumps(False)






if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)