import base_dir
import sqlite3
import json 
import os
            
from src.settings import DATA_PATH

## create database
conn = sqlite3.connect('database.db')
c = conn.cursor()


print("Creating table...")
## Create table
c.execute('''CREATE TABLE IF NOT EXISTS persons(
                id integer primary key,
                name text not null,
                email text not null unique,
                phone text not null unique,
                bio text,
                dob text,
                gender integer not null check (gender in (0,1)),
                address text,
                longitude text,
                lattitude text,
                social_media text,
                img text
                )''')

## populate table with 200 data set
data_path = os.path.join(DATA_PATH, 'data_1000.json')
data = json.load(open(data_path, 'r'))

count=1
for _ in data:
    #print(_)
    print("Inserting data....{}".format(count))
    name = _['name']
    email = _['email']
    phone = _['phone']
    bio = _['bio']
    dob = _['dob']
    gender = _['gender']
    address = _['address']
    longitude = _['longitude']
    latitude = _['latitude']
    social_media = 'http://facebook.com/'+_['social_media']

    img = 'user.png'


    c.execute('''INSERT INTO persons(name, email, phone, bio, dob, gender, address, longitude, lattitude, img, social_media)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                (name, email, phone, bio, dob, gender, address, longitude, latitude, img, social_media)
            )


    count+=1


conn.commit()
print("\nCreated table and initialized with 200 data set successful !\n")
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()