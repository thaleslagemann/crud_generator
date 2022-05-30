from dbConnection import dbConnection
from crud_exemple import crud_exemple
from dbConnectionData import dbConnectionData
from dbMetadata import dbMetadata
from classWriter import classWriter
import getpass

c = dbConnectionData()

host = "localhost"
dbname = "testDB"
user = "testUsr"
pwd = "tstusr"
#pwd = getpass.getpass("Password: ")

#host = input("Host: ")
c.setHost(host)
        
#dbname = input("DB Name: ")
c.setDbname(dbname)
        
#user = input("User: ")
c.setUser(user)

#pwd = input("Password: ")
c.setPwd(pwd)

tableList = dbMetadata.getTableList(c)
#print("\nGET METADATA FOR TABLE:")
#j = 1
#for i in tableList:
#    print(j, "-", i[0])
#    j = j + 1
#tableNumber = int(input("Table Number: "))
#tableName = tableList[tableNumber - 1][0]
#cur = c.cursor()
#cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
#tableList = cur.fetchall()
#print("SELECT TABLE:")
#j = 1
#for i in tableList:
#    print(j, "-", i[0])
#   j = j + 1
#tableNumber = int(input("Table Number: "))
#tableName = tableList[tableNumber - 1][0]

#cur.execute(f"SELECT * FROM public.{tableName}")
#columnNames = [desc[0] for desc in cur.description]

tableName = "testtable"
db = crud_exemple(c, tableName)

cw = classWriter(c, tableName)

cw.createFile()

cw.writeInFile()

#db.viewTable(tableName)

#print(f"Table <{tableName}> found.")

#a = client()
#a._set_sql_insertion("INSERT test IN test")
#a.print_value()