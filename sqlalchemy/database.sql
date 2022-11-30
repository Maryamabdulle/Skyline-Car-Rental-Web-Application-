DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
  user_id VARCHAR(255),
  fname VARCHAR(255), 
  email VARCHAR(255),
  pass VARCHAR(255),
);


INSERT INTO Users (user_id,fname,email, pass) VALUES ('1','Tom','tom@gmail.com', 'hello12');
INSERT INTO Users (user_id,fname,email, pass) VALUES ('2','Alex','alex@gmail.com', 'study23');
INSERT INTO Users (user_id,fname,email, pass) VALUES ('3','Jack', 'jack@gmail.com', 'sleep38');
INSERT INTO Users (user_id,fname,email, pass) VALUES ('4','Jazmine', 'jazmine@gmail.com', 'great93');
INSERT INTO Users (user_id,fname,email, pass) VALUES ('5','Maryam', 'maryam@gmail.com', 'what20');
select * from Users


CREATE TABLE Cars (
car_id SERIAL PRIMARY KEY,
car_id VARCHAR(255),
vehicle_type VARCHAR(255)
vehicle_name VARCHAR(255), 
seats INTEGER,
Doors INTEGER,
Automatic_or_manual BOOLEAN,
large_bag VARCHAR(255),
small_bag VARCHAR(255),
AC BOOLEAN,
mpg INTEGER,
per_day_charges INTEGER
category VARCHAR(255), 
images VARCHAR(255),
);

