
![Alt text]


## Table of Contents 📖 

* [Overview](#overview)
* [Project Demo Video](#project-demo-video)
* [About Me](#about-me)
* [Tech Stack](#tech-stack)
* [Python Libraries Used](#python-libraries-used)
* [Roadmap](#roadmap)
* [Features](#features)
* [Installation](#installation)
* [Future Iterations](#future-iterations)


 
## <a name="overview"></a>Overview 🚗

Skyline car Rental is a full-stack web application that allows users to browse a variety of cars and their categories to learn about it. Users can utilize the filter method to sort by price, mileage, and the number of seats and select which car categories they want the filters to apply to from the four car categories such as ( SUVs, Small to full size, Luxury & Convertibles, or all All cars). Users are able to create an account or login to book a car online with the options of paying now or later. It lets users know when the selected car is not available. Users can select pick-up and drop-off locations and can view the full details of the locations. Users can also leave a review and rating for the car after it is returned and all users can see reviews of the cars. Users can choose to return without review. Users can favorite cars which will then show up on the user’s favorites page. Users can visit their profile page and also see all current, past, and future reservations they have made. Users can always cancel a reservation on the profile page, but I implemented a 24-hour cancellation restriction which prohibits the cancellation within 24 hours of their reservation time. I created a contact option for users to reach out to me.
 

### 📹 [Project Demo Video] (https://www.youtube.com/watch?v=hs9bWSQ_A2w) 

## <a name= "about-me"></a>About Me 🧕🏽

Maryam Abdulle is a software Engineer and enjoys problem solving.


## <a name= "tech-stack"></a>Tech Stack 📚
 
**Backend**: Python(Flask), PostgreSQL, SQLAlchemy <br/>
**Frontend**: AJAX, Bootstrap, CSS, HTML, Jinja2, Javascript(AJAX, JSON), jQuery <br/>
**APIs**: Google Maps API <br/>
 
## <a name="python-libraries-used"></a>Python libraries Used 💻
 
- Flask Bootsrap - style <br/>
- Datetime - Date and Time <br/>
- Hashlib - Password security <br/>
 
 
## <a name="roadmap"></a>Roadmap 📈
 
#### MVP :
- users can create an account
- Users can log in
- users without an account can view cars and details of the car and images
- Users can use the Dropdown of the Navbar to view car categories
- Users can make a reservation and book car online after login
- Users can pick the pick-up & drop-off locations, dates, and times.
- Users can favorite cars that show up on the user’s favorites page after login
 
 
#### 2.0 :
- Users cannot book a car if another User has already booked for the same date.
- Google Maps API & google geocoding are used to render a map with location markers for vehicle pick-up and drop-off locations which users can see the details of the locations.
- Users can use the filter/sort method for different car categories based on price (low to high), number of seats(high to low), and mileage(high to low)
- Users have a profile page to which they can update booking and have access to ( current, past, & future reservations and details of the user information)
- Users can choose to rate and leave a review of the car after returning
- Users have access to either pay now or pay later options when booking a car
- Users can Contact me directly by sending a message from the contact me page
- Users can visit the About us page to get more information about Skyline Car Rental

 
## <a name= "features"></a>Features 🌼
 
Car Carsouel page: <br>
(https://user-images.githubusercontent.com/114389244/208366234-a9a521cf-1b81-4b3e-bb15-2efa64b3122d.mp4)









Hompe page: <br>
![hnet-image(1)](note to myself post the video here of the homepage)<br>
 
 
 


All Cars page page: <br>




Utalizing the Sort by/filter Method <br>


Dropdown to select Categories <br>
Register or Login <br>

Favorite to save to favorites page <br>


Selecting locations and Google Maps with geocoding <br>

Selecting a car to book <br>

Validating if dates has been already book or incorrect <br>

Confirmation details page with payment options <br>

Profile Page <br>

Canceling reservation successfully <br>

Unable to cancel reservation within 24 hours before the pick up time of the car <br>

Return the car without a rate and a review <br>

Return the car with a rate and a review  <br>

Displaying rate and review with jinja2 templates <br>

Contact Page <br>




















## <a name= "installation"></a>Installation 🖊️
 
 ### Requirments 
 
 * Install requirements.txt
 * Python 3
 * PostgreSQL

To run this web application locally on your device, follow the below steps.

Steps 1- Clone this repository:
```
$ git clone https://github.com/Maryamabdulle/Skyline-Car-Rental-Web-Application-.git
```

Step 2- Create and activate a virtual environment:
```
 $ pip3 install virtualenv
 $ virtualenv env
 $ source env/bin/activate
 ```

Step 3- Install dependencies:
 ```
 $ pip3 install -r requirements.txt
 ```
 

Step 4- Install Flask Mail:

 ```
 $ pip install Flask-Mail
 ````

Step 5- create a secrets.sh file to save secret keys:
 ```
 export "API" = "youcanputhereyourGooglemapsapi" 
 ```

Step 6- Create and use app passwords to access Google Account:

 - Create sender and receiver emails to add to secret.sh.sh file 
 - For the sender email, turn on 2-step Verification on your account to create and use app passwords
 - Upon successful creation of the app password, a 16-character code in the yellow bar on your device should be generated 
 - Following the Sender email you created, add this code to your secrets.sh file 

Step 7- Add both receiver and sender emails and 16-character code into secrets.sh:
```
export= "EMAIL"= "emailaddress";export "PASS"= "16-charactercode"
export= "RECIEVER"="emailaddress"
```

Step 8- Activate the secrets.sh file in terminal:
 ```
 (env) $ source secrets.sh
 ```

Step 9- Create the database:
 ```
 (env) $ createdb cars
 (env) $ psql cars < cars.sql>
```

Step 10- Seed the database:
```
(env) $ python3 model.py
(env) $ python3 seed_database.py
```

Step 11- Run the server:
```
(env) $ python3 server.py
```

Step 12- To view locally, Type on local browser:

localhost:5000



## <a name="future-iterations"></a>Future Iterations 💥
- Create user authentication so users can retrieve forgotten passwords and create new passwords
- Adding an admin page so I can add more cars and more locations easily on the admin side
- Add functionality that lets users book directly with other rental car companies through Skyline Car Rental