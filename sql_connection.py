import psycopg2

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


def insert(cursor, project,action,started,ended):
    temp_at_end_time = 25
    SQL = "INSERT INTO testilog(project,action,started,ended,temperature) VALUES(%s,%s,%s,%s);"
    data = (project,action,started,ended,temp_at_end_time)
    cursor.execute(SQL,data)


####################

def connect():
    con = None
    
    con = psycopg2.connect(**config())
    cursor = con.cursor()  
    
    select(cursor)
    insert(cursor,'projekti','kahvittelin','1999-01-08 04:05','2021-7-15 15:00')
      
    if con is not None:
        con.close()


################


connect()
    
