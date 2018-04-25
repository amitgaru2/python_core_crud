import base_dir
from modules.validator import Validation
from modules.person import Person
from modules.connection import DBConnection

# create database connection
conn = DBConnection()
conn.connect()

# persons table relation
_person = Person(conn)

# for validating user inputs
validator = Validation()


while True:
    option = int(input('''
            1. Insert Person
            2. Read All Persons
            3. Read Person
            4. Update Person
            5. Delete Person

            Enter your choice? '''))

    if option == 1:
        try:
            name = validator.validate_name(input("\nEnter name* ? "))
            phone = validator.validate_phone(input("Enter phone no.* ? "))
            email = validator.validate_email(input("Enter email* ? "))
            gender = validator.validate_gender(input("Gender (0-F, 1-M)* ? "))
            address = input("Enter address ? ")
            dob = validator.validate_dob(input("DOB (mm/dd/yyyy) ? "))
            longitude = validator.validate_longitude(input("Longitude ? "))
            latitude = validator.validate_latitude(input("Latitude ? "))
            bio = input("Bio ? ")
            social_media = validator.validate_social(input("Media link ? "))
            img = input("image location ? ")

            
            _create = _person.create(
                name=name, 
                email=email, 
                address=address, 
                dob=dob, 
                longitude=longitude,
                phone=phone,
                latitude=latitude,
                bio=bio,
                gender=gender,
                social_media=social_media,
                img = img
                )
            
           
        except Exception as e:
            print("\nAdd Person Failed due to {} ! Enter to continue....".format(e))
            input()


    elif option == 2:
        _person.read(display=True)


    elif option == 3:
        pid = input("\nEnter id of person? ")
        _person.read(id=pid, display=True)


    elif option == 4:
        pid = input("\nEnter id of person? ")
        result = _person.read(id=pid)
        if len(result.fetchall()) == 0:
            input("Sorry! user not found. Enter to continue... ")
        else:
            result = Person.get_dict_of_query_result(_person.read(id=pid).fetchone())
            try:  
                name = validator.validate_name(input("Enter new name ({})* ? ".format(result['name'])))
                email = validator.validate_email(input("Enter new email ({})* ? ".format(result['email'])))
                phone = validator.validate_phone(input("Enter new phone no. ({})* ? ".format(result['phone'])))
                gender = validator.validate_gender(input("Gender new(0-F, 1-M) ({})* ? ".format(result['gender'])))
                bio = input("Bio new ({}) ? ".format(result['bio']))
                dob = validator.validate_dob(input("DOB new(mm/dd/yyyy) ({}) ? ".format(result['dob'])))
                address = input("Enter new address ({}) ? ".format(result['address']))
                longitude = validator.validate_longitude(input("Longitude new ({}) ? ".format(result['longitude'])))
                latitude = validator.validate_latitude(input("Latitude new ({}) ? ".format(result['latitude'])))
                social_media = validator.validate_social(input("Media link new ({}) ? ".format(result['social_media'])))
                img = input("image location new? ")

                _person.update(pid,
                    name=name, 
                    email=email, 
                    address=address, 
                    dob=dob, 
                    longitude=longitude,
                    phone=phone,
                    latitude=latitude,
                    bio=bio,
                    gender=gender,
                    social_media=social_media,
                    img=img
                )

            except Exception as e:
                print("\nUpdate Person Failed due to {} ! Enter to continue....".format(e))
                input()


    elif option == 5:
        pid = input("\nEnter id of person? ")
        result = _person.read(id=pid)
        if len(result.fetchall()) == 0:
            input("Sorry! user not found. Enter to continue... ")
        else:
            try: 
                _person.delete(pid)
                
            except Exception as e:
                print("\nDelete Person Failed due to {}".format(e))


    else:
        conn.close()
        break


    input("\nEnter to continue....")
