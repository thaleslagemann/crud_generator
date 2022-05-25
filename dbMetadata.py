import psycopg2
from dbConnection import dbConnection

class dbMetadata():

    def __init__(self, c):
        self.c = c

    def getMetadata(self):
        con = dbConnection.openConnection(self.c)
        cur = con.cursor()
        cur.execute('SELECT version()')
        version = cur.fetchone()[0]
        print(version)

        cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
        tableList = cur.fetchall()
        print("\nVIEW METADATA FOR TABLE:")
        j = 1
        for i in tableList:
            print(j, "-", i[0])
            j = j + 1
        tableNumber = int(input("Table Number: "))
        tableName = tableList[tableNumber - 1][0]

        cur.execute(f"SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.columns WHERE table_name = '{tableName}'")
        s = f"\nMETADATA FROM TABLE <{tableName}>:"
        print(s.upper())
        data = cur.fetchall()
        self.metadataSize = len(data)
        self.printTable(self.metadataSize, 3, data)