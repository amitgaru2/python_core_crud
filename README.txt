TASK 1 / ASSIGNMENT 1
By - Amit Garu


Python version - 3.5.2


Schema for sqlite

CREATE TABLE IF NOT EXISTS persons(
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
                                )



Schema for postgres

CREATE TABLE IF NOT EXISTS persons(
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
                                 )


Files and there purposes:
1. src/modules/binary_searching.py - contains binary search algorithm function
2. src/modules/connection.py - database connection class
3. src/modules/person.py - contains person table as class with its crud methods
4. src/modules/radix.py - contains radix search algorithm class
5. src/modules/validator.py - contains validation rules
6. src/assignment1/args.py - for command line argument for crud, sorting, searching operations
7. src/assignment1/crud.py - for crud operation in interactive terminal
8. src/assignment1/searching.py - for searching operation in interactive terminal
9. src/assignment1/settings.py - contains constants used by other part of code like connection information, media path
10. src/assignment1/sorting.py - for sorting operation in interactive terminal



* Assumption - Data already initialized in sqlite and postgres database
* Assumption - Database columns order in:
    0. id
    1. name
    2. email
    3. phone
    4. bio
    5. dob
    6. gender
    7. address
    8. longitude
    9. latitude
    10. social_media
    11. img
* Change connection information in settings.py
* More info on command line arguments in settings.py ARG_DICT and args.py __doc__ 

* img field value can be provided by the image name inside MEDIA_PATH folder in settings.py

* before entering terminal commands change directory to /src/assignment1 from project root
    -> cd src/assignment1


1. CRUD operations

    1.1 using interactive terminal
        python3 crud.py

    1.2 using args
        1.2.1 create
            *Name, email, phone and gender are required value

            1.2.1.1 sqlite
                python3 args.py -db 1 -c -n "test testing" -e emaaa@emmaaam.com -p 1233323993 -g 0 -a sallaghari -lo -177.22 -la 22.22 -sm http://facebook.com/xillar -im user.png -b "this is test bio" -do 01/11/1992
                
                or,
                python3 args.py -db 1 -c -n "test testing" -e emaaa@emmaaam.com -p 1233323993 -g 0

            1.2.1.2 postgres
                python3 args.py -db 2 -c -n "test testing" -e emaaa@emmaaam.com -p 1233323993 -g 0 -a sallaghari -lo -177.22 -la 22.22 -sm http://facebook.com/xillar -im user.png -b "this is test bio" -do 01/11/1992
        
            -> creates new user with given arguments

        1.2.2 read all rows

            1.2.2.1 sqlite
                python3 args.py -db 1 -ra
            
            1.2.2.2 postgres
                python3 args.py -db 2 -ra
            
            -> reads all rows
            
        1.2.3 read first n rows

            1.2.3.1 sqlite
                python3 args.py -db 1 -rf 10
            
            1.2.3.2 postgres
                python3 args.py -db 2 -rf 10
            
            -> reads first 10 rows
        
        1.2.4 read last n rows

            1.2.4.1 sqlite
                python3 args.py -db 1 -rl 10

            1.2.4.2 postgres
                python3 args.py -db 2 -rl 10

            -> reads last 10 rows
        
        1.2.5 read person by id

            1.2.5.1 sqlite
                python3 args.py -db 1 -r 1
            
            1.2.5.2 postgres
                python3 args.py -db 2 -r 1
            
            -> reads person id 1

        1.2.6 update
            *At least one argument for database column required thats need to be updated.
            *Rest not passed arguments for database column value remains same as old value.

            1.2.6.1 sqlite
                python3 args.py -db 1 -u 1 -n "new name test testing" -e newemaaa@emmaaam.com -p 1233323993 -g 0 -a sallaghari -lo -177.22 -la 22.22 -sm http://facebook.com/xillar -im user.png -b "this is test bio" -do 01/11/1992
                
                or,
                python3 args.py -db 1 -u 1 -n "test fda testing"

            1.2.6.2 postgres
                python3 args.py -db 2 -u 1 -n "new name test testing" -e newemaaa@emmaaam.com -p 1233323993 -g 0 -a sallaghari -lo -177.22 -la 22.22 -sm http://facebook.com/xillar -im user.png -b "this is test bio" -do 01/11/1992
        
            -> updates person id 1
        
        1.2.7 delete

            1.2.7.1 sqlite
                python3 args.py -db 1 -d 1
            
            1.2.7.2 postgres
                python3 args.py -db 2 -d 1
    
            -> deletes person id 1



2. Sorting operations
    *Sorts by all database column selected by user.

    2.1 using interactive terminal
        python3 sorting.py
    

    2.2 using args
        Sort by flag:
            -id | --id = sort by id
            -n | --name = sort by name
            -e | --email = sort by email
            -p | --phone =  sort by phone
            
            .... more on settings.py ARG_DICT dictionary variable

        2.2.1 sqlite
            python3 args.py -db 1 -so flag

            eg. for sorting by name...
            python3 args.py -db 1 -so -n
            

        2.2.2 postgres
            python3 args.py -db 2 -so flag
        
        -> sorts by flag given



3. Searching operations
    *Searching by person id only.

    3.1 using interactive terminal
        python3 searching.py
    

    3.2 using args
        
        3.2.1 sqlite
            python3 args.py -db 1 -se 1

        3.2.2 postgres
            python3 args.py -db 2 -se 1
        

        -> searches person id 1



Task 2 | Assignment 2

1. Creating API 

    Run server:
        python3 api.py port

        -> port is optional

    1.1 GET Requests
        
        Request url: http://localhost:8000/person/id 

        eg. http://localhost:8000/person/1 
            gives the json object of person id 1 stored in the database
        