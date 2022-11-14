"""Flask app for testing the project."""
from unittest import TestCase

from server import app
from model import connect_to_db, db, test_data



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

    result =self.client.get("/")
    self.assertIn(b"Welcome to", result.data)


def test_car_title(self):
    """Test all_vehcile page. Make sure name of the car is showing."""

    result =self.client.get("/cars")
    self.assertIn(b"Ford Fiesta", result.data)
    self.assertIn(b"Mazda CX-5",result.data)

def test_all_cars(self):
    """Test all cars route."""
    response=self.client.get('/search', content_type="html/text")
    self.assertEqual(response.status_code, 200)


def test_user_resgistration(self):
    """Test user resgistration."""
    response = self.client.post("/register",
                         data={"email": "user1@test.com", 
                         "password": "testing",
                         "fname":"usertest"},
                         follow_redirects= True)
    self.assertIn(b"Account created!", response.data)

def test_resgistration_existing_email(self):
    """Test user attempting to create an account with an existing email."""

    response = self.client.post("/register",
                            data={"email": "user@test.com", 
                            "password": "existingemail"},
                            follow_redirects= True)

    self.assertIn(b"Cannot create an account with that email." , response. data)

def test_login(self):
    """Test login page."""

    result= self.client.post("/login", 
                            data={"email": "user@test.com", 
                                    "password": "testing"},
                            follow_redirects= True)
    self.assertIn(b"Reservations", result.data)



def tearDown(self):
    """Drop data at tend of every test."""

    db.session.remove()
    db.drop_all()
    db.engine.dispose()


if __name__ == "__main__":
    import unittest
    unittest.main()