-- Small to Full Size
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('1', 'Economy' , 'Ford Fiesta', '5 seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '27/35 27-35 mpg',$145, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('2', 'Compact' , 'Kia Soul', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '25-29 mpg',$151, True, 'Small to Full Size','/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('3', 'Intermediate' , 'Toyota Corolla', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '29-35 mpg',$156, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('4', 'Standard' , 'Volkswagen Jetta', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '24-35 mpg',$173, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('5', 'Full Size' , 'Toyota Camry ', '5 Seats', '4 Doors', 'Automatic Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '22-30 mpg',$175, True, 'Small to Full Size', ,'/home/Document/a.jpg' )

-- NEW: Small to Full Size-----------------------
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('6', 'Full Size' , 'Chevy Malibu', '5 Seats', '4 Doors', 'Automatic Transmission' , '2 Large Bag', '1 Small Bag', 'A/C', '22-30 mpg',$125, True, 'Small to Full Size', ,'/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('7', 'Standard Elite' , 'BMW 228i gran coupe', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '24-35 mpg',$173, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('8', 'Intermediate Electric Car' , 'Nissan LEAF', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '27/35 27-35 mpg',$112, True, 'Small to Full Size', ,'/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('9', 'Full-Size Hybrid Car' , 'Ford Fusion Hybrid', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '22-30 mpg',$122, True, 'Small to Full Size', ,'/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('10', 'Standard' , 'Chevrolet Impala', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '24-35 mpg',$157, True, 'Small to Full Size', ,'/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('11', 'Standard Hybrid' , 'Toyota Prius', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '24-35 mpg',$129, True, 'Small to Full Size', ,'/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('12', 'Compact'  , 'Nissan Versa ', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '25-29 mpg',$111, True, 'Small to Full Size', ,'/home/Document/a.jpg' )




-- for  SUV

INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('1', 'Intermediate SUV', 'Mazda CX-5', '5 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '27/35 27-35 mpg',$189, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('2', 'Standard SUV', 'Ford Edge', '5 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '15-22 mpg',$204, True, 'SUVs', '/home/Document/a.jpg' )

-- NEW :  SUV--------------------------
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('3', 'Standard SUV', 'Toyota 4Runner', '5 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '15-22 mpg',$102, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('4', 'Standard Elite SUV', 'Chevrolet Traverse', '7 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '15/20-15-20 mpg',$100, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('5', 'Premium SUV', 'Chevrolet Suburban', '7/8 Seats', '4 Doors', 'Automati Transmission' , '3 Large Bag', '4 Small Bag', 'A/C', '16/21-16-21 mpg',$278, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('6', 'Compact SUV', 'Nissan Kicks', '5 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '16/21-16-21 mpg',$179, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('7', 'Full-Size SUV', 'Chevrolet Tahoe', '7/8 Seats', '4 Doors', 'Automati Transmission' , '4 Large Bag', '3 Small Bag', 'A/C', '16/21-16-21 mpg',$312, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('8', 'Luxury SUV', 'Infiniti QX80', '8 Seats', '4 Doors', 'Automati Transmission' , '4 Large Bag', '2 Small Bag', 'A/C', '16/21-16-21 mpg',$260, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('9', 'Premium Crossover SUV', 'Volkswagen Atlas', '8 Seats', '4 Doors', 'Automati Transmission' , '4 Large Bag', '3 Small Bag', 'A/C', '15-22 mpg',$299, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('10', 'Full-Size SUV', 'Ford Expedition', '7/8 Seats', '4 Doors', 'Automati Transmission' , '4 Large Bag', '3 Small Bag', 'A/C', '16/21-16-21 mpg',$299, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('11', 'Standard Elite SUV', 'GMC Acadia', '7 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '3 Small Bag', 'A/C', '15/20-15-20 mpg',$128, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('12', 'Standard Elite SUV', 'Dodge Durango ', '8 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '3 Small Bag', 'A/C', '15-22 mpg',$292, True, 'SUVs', '/home/Document/a.jpg' )





-- Luxury & Convertibles
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('1', ' Premium', 'Volkswagen Passat', '5 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '18-29 mpg',$198, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('2', ' Convertible', 'Ford Mustang Convertible' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '19-24 mpg',$223, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('3', ' Luxury', 'Chrysler 300' , '5 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '18-21 mpg',$215, True, 'Luxury & Convertibles', ,'/home/Document/a.jpg' )

-- NEW: Luxury & Convertibles----------------------------
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('4', 'Standard Elite Coupe', 'Dodge Challenger R/T' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '15-19 mpg',$187, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('5', 'Intermediate Elite Electric', 'Tesla Model 3' , '5 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', 'Electric',$120, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('6', 'Standard Sport', 'Ford Mustang Coupe' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '16/24-16-24 mpg',$100, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('7', 'Convertible' , 'BMW 7-Series' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '19-24 mpg',$157, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('8',  'Luxury' , 'Jaguar F-Type SVR' , '2 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '15-19 mpg',$107, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('9', ' Luxury', 'Mercedes Benz SL400' , '2 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '18-21 mpg',$172, True, 'Luxury & Convertibles', ,'/home/Document/a.jpg' )
INSERT INTO cars (car_id, vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('10', ' Convertible', 'chevrolet camaro convertible' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '19-24 mpg',$223, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('11', 'Luxury Elite Electric Car' 'Porsche Taycan' , '4 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', 'Electric',$315, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id,  vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('12', 'Luxury' 'Lexus LC 500' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '15-19 mpg',$178, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )







-- All vehicles including suvs
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('1', 'Economy' , 'Ford Fiesta', '5 seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '27/35 27-35 mpg',$145, True, 'Small to Full Size','/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('2', 'Compact' , 'Kia Soul', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '25-29 mpg',$151, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('3', 'Intermediate' , 'Toyota Corolla', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '29-35 mpg',$156, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('4', 'Standard' , 'Volkswagen Jetta', '5 Seats', '4 Doors', 'Automatic Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '24-35 mpg',$173, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('5', 'Full Size' , 'Toyota Camry ', '5 Seats', '4 Doors', 'Automatic Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '22-30 mpg',$175, True, 'Small to Full Size', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('6', 'Intermediate SUV', 'Mazda CX-5', '5 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '27/35 27-35 mpg',$189, True, 'SUVs', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('7', 'Standard SUV', 'Ford Edge', '5 Seats', '4 Doors', 'Automati Transmission' , '1 Large Bag', '2 Small Bag', 'A/C', '15-22 mpg',$204, True, 'SUVs','/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('8', ' Premium' 'Volkswagen Passat', '5 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '18-29 mpg',$198, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('9', ' Convertible' 'Ford Mustang Convertible' , '4 Seats', '2 Doors', 'Automati Transmission' , '1 Large Bag', '1 Small Bag', 'A/C', '19-24 mpg',$223, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )
INSERT INTO cars (car_id, , vehicle_type, vehicle_name, seats, Doors, Automatic_or_manual, large_bag, small_bag, AC, per_day_charges, category, images) VALUES ('10', ' Luxury' 'Chrysler 300' , '5 Seats', '4 Doors', 'Automati Transmission' , '2 Large Bag', '2 Small Bag', 'A/C', '18-21 mpg',$215, True, 'Luxury & Convertibles', '/home/Document/a.jpg' )







CREATE TABLE Trips (
trip_id VARCHAR(255),
user_id VARCHAR(255),
car_id VARCHAR (255),
pick_up_location VARCHAR(255), 
drop_of_location VARCHAR(255),
pick_up_date Timestamp, 
drop_of_date Timestamp,
pick_up_time Timestamp
drop_of_time Timestamp,
);

INSERT INTO Trips (trip_id, user_id, car_id, pick_up_location, drop_of_location, pick_up_date, drop_of_date, pick_up_time, drop_of_time) VALUES ('', '', '');


CREATE TABLE Rate (
rate_id VARCHAR(255),
user_id VARCHAR(255),
car_id VARCHAR (255),
feedback Text,
);










