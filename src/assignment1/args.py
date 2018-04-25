'''

    Command line arguments for CRUD, Sorting, Searching

    python args.py
    1. -db db_select --> select database

    2. -c | --create --> create person
        3. -n | --name name --> name of person
        3. -e | --email email --> email of person
        3. -g | --gender (0/1) --> gender 0-Female 1-Male
        3. -a | --address address --> address of person 
        3. -do | --dob mm/dd/yyyy --> dob of person
        3. -lo | --longitude value --> longitude of person
        3. -la | --latitude value --> latitude of person
        3. -sm | --social value --> social media link of person in format http://something
        3. -b | --bio bio --> bio of the person

    2. -ra | --readall --> read all rows
    2. -rf | --readfirst n --> read first n rows
    2. -rl | --readlast n --> read last n rows
    2. -r | --read id --> read id
    2. -u | --update pid -> update person
        3. -n | --name name --> name of person
        3. -e | --email email --> email of person
        3. -g | --gender (0/1) --> gender 0-Female 1-Male
        3. -a | --address address --> address of person 
        3. -do | --dob mm/dd/yyyy --> dob of person
        3. -lo | --longitude value --> longitude of person
        3. -la | --latitude value --> latitude of person
        3. -sm | --social value --> social media link of person in format http://something
        3. -b | --bio bio --> bio of the person

    2. -d | --delete id --> delete person with id

    2. -so | -- sorting flag --> flag=(-id|-n|-e|-p....) sort by flag
    
    2. -se | -- searching id --> search person with id

'''
import base_dir
import sys, time
from src.modules.connection import DBConnection
from src.modules.person import Person
from src.modules.radix import RadixSorting
from src.modules.binary_searching import binary_search
from src.modules.validator import Validation
from src.settings import ARGS_DICT


## select database using args
if sys.argv[1]=='-db' or sys.argv[1]=='--database':
    select_db = int(sys.argv[2])
    
    # create database connection
    conn = DBConnection(select_db=select_db)
    conn.connect()

    # persons table relation
    _person = Person(conn)
else:
    print("\n\tWarning! Enter args for database select.")
    exit()


## validate user inputs for create and update - crud
def validate_user_args(user_args, **kwargs):
    if 'update' in kwargs:      # these arguments could be empty in update to set old values
        user_args['name'] = validator.validate_name(user_args['name']) if 'name' in user_args else ''
        user_args['phone'] = validator.validate_phone(user_args['phone']) if 'phone'  in user_args else ''
        user_args['email'] = validator.validate_email(user_args['email']) if 'email' in user_args else ''
        user_args['gender'] = validator.validate_gender(user_args['gender']) if 'gender' in user_args else ''
    else:
        user_args['name'] = validator.validate_name(user_args['name'])
        user_args['phone'] = validator.validate_phone(user_args['phone'])
        user_args['email'] = validator.validate_email(user_args['email'])
        user_args['gender'] = validator.validate_gender(user_args['gender'])
    user_args['address'] = user_args['address'] if 'address' in user_args else ''
    user_args['dob'] = validator.validate_dob( user_args['dob'] if 'dob' in user_args else '' )
    user_args['longitude'] = validator.validate_longitude(user_args['longitude'] if 'longitude' in user_args else '' )
    user_args['latitude'] = validator.validate_latitude(user_args['latitude'] if 'latitude' in user_args else '' )
    user_args['bio'] = user_args['bio'] if 'bio' in user_args else '' 
    user_args['social_media'] = validator.validate_social(user_args['social_media'] if 'social_media' in user_args else '' )
    user_args['img'] = user_args['img'] if 'img' in user_args else '' 

    return user_args

# index 3 args

# create
if sys.argv[3]=="-c" or sys.argv[3]=="--create":

    user_args = {}

    create_args = sys.argv[4:]
    for indx in range(0,len(create_args),2):
        if create_args[indx] in ARGS_DICT:
            if (indx+1)<(len(create_args)):
                arg_name = ARGS_DICT[create_args[indx]]
                user_args[arg_name] = create_args[indx+1]

    if 'name' not in user_args or 'email' not in user_args or 'phone' not in user_args or 'gender' not in user_args:
        print("Warning! Name, Email, Phone, Gender are required arguments.")
    else:
        try:
            # for validating user inputs
            validator = Validation()
            user_args = validate_user_args(user_args)
            _create = _person.create(
                name=user_args['name'], 
                email=user_args['email'], 
                address=user_args['address'], 
                dob=user_args['dob'], 
                longitude=user_args['longitude'],
                phone=user_args['phone'],
                latitude=user_args['latitude'],
                bio=user_args['bio'],
                gender=user_args['gender'],
                social_media=user_args['social_media'],
                img=user_args['img']
            )
            
        except Exception as e:
            print("\nAdd Person Failed due to {} ! Enter to continue....".format(e))

# read all rows
elif sys.argv[3]=="-ra" or sys.argv[3]=="--readall":
    _person.read(display=True)

# read first n rows
elif sys.argv[3]=="-rf" or sys.argv[3]=="--readfirst":
    read_first = int(sys.argv[4])
    _person.read(read_first=read_first, display=True)

# read last n rows
elif sys.argv[3]=="-rl" or sys.argv[3]=="--readlast":
    read_last = int(sys.argv[4])
    _person.read(read_last=read_last, display=True)

# read id
elif sys.argv[3]=="-r" or sys.argv[3]=="--read":
    pid = int(sys.argv[4])
    _person.read(id=pid, display=True)

# update
elif sys.argv[3]=="-u" or sys.argv[3]=="--update":
    user_args = {}

    pid = int(sys.argv[4])
    create_args = sys.argv[5:]
    for indx in range(0,len(create_args),2):
        if create_args[indx] in ARGS_DICT:
            if (indx+1)<(len(create_args)):
                arg_name = ARGS_DICT[create_args[indx]]
                user_args[arg_name] = create_args[indx+1]

    if len(user_args.keys()) == 0:
        print("Warning! At least 1 argument required for update.")
    else:
        try:
            # for validating user inputs
            validator = Validation()
            user_args = validate_user_args(user_args, update=True)
            _person.update(pid,
                    name=user_args['name'], 
                    email=user_args['email'], 
                    address=user_args['address'], 
                    dob=user_args['dob'], 
                    longitude=user_args['longitude'],
                    phone=user_args['phone'],
                    latitude=user_args['latitude'],
                    bio=user_args['bio'],
                    gender=user_args['gender'],
                    social_media=user_args['social_media'],
                    img=user_args['img']
                )

        except Exception as e:
            print("\nUpdate Person Failed due to {} ! Enter to continue....".format(e))

# delete
elif sys.argv[3]=="-d" or sys.argv[3]=="--delete":
    pid = int(sys.argv[4])

    result = _person.read(id=pid)
    if len(result.fetchall()) == 0:
        input("Sorry! user not found. Enter to continue... ")
    else:
        try: 
            _person.delete(pid)
            
        except Exception as e:
            print("\nDelete Person Failed due to {}".format(e))


# sorting
elif sys.argv[3] == '-so' or sys.argv[3] == '--sorting':
    sort_by = _person.columns.index(ARGS_DICT[sys.argv[4]])

    print("\n\tPlease Wait! Fetching all data from database...")
    result = _person.read(random=True).fetchall()

    base_list = []
    base_dict = {}
    print("\n\tPlease Wait! Sorting data....")
    start_time = time.clock()
    if sort_by == 0:     # if sort by id then only store id in base_list for keeping track of swappings
        
        for row in result:
            base_list.append(row[0])
            base_dict[row[0]] = row

        radix = RadixSorting(base_list, sort_by)
        radix.sort_id()
        sorted_list = radix.result

        # re-arrange the rows based on the sorted list
        for i in range(len(sorted_list)):
            result[i] = base_dict[sorted_list[i]]


    else:
        for row in result:     # if sort by other than id then id with field value to keep track of swappings
            base_list.append((row[0], row[sort_by],))       # (id, name) or (id, address) or ...
            base_dict[row[0]] = row
            

        radix = RadixSorting(base_list, sort_by)
        #if sort_by in [1,2,4,7,10]: 
        
        if sort_by == 1:
            radix.sort_name()
        elif sort_by in [2,4,7,10]:
            radix.sort_email_bio_address_media()
        elif sort_by == 3:
            radix.sort_phone()
        elif sort_by == 5:
            radix.sort_dob()
        elif sort_by == 6:
            radix.sort_gender()
        elif sort_by in [8,9]:
            radix.sort_long_lat()
        
        
        sorted_list = radix.result
        # re-arrange the rows based on the sorted list
        for i in range(len(sorted_list)):
            result[i] = base_dict[sorted_list[i][0]]
        
        end_time = time.clock()-start_time

    _person.display_query_result(result)
    # print("\n\tDisplaying first and last row of sorted result...")
    # _person.display_query_result([result[0]])
    # _person.display_query_result([result[-1]])

    # for row in result:
    #     print(row[sort_by])

    print("\nCPU clock time spent:", end_time)


# searching
elif sys.argv[3] == '-se' or sys.argv[3] == '--searching':
    ## get search key from user
    pid = int(sys.argv[4])

    print("\n\tPlease Wait! Fetching all data from database...")
    result = _person.read(random=True).fetchall()

    # extract only the id and add the tuple to dictionary
    base_list = []
    base_dict = {}
    for row in result:
        base_list.append(row[0])
        base_dict[row[0]] = row


    print("\n\tPlease Wait! Searching data....")
    start_time = time.clock()

    ## first sorting using radix sort
    radix = RadixSorting(base_list, 0)          # 0 - sort by id
    radix.sort_id()
    result = radix.result

    search_result = binary_search(result, pid)      # returns pid if found else returns False
    end_time = time.clock()-start_time

    if search_result:
        _person.display_query_result([base_dict[search_result]])    # fetch the row of the id using base dict created earlier
    else:
        print("\n\tNo result found!")

    print("\nCPU clock time spent:", end_time)
