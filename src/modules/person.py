import base_dir
import os
from src.settings import MEDIA_PATH

class Person():
    '''
       Person table module
    '''
    table = 'persons'
    columns = ['id','name','email','phone','bio','dob','gender','address','longitude','latitude','social_media','img']
    columntypes =  {
                        'id':'integer', 
                        'name':'text',
                        'email':'text',
                        'phone':'text',
                        'bio':'text',
                        'dob':'text',
                        'gender':'integer',
                        'address':'text',
                        'longitude':'text',
                        'latitude':'text',
                        'social_media':'text',
                        'img':'text'
                    }


    def __init__(self, conn):
        self.conn = conn
        self.ph = conn.placeholder


    def create(self, **_):
        name = _['name']
        email = _['email']
        phone = _['phone']
        bio = _['bio']
        dob = _['dob']
        gender = _['gender']
        address = _['address']
        longitude = _['longitude']
        latitude = _['latitude']
        social_media = _['social_media']
        img = _['img']
        # if _['img'] != '':
        #     img_path = os.path.join(MEDIA_PATH, _['img'])
        #     img = base64.b64encode(open(img_path, "rb").read()).decode('utf-8')
        # else:
        #     img = ''

        ## for returning id of last row inserted
       
        if self.conn.execute('''INSERT INTO persons(name, email, phone, bio, dob, gender, address, longitude, lattitude, social_media, img)
                VALUES ({0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0})'''.format(self.ph,), 
                (name, email, phone, bio, dob, gender, address, longitude, latitude, social_media, img)
        ):
            self.conn.commit()
            print("\nPerson created successfully at id: {}".format(self.conn.last_row_id))


    def read(self, **_):
        if 'id' in _:       # if id sent as argument then detail view of that id
            result = self.conn.execute('''
                                       SELECT * FROM persons where id={0}
                                       '''.format(self.ph,), (_['id'],)
                                      )     

        else:       # if not sent then show all data i.e list view all
            if 'random' in _:
                result = self.conn.execute('SELECT * FROM persons ORDER BY RANDOM()')
            elif 'read_first' in _:
                result = self.conn.execute('SELECT * FROM persons LIMIT {0}'.format(self.ph),(_['read_first'],))
            elif 'read_last' in _:
                result = self.conn.execute('SELECT * FROM persons ORDER BY id DESC LIMIT {0}'.format(self.ph),(_['read_last'],))
            else:
                result = self.conn.execute('SELECT * FROM persons')
        if 'display' in _:      # display in terminal
            self.display_query_result(result)
        else:
            return result
       
    @staticmethod
    def display_query_result(result):
        count = 0
        for row in result:
            pid = row[0]
            name = row[1]
            email = row[2]
            phone = row[3]
            bio = row[4]
            dob = row[5]
            gender = 'Male' if row[6] else 'Female'
            address = row[7]
            longitude = row[8]
            latitude = row[9]
            social_media = row[10]
            img = row[11]

            print('''
                    Id: {},
                    Name: {}, 
                    Email: {}, 
                    Phone: {}, 
                    Bio: {}, 
                    DOB: {}, 
                    Gender: {}, 
                    Address: {}, 
                    Longitude: {}, 
                    Latitude: {}, 
                    Social Media: {},
                    Image: {}
                '''.format(pid, name, email, phone, bio, dob, gender, address, longitude, latitude, social_media, img)
                )

            count+=1
        # if no result found display no found message
        if not count:
            print("\n\tSorry! No result found.")


    @classmethod
    def get_dict_of_query_result(cls, _person):
        dict_person = {}

        count = 0
        for value in _person:
            dict_person[cls.columns[count]] = _person[count]
            count+=1
        
        return dict_person
        

    def update(self, pid, **_):
        _person = Person.get_dict_of_query_result(self.read(id=pid).fetchone())

        # update values in the _person dict
        for column in _.keys():
            if _[column] != '':
                _person[column] = _[column]

        # if _['img'] != '':
        #     img_path = os.path.join(MEDIA_PATH, _['img'])
        #     _person['img'] = base64.b64encode(open(img_path, "rb").read()).decode('utf-8')
        
        if self.conn.execute(
                    '''UPDATE persons SET 
                    name = {0}, 
                    email = {0}, 
                    phone = {0}, 
                    bio = {0}, 
                    dob = {0}, 
                    gender = {0}, 
                    address = {0}, 
                    longitude = {0}, 
                    lattitude = {0}, 
                    social_media = {0}, 
                    img = {0}
                    WHERE id = {0}
                  '''.format(self.ph,),
                  (_person['name'],_person['email'],_person['phone'],_person['bio'],_person['dob'],_person['gender'],_person['address'],_person['longitude'],_person['latitude'],_person['social_media'],_person['img'],pid)
        ):
            self.conn.commit()
            print("\nPerson updated successfully of id: {}".format(pid))
            

    def delete(self, pid):
        if self.conn.execute( ''' 
                            DELETE FROM persons WHERE id = {0}
                            '''.format(self.ph,), (pid,)
        ):
            self.conn.commit()
            print("\nPerson deleted successfully of id: {}".format(pid))
