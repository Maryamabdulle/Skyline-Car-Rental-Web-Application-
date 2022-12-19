
<img width="1007" alt="Screen Shot 2022-12-19 at 12 28 42 AM" src="https://user-images.githubusercontent.com/114389244/208370848-8e50062b-d74a-48e1-8b14-5ade7428c8ce.png">


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
 

### 📹 [Project Demo Video](https://www.youtube.com/watch?v=hs9bWSQ_A2w)

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
 
Carousel <br>

![Hnet-image (1)](https://user-images.githubusercontent.com/114389244/208368302-fca5d53d-6bee-4094-8ca8-48e712966ef8.mp4)

Hompe page <br>

![hnet-image(2](https://user-images.githubusercontent.com/114389244/208369734-fe0b2b13-2f4e-4aa3-8c6b-73eb4d8f4a4b.mp4)<br>
 
All Cars page page <br>

![hnet-image(3](https://user-images.githubusercontent.com/114389244/208370639-def74380-739d-420a-a651-92bf14b9d0ea.mp4) <br>

Utilizing the Sort by/filter Method <br>

![hnet-image(4](https://user-images.githubusercontent.com/114389244/208371612-295505aa-9c32-491d-ba12-c9a6d73d81e8.mp4) <br>

Dropdown to select a Category <br> 

![hnet-image(5](https://user-images.githubusercontent.com/114389244/208372023-bebbe267-07cf-4a85-b944-da9bdf8eacc6.mp4) <br>

Register or Login <br>

![hnet-image(6](https://user-images.githubusercontent.com/114389244/208373308-c98dd59f-f357-4978-83ab-480ab7dc14ed.mp4) <br>

Favorite to save to favorites page <br>
![hnet-image(7](https://user-images.githubusercontent.com/114389244/208468239-b5394d48-0e6c-4c6f-a4e3-a098ada350bf.mp4) <br>

Selecting locations and Google Maps with geocoding & selecting a car to book<br>
![hnet-image(8](https://user-images.githubusercontent.com/114389244/208470533-d771d922-6456-4c0b-8e5b-46ebb839bb51.mp4) <br>

Validating if dates has been already book or incorrect & payment options<br>
![hnet-image(9](https://user-images.githubusercontent.com/114389244/208472412-27e40d06-b90e-45c8-9343-e6a00634f904.mp4) <br>

Profile Page <br>
![hnet-image(10](https://user-images.githubusercontent.com/114389244/208472773-f5628ab4-f248-474c-8fe4-65d63cb83202.mp4) <br>


Canceling reservations both successfully & restrictions <br>
![hnet-image(11](https://user-images.githubusercontent.com/114389244/208473132-83515826-8b63-437b-9c30-9b744bd1618e.mp4) <br>

Return the car with a rate and a review  <br>

![hnet-image(12]( https://user-images.githubusercontent.com/114389244/208473645-26ce55cf-54c8-49bc-906b-a3f0929a6b96.mp4) <br>

Displaying rate and review with jinja2 templates <br>
![hnet-image(13](https://user-images.githubusercontent.com/114389244/208474153-edd0d169-3a8a-4a92-8bfe-1a4f7abd3f3d.mp4) <br>

Contact Page <br>
![hnet-image(14](https://user-images.githubusercontent.com/114389244/208474639-72e0c86b-4032-4990-b971-732b1d09ae31.mp4) <br>


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