'''
    0. sort by id
    1. sort by name
    2. sort by email
    3. sort by phone
    4. sort by bio
    5. sort by dob
    6. sort by gender
    7. sort by address
    8. sort by longitude
    9. sort by latitude
    10. sort by media link 
'''

import base_dir
from modules.connection import DBConnection
from modules.person import Person
from modules.radix import RadixSorting
from settings import COLUMN_ORDERS
import time


conn = DBConnection()
conn.connect()

_person = Person(conn)
print("\n\tPlease Wait! Fetching all data from database...")
result = _person.read(random=True).fetchall()

sort_by = int(input(__doc__+"\n Sort by: "))
if sort_by not in [0,1,2,3,4,5,6,7,8,9,10]: exit()


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
# _person.display_query_result([result[0]])
# _person.display_query_result([result[-1]])

# for row in result:
#     print(row[sort_by])

print("\nCPU clock time spent:", end_time)
