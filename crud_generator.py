import psycopg2
from dbConnection import dbConnection

class crud_generator():

    metadataSize = 0
    
    def __init__(self, con, c):
        self.con = dbConnection.openConnection(c)

    def getTable(self):
        cur = self.con.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
        tableList = cur.fetchall()
        print("\nVIEW DATA FOR TABLE:")
        j = 1
        for i in tableList:
            print(j, "-", i[0])
            j = j + 1
        tableNumber = int(input("Table Number: "))
        tableName = tableList[tableNumber - 1][0]

        cur.execute(f"SELECT * FROM public.{tableName}")
        columnNames = [desc[0] for desc in cur.description]
        print(f"Table <{tableName}> found.")
        print("Found column names: ")
        j = 1
        for i in columnNames:
            print(j, "-", i)
            j = j + 1
        orderNum = int(input("Order by: "))
        order = columnNames[orderNum - 1]

        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM public.{tableName} ORDER BY {order}")
        data = cur.fetchall()
        size = len(data)
        s = f"\nDATA FROM TABLE <{tableName}>:"
        print(s.upper())
        self.printTable(size, self.metadataSize, data)

    def printTable(self, rows, columns, data):
        for x in range(rows):
            print("[", end = ' ')
            for y in range(columns):
                print(f"{data[x][y]};", end = ' ')
            print(']')