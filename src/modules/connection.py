import base_dir
import sqlite3, psycopg2
from src import settings

class DBConnection():
    '''
        Abstraction of database connection and transaction.
    '''

    def __init__(self, select_db=None):
        # select_db = 1 for sqlite select_db = 2 for postgres
        self.conn = None
        self.cursor = None

        if select_db == None:
            # select database
            select_db = int(input('''
                1. SQLite
                2. Postgres

                Select database (1/2) ? '''))

            if select_db not in [1,2]: exit()

        # set db_type and db
        if select_db==1:
            self.db_type = 'SQLITE' 
            self.db = settings.SQLITE['database']

        elif select_db==2:
            self.db_type = 'POSTGRES'
            self.db = "host="+settings.POSTGRES['host']+" dbname="+settings.POSTGRES['database']+" user="+settings.POSTGRES['user']+" password="+settings.POSTGRES['password']
        
        else:
            print("No database found for this index")
            exit()
            
        print("\n\tUSING {} DATABASE.".format(self.db_type))
        
    def connect(self):
        try:
            if self.db_type == 'SQLITE':
                self.conn = sqlite3.connect(self.db)
            elif self.db_type == 'POSTGRES':
                self.conn = psycopg2.connect(self.db)
                
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)


    def execute(self, query, values=None):
        try:
            if self.db_type == 'SQLITE':
                if values == None:      # for read all data operations that do not require any value
                    return self.cursor.execute(query)
                else:
                    return self.cursor.execute(query, values)

            elif self.db_type == 'POSTGRES':
                if values == None: 
                    self.cursor.execute(query)
                else:
                    if query.startswith('INSERT'):
                        query += ' RETURNING id'        # for returning id of last inserted data for postgres
                    self.cursor.execute(query, values)
                return self.cursor

        except Exception as e:
            print(e)
            return False   


    def commit(self):
        try:
            self.conn.commit()
            return True

        except Exception as e:
            print(e)
            return False


    def close(self):
        self.conn.close()
    

    @property
    def placeholder(self):
        if self.db_type == 'SQLITE':
            return '?'
        elif self.db_type == 'POSTGRES':
            return '%s'

    @property
    def last_row_id(self):
        if self.db_type == 'SQLITE':
            return self.cursor.lastrowid
        elif self.db_type == 'POSTGRES':
            return self.cursor.fetchone()[0]
