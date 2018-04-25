'''
    searching of person using id
'''
import base_dir
from modules.connection import DBConnection
from modules.person import Person
from modules.radix import RadixSorting
from modules.binary_searching import binary_search
import time

## connect to database

conn = DBConnection()
conn.connect()

## fetch all database rows
_person = Person(conn)

print("\n\tPlease Wait! Fetching all data from database...")
result = _person.read(random=True).fetchall()

# extract only the id and add the tuple to dictionary
base_list = []
base_dict = {}
for row in result:
    base_list.append(row[0])
    base_dict[row[0]] = row


## get search key from user
pid = int(input("\n\tEnter searching id? "))

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
