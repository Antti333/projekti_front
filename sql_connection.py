from main import start
import psycopg2
from main import user_interface

from configparser import ConfigParser, Error

from temperature import get_weather

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


######################################## work time ########################


def select(cursor):
    SQL = 'SELECT * FROM testilog;'
    cursor.execute(SQL)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()


def select_one_id(cursor,id):
    SQL = 'SELECT * FROM testilog WHERE id = %s;'
    data = id
    cursor.execute(SQL,data)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()


def get_start_time(cursor,date):
    SQL = 'SELECT * FROM testilog WHERE started = %s;'
    cursor.execute(SQL,date)
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()



def get_end_time(cursor,date):
    pass


def insert(cursor, project,action,started,ended):
    #temp_at_end_time = 25
    SQL = "INSERT INTO testilog(project,action,started,ended,temperature) VALUES(%s,%s,%s,%s,25);"
    data = (project,action,started,ended)
    cursor.execute(SQL,data)


####################

def connect():
    con = None
    
    con = psycopg2.connect(**config())
    cursor = con.cursor()  
    
    #get_start_time(cursor,'2021-07-21 08:05')

    while True:

        list_of_values = user_interface()
        insert(cursor,list_of_values[0],list_of_values[1],list_of_values[2],list_of_values[3])
        con.commit()

        if list_of_values[4] == "no":
           break
    
    #datan latausta

    #insert(cursor,'projekti2','vessassa','2021-07-21 08:05','2021-7-21 15:00')
    #insert(cursor,'projekti2','lounas','2021-07-20 08:05','2021-7-20 15:00')
    #insert(cursor,'projekti3','lapsi sairaana','2021-07-19 08:05','2021-7-21 16:00')
    #insert(cursor,'projekti3','sairaana','2021-07-20 08:05','2021-7-20 15:00')

    #select_one_id(cursor,'4')
    
    #select(cursor)

    if con is not None:
        con.close()


################


connect()
    
