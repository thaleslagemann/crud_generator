# Trabalho 1 - Laboratório de Orientação a Objetos
# UFSM - 2022/1
# Gerador de Cruds
# Thales Augusto Lagemann - 201821179
# Isadora Moro - 

from DbConnection import DbConnection
from CrudExample import CrudExample
from DbConnectionData import DbConnectionData
from DbMetadata import DbMetadata
from ClassWriter import ClassWriter

conData = DbConnectionData()

host = input("Host: ")
conData.setHost(host)
        
dbname = input("DB Name: ")
conData.setDbname(dbname)
        
user = input("User: ")
conData.setUser(user)

pwd = input("Password: ")
conData.setPwd(pwd)

tableList = DbMetadata.getTableList(conData)

print("\nGET METADATA FOR TABLE:")
j = 1
for i in tableList:
    print(j, "-", i[0])
    j = j + 1
tableNumber = int(input("Table Number: "))
tableName = tableList[tableNumber - 1][0]

table = DbMetadata.getTable(conData, tableName)
tableMdt = DbMetadata.getTableMetadata(conData, tableName)

columns = DbMetadata.getTableColumnCount(conData, tableName)
lines = DbMetadata.getTableLineCount(conData, tableName)

cw = ClassWriter(conData, tableName)

cw.writeDAOFile()
cw.writeEntityFile()
cw.writeExampleFile()