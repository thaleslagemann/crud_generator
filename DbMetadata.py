import psycopg2
from DbConnection import DbConnection
from Model import Model

class DbMetadata(Model):
    
    def getDBVersion(c):
        con = DbConnection.openConnection(c)
        cur = con.cursor()
        cur.execute('SELECT version()')
        version = cur.fetchone()[0]
        
        con.close()
        return version

    def getTableList(c):
        con = DbConnection.openConnection(c)
        cur = con.cursor()

        cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
        tableList = cur.fetchall()
        
        con.close()

        return tableList

    def getTableMetadata(c, tableName):
        con = DbConnection.openConnection(c)
        cur = con.cursor()

        cur.execute(f"SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.columns WHERE table_name = '{tableName}'")
        tableMetadata = cur.fetchall()
        
        print(tableMetadata)
        
        con.close()
        return tableMetadata

    def getTable(c, tableName):
        con = DbConnection.openConnection(c)
        cur = con.cursor()

        mtdt = DbMetadata.getTableMetadata(c, tableName)
        cur.execute(f"SELECT * FROM public.{tableName} ORDER BY {mtdt[0][0]}")
        table = cur.fetchall()

        con.close()
        return table

    def getTableColumnCount(c, tableName):
        con = DbConnection.openConnection(c)
        cur = con.cursor()
        
        cur.execute(f"SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.columns WHERE table_name = '{tableName}'")
        cc = len(cur.fetchall())

        con.close()
        return cc

    def getTableLineCount(c, tableName):
        con = DbConnection.openConnection(c)
        cur = con.cursor()
        
        cur.execute(f"SELECT * FROM {tableName}")
        cc = len(cur.fetchall())   

        con.close()
        return cc

    def printMetadata(data, tableName):
        s = f"\nMETADATA FROM TABLE <{tableName}>:"
        print(s.upper())
        metadataSize = len(data)
        DbMetadata.printTable(metadataSize, 3, data)

    def printTable(lines: int, columns: int, data):
        print("Lines | Columns:", lines, columns)
        print("Data: ", data)
        for x in range(lines):
            print("[", end = ' ')
            for y in range(columns):
                print(f"{data[x][y]};", end = ' ')
            print(']')
