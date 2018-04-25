import base_dir
import psycopg2
import json 
import os, csv

from src.settings import DATA_PATH

## create database
conn = psycopg2.connect("host='localhost' dbname='database' user='postgres' password='passmeword'")
c = conn.cursor()

print("Creating table...")
## Create table
c.execute('''CREATE TABLE IF NOT EXISTS persons(
                id serial primary key,
                name text not null,
                email text not null,
                phone text not null,
                bio text,
                dob text,
                gender integer not null check (gender in (0,1)),
                address text,
                longitude text,
                lattitude text,
                social_media text,
                img text
                )''')


with open('data/2.csv', 'r') as f:
    reader = csv.reader(f)
    
    count = 1
    for row in reader:
        print("Inserting data....{}".format(count))
        #name,email,digit,sentence,date,gender,city,longitude,latitude,alpha
        name = row[0]
        email = row[1]
        phone = row[2]
        bio = row[3]
        dob = row[4]
        gender = 1 if row[5]=='Male' else 0
        address = row[6]
        longitude = row[7]
        latitude = row[8]
        social_media = 'http://facebook.com/'+row[9]
        
        # name = _['name']
        # email = _['email']
        # phone = _['phone']
        # bio = _['bio']
        # dob = _['dob']
        # gender = _['gender']
        # address = _['address']
        # longitude = _['longitude']
        # latitude = _['latitude']
        # social_media = 'http://facebook.com/'+_['social_media']

        # img ='''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB1klEQVR42n2TzytEURTHv3e8N1joRhZG" + 
        #     "zJsoCjsLhcw0jClKWbHwY2GnLGUlIfIP2IjyY2djZTHSMJNQSilFNkz24z0/Ms2MrnvfvMu8mcfZvPvu" + 
        #     "Pfdzz/mecwgKLNYKb0cFEgXbRvwV2s2HuWazCbzKA5LvNecDXayBjv9NL7tEpSNgbYzQ5kZmAlSXgsGG" + 
        #     "XmS+MjhKxDHgC+quyaPKQtoPYMQPOh5U9H6tBxF+Icy/aolqAqLP5wjWd5r/Ip3YXVILrF4ZRYAxDhCO" + 
        #     "J/yCwiMI+/xgjOEzmzIhAio04GeGayIXjQ0wGoAuQ5cmIjh8jNo0GF78QwNhpyvV1O9tdxSSR6PLl51F" + 
        #     "nIK3uQ4JJQME4sCxCIRxQbMwPNSjqaobsfskm9l4Ky6jvCzWEnDKU1ayQPe5BbN64vYJ2vwO7CIeLIi3" + 
        #     "ciYAoby0M4oNYBrXgdgAbC/MhGCRhyhCZwrcEz1Ib3KKO7f+2I4iFvoVmIxHigGiZHhPIb0bL1bQApFS" + 
        #     "9U/AC0ulSXrrhMotka/lQy0Ic08FDeIiAmDvA2HX01W05TopS2j2/H4T6FBVbj4YgV5+AecyLk+Ctvms" + 
        #     "QWK8WZZ+Hdf7QGu7fobMuZHyq1DoJLvUqQrfM966EU/qYGwAAAAASUVORK5CYII='''
    

        img = 'user.png'

        c.execute('''INSERT INTO persons(name, email, phone, bio, dob, gender, address, longitude, lattitude, img, social_media)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                    (name, email, phone, bio, dob, gender, address, longitude, latitude, img, social_media)
                )


        count+=1


conn.commit()
print("\nCreated table and initialized with 1000000 data set successful !\n")
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()