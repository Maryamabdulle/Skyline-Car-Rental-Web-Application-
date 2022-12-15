"""Flask app for testing the project."""
from unittest import TestCase

from server import app
from model import connect_to_db, db, test_data, Favorite, Rate, Car, User
import requests
import hashlib


class FlaskTestBasic(TestCase):
    """Flask tests."""
    def setUp(self):


        #Show Flask errors that happen during tests
        app.config['TESTING']= True
        connect_to_db(app, "postgresql:///testdb")
        app.config['SECRET_KEY']= 'carsaregreat'
        #Get the Flask test client
        self.client= app.test_client()
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id']=1
        db.create_all()
        test_data()

    def test_homepage(self):
        """Test homepage route."""

        r = self.client.get ("/")
        self.assertIn(b"Rent a Car Online Today", r.data)


    def test_car_title(self):
        """Test all_vehcile page. Make sure name of the car is showing."""

        r = requests.get('http://localhost:5000/cars')
        self.assertIn(b"Ford Fiesta", r.content)
        self.assertIn(b"Mazda CX-5",r.content )

    def test_car_sort(self):
        """Test car sort route."""
        r = requests.get('http://localhost:5000/vehicle-sort?sort=price')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'Chevrolet Traverse', r.content)

    def test_car_cat(self):
        r = requests.get('http://localhost:5000/cars?cat=suv')
        self.assertEqual(r.status_code, 200)
        self.assertIn(b'Chevrolet Traverse', r.content)

    def test_all_cars(self):
        """Test all cars route."""
        response=self.client.get('/cars', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        r = requests.get('http://localhost:5000/some-page-that-dont-exists')
        self.assertEqual(r.status_code, 404)
        pass

    def test_insert_user(self):
        password = 'testing'
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(
            fname='testfname',
            lname='testlname',
            email='test@test.com',
            password=hash_password,
            address='test addrss',
            contact='031233934344'
        )
        db.session.add(user)
        db.session.commit()

        user_out = User.query.filter_by(fname='testfname', lname='testlname', email='test@test.com').all()
        self.assertEqual(len(user_out), 1)
        pass

    def test_duplicate_email_user(self):
        data=''
        try:
            # can be run  two times
            # To get duplicate email
            for _ in range(2):
                password = 'testing'
                hash_password = hashlib.sha256(password.encode()).hexdigest()
                user1 = User(
                    fname='testfname',
                    lname='testlname',
                    email='test@test.com',
                    password=hash_password,
                    address='test addrss',
                    contact='031233934344'
                )
                db.session.add(user1)
                db.session.commit()
                data='ok'
        except:
            data = 'Email already exists'
        pass

        self.assertEqual('Email already exists', data)


    def test_insert_car(self):
        car = Car(
            vehicle_type='test type',
            vehicle_name='testcar name',
            seats=5,
            doors=4,
            Transmission='automatic',
            large_bag='test',
            small_bag='test',
            ac='test',
            mpg='test',
            per_day_charges='test',
            category='tset',
            car_img='test'
        )
        db.session.add(car)
        db.session.commit()

        car_out = Car.query.filter_by(vehicle_name='testcar name', vehicle_type='test type').all()
        self.assertEqual(len(car_out), 1)


    def test_add_favourite(self):
        fav_in = Favorite(car_id=1, user_id=1)
        db.session.add(fav_in)
        db.session.commit()

        self.assertEqual(fav_in.favorites_id, 1)
        pass


    def test_fav_car(self):
        fav_in = Favorite(car_id=1, user_id=1)
        db.session.add(fav_in)
        db.session.commit()

        fav_out = Favorite.query.filter_by(user_id=1, car_id=1).all()
        self.assertEqual(len(fav_out), 1)
        pass

    def test_car_not_favourite(self):
        car_id = 99
        user_id = 99
        fav = Favorite.query.filter_by(car_id=car_id, user_id=user_id).all()
        self.assertEqual(len(fav), 0)

    def test_rated_car(self):
        rate_in = Rate(car_id=1, user_id=1, score=5, rate='Nice experience', trip_id=1)
        db.session.add(rate_in)
        db.session.commit()

        rate_out = Rate.query.filter_by(user_id=1, car_id=1).all()
        self.assertEqual(len(rate_out), 1)
        pass

    def test_none_rated_car(self):
        car_id = 99
        user_id = 99

        rate = Rate.query.filter_by(car_id=car_id, user_id=user_id).all()
        self.assertEqual(len(rate), 0)
        pass


    def tearDown(self):
        """Drop data at tend of every test."""

        db.session.remove()




def test_user_resgistration(self):
    """Test user resgistration."""
    password = 'testing'
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    response = self.client.post("/register",
                         data={"email": "user1@test.com", 
                         "password": hash_password,
                         "fname":"usertest", "lname": 'test', 'address': 'test', 'contact': '1232321312'},
                         follow_redirects= True)
    self.assertIn(b"Account created!", response.data)

def test_resgistration_existing_email(self):
    """Test user attempting to create an account with an existing email."""

    password = 'testing'
    hash_password = hashlib.sha256(password.encode()).hexdigest()

    response = self.client.post("/register",
                            data={"email": "user1@test.com", 
                         "password": hash_password,
                         "fname":"usertest", "lname": 'test', 'address': 'test', 'contact': '1232321312'},
                            follow_redirects= True)

    self.assertIn(b"Cannot create an account with that email." , response. data)

def test_login(self):
    """Test login page."""
    password = 'testing'
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    result= self.client.post("/login", 
                            data={"email": "user@test.com", 
                                    "password": hash_password},
                            follow_redirects= True)
    self.assertIn(b"Reservations", result.data)




if __name__ == "__main__":
    import unittest
    unittest.main()