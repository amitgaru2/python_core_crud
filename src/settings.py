import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

MEDIA_PATH = os.path.join(BASE_DIR, 'media')
DATA_PATH = os.path.join(BASE_DIR, 'data')
SQLITE = {'database':'database.db'}

POSTGRES = {
                'host':'localhost',
                'database':'database',
                'user':'postgres',
                'password':'passmeword'
           }

ARGS_DICT = {
                '-id': 'id',
                '-n': 'name', 
                '-p': 'phone', 
                '-e': 'email',
                '-g': 'gender', 
                '-a': 'address', 
                '-do': 'dob',
                '-lo': 'longitude',
                '-la': 'latitude',
                '-sm': 'social_media',
                '-b': 'bio',
                '-im': 'img',
                '--id': 'id',
                '--name': 'name',
                '--phone': 'phone',
                '--email': 'email',
                '--gender': 'gender',
                '--address': 'address',
                '--dob': 'dob',
                '--longitude': 'longitude',
                '--latitude': 'latitude',
                '--social': 'social_media',
                '--bio': 'bio',
                '--img': 'img'
            }
