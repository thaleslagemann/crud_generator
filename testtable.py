import psycopg2
from Model import Model
from DbConnection import DbConnection
from DbMetadata import DbMetadata

class testtableDAO(Model):

    def __init__(self, c, tableName):
        self.c = c
        self.tableName = tableName

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