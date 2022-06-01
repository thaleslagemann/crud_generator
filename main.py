from DbConnection import DbConnection
from CrudExample import CrudExample
from DbConnectionData import DbConnectionData
from DbMetadata import DbMetadata
from ClassWriter import ClassWriter

connection = DbConnectionData()

host = "localhost"
dbname = "testDB"
user = "testUsr"
pwd = "tstusr"
#pwd = getpass.getpass("Password: ")

#host = input("Host: ")
connection.setHost(host)
        
#dbname = input("DB Name: ")
connection.setDbname(dbname)
        
#user = input("User: ")
connection.setUser(user)

#pwd = input("Password: ")
connection.setPwd(pwd)

tableList = DbMetadata.getTableList(connection)

#print("\nGET METADATA FOR TABLE:")
#j = 1
#for i in tableList:
#    print(j, "-", i[0])
#    j = j + 1
#tableNumber = int(input("Table Number: "))
#tableName = tableList[tableNumber - 1][0]
#cur = connection.cursor()
#cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
#tableList = cur.fetchall()
#print("SELECT TABLE:")
#j = 1
#for i in tableList:
#    print(j, "-", i[0])
#    j = j + 1
#tableNumber = int(input("Table Number: "))
#tableName = tableList[tableNumber - 1][0]

tableName = 'testtable'

#DbMetadata.printMetadata(tableList, 'testTable')
table = DbMetadata.getTable(connection, tableName)
tableMdt = DbMetadata.getTableMetadata(connection, tableName)

columns = DbMetadata.getTableColumnCount(connection, tableName)
lines = DbMetadata.getTableLineCount(connection, tableName)

DbMetadata.printMetadata(tableMdt, tableName)

DbMetadata.printTable(lines, columns, table)

db = CrudExample(connection, tableName)

cw = ClassWriter(connection, tableName)

cw.createFile()

cw.writeInFile()