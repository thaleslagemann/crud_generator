from dbConnection import dbConnection
from crud_generator import crud_generator
from dbData import dbData
from dbMetadata import dbMetadata
import getpass

c = dbData()

host = "localhost"
dbname = "testDB"
user = "testUsr"
#pwd = "tstusr"
pwd = getpass.getpass("Password: ", stream = "*")

#host = input("Host: ")
c.setHost(host)
        
#dbname = input("DB Name: ")
c.setDbname(dbname)
        
#user = input("User: ")
c.setUser(user)

#pwd = input("Password: ")
c.setPwd(pwd)

dbmdt = dbMetadata(c)
dbmdt.getMetadata()
db = crud_generator(c)
db.getTable()
#a = client()
#a._set_sql_insertion("INSERT test IN test")
#a.print_value()