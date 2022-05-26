import psycopg2
from dbConnection import dbConnection
from model import model

class dbMetadata(model):
    
    def getDBVersion(c):
        con = dbConnection.openConnection(c)
        cur = con.cursor()
        cur.execute('SELECT version()')
        version = cur.fetchone()[0]
        
        con.close()
        return version

    def getTableList(c):
        con = dbConnection.openConnection(c)
        cur = con.cursor()

        cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
        tableList = cur.fetchall()
        
        con.close()

        return tableList

    def getTableMetadata(c, tableName):
        con = dbConnection.openConnection(c)
        cur = con.cursor()

        cur.execute(f"SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.columns WHERE table_name = '{tableName}'")
        tableMetadata = cur.fetchall()
        
        con.close()
        return tableMetadata

    def getTable(c, tableName):
        con = dbConnection.openConnection(c)
        cur = con.cursor()
        
        mtdt = dbMetadata.getTableMetadata(c, tableName)
        cur.execute(f"SELECT * FROM public.{tableName} ORDER BY {mtdt[0][0]}")
        table = cur.fetchall()

        con.close()
        return table

    def getTableColumnCount(c, tableName):
        con = dbConnection.openConnection(c)
        cur = con.cursor()
        
        cur.execute(f"SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.columns WHERE table_name = '{tableName}'")
        cc = len(cur.fetchall())

        con.close()
        return cc

    def getTableLineCount(c, tableName):
        con = dbConnection.openConnection(c)
        cur = con.cursor()
        
        cur.execute(f"SELECT * FROM {tableName}")
        cc = len(cur.fetchall())   

        con.close()
        return cc

    def printMetadata(self, data):
        s = f"\nMETADATA FROM TABLE <{self.tableName}>:"
        print(s.upper())
        metadataSize = len(data)
        self.printTable(metadataSize, 3, data)

    def printTable(self, lines, columns, data):
        return super().printTable(lines, columns, data)