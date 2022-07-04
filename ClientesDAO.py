import psycopg2
from Model import Model
from DbConnection import DbConnection
from DbMetadata import DbMetadata

class ClientesDAO(Model):

    def __init__(self, c):
        self.c = c
        self.tableName = 'clientes'

    def viewTable(self):
        lineCount = DbMetadata.getTableLineCount(self.c, self.tableName)
        columnCount = DbMetadata.getTableColumnCount(self.c, self.tableName)
        print("Column count:", columnCount)
        print("Line count:", lineCount)
        s = f"DATA FROM TABLE <{self.tableName}>:"
        print(s.upper())
        table = DbMetadata.getTable(self.c, self.tableName)
        self.printTable(lineCount, columnCount, table)

    def insertItem(self, con, data):
        con = DbConnection.openConnection(self.c)
        cur = con.cursor()

        try:
            cur.execute(f"INSERT INTO {self.tableName} VALUES ({data[0]}, {data[1]}])")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()
        con.close()

    def updateItem(self, con, data):
        con = DbConnection.openConnection(self.c)
        cur = con.cursor()

        try:
            cur.execute(f"UPDATE {data[0]} WHERE table = '{self.tableName}' VALUES ({data[0]}, {data[1]}])")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()

    def deleteItem(self, con, data):
        con = DbConnection.openConnection(self.c)
        cur = con.cursor()
        metadata = DbMetadata.getTableMetadata(con, self.tablename)

        try:
            cur.execute(f"DELETE FROM {self.tablename} WHERE codigo = '{data[0]}'")
            row = cur.fetchone()
            print(row)
        
        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)

        con.commit()

    def researchItem(self, con, data):
        con = DbConnection.openConnection(self.c)
        cur = con.cursor()
        metadata = DbMetadata.getTableMetadata(con, self.tablename)

        try:
            cur.execute(f"SELECT * FROM {self.tablename} WHERE codigo = '{data[0]}'")
            row = cur.fetchone()
            print(row)
        
        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)

        con.commit()