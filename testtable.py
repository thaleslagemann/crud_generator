import psycopg2
from model import model
from dbConnection import dbConnection
from dbMetadata import dbMetadata

class testtableDAO(model):

    def __init__(self, c, tableName):
        self.c = c
        self.tableName = tableName

    def viewTable(self):
        lineCount = dbMetadata.getTableLineCount(self.c, self.tableName)
        columnCount = dbMetadata.getTableColumnCount(self.c, self.tableName)
        print("Column count:", columnCount)
        print("Line count:", lineCount)
        s = f"DATA FROM TABLE <{self.tableName}>:"
        print(s.upper())
        table = dbMetadata.getTable(self.c, self.tableName)
        self.printTable(lineCount, columnCount, table)

    def insertItem(self, con, data):
        con = dbConnection.openConnection(self.c)
        cur = con.cursor()

        try:
            cur.execute(f"INSERT INTO {self.tableName} VALUES ({data[0]}, {data[1]}], {data[2]}])")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()
        con.close()

    def updateItem(self, con, data):
        cur = con.cursor()

        try:
            cur.execute(f"UPDATE {data[0]} WHERE table = '{self.tableName}' VALUES ({data[0]}, {data[1]}], {data[2]}])")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()