import psycopg2
from dbConnection import dbConnection
from dbMetadata import dbMetadata
from model import model

class crud_generator(model):
    
    def __init__(self, c):
        self.c = c
        self.metadataSize = 0

    # Método substituto da viewTable dos exemplos, pega uma table do banco e printa ela na tela
    def getTable(self):
        con = dbConnection.openConnection(self.c)
        cur = con.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_schema, table_name;")
        tableList = cur.fetchall()
        print("VIEW DATA FOR TABLE:")
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

        cur = con.cursor()
        cur.execute(f"SELECT * FROM public.{tableName} ORDER BY {order}")
        data = cur.fetchall()
        size = len(data)
        mtdtSize = dbMetadata.getTableSize(self.c, tableName)
        s = f"DATA FROM TABLE <{tableName}>:"
        print(s.upper())
        self.printTable(size, mtdtSize, data)
        con.close()

    # Método que cria uma tabela nova na base de dados
    def newTable(self, con):
        tableName = input("New Table Name: ")
        cur = con.cursor()
        try:
            cur.execute(f"CREATE TABLE {tableName} (id integer, num integer, data varchar);")
            print(f"Table <{tableName}> creation successful.")

        except (Exception, psycopg2.errors.DuplicateTable) as error:
            print(error)
        
        con.commit()
        con.close()

    # Método que insere um item novo na tabela informada
    # OBS: Não funciona para qualquer tabela, por enquanto só serve
    # para inserir elementos em uma tabela com atributo chave id e
    # dois outros atributos de nome quaisquer, um int e um varchar
    def insertItem(self, con):
        tableName = input("Table name: ")
        cur = con.cursor()

        try:
            id = int(input("ID: "))
            attribute1 = int(input("Attr1: "))
            attribute2 = input("Attr2: ")

            print(type(id), type(attribute1), type(attribute2))
            cur.execute(f"INSERT INTO {tableName} VALUES ({id}, {attribute1}, '{attribute2}')")
            cur.execute(f"SELECT * FROM {tableName} WHERE id = {id}")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()
        con.close()

    # Método utilizado para deletar um item escolhido da tabela informada
    def deleteItem(self, con):
        tableName = input("Table name: ")
        cur = con.cursor()

        try:
            cur.execute(f'SELECT * FROM public.{tableName} ORDER BY id')
            print(f"Table <{tableName}> found.")
            data = cur.fetchall()
            size = len(data)
            print(f"{tableName}")
            for x in range(size):
                print(f"{data[x]};")
            id = int(input("ID: "))
            cur.execute(f"select data from {tableName} where id = {id}")
            attribute1 = cur.fetchone()[0]
            print(f"You are about to delete {attribute1}, do you wish to proceed?\n(Y\\N)")
            if(input("") == 'Y' or 'y'):
                cur.execute(f"delete from {tableName} where id = {id}")
                print("Deletion successful.")
            else:
                print("Cancelled.")
        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(f"Table <{tableName}> not found.")
            print(error)

        con.commit()
        con.close()

    # Método utilizado para visualizar um item específico da tabela informada
    def viewItem(self, con):
        tableName = input("Table: ")
        cur = con.cursor()

        if(cur.execute("select * from information_schema.tables where table_name = %s", (tableName,))):
            print("Table name does not exist.")
        else:
            print(f"Table <{tableName}> found.")
            id = input("ID: ")
            cur.execute(f"SELECT * FROM {tableName} WHERE id = {id};")
            row = cur.fetchone()
            print("Current item values:")
            print(row)

        con.close()

    def printTable(self, rows, columns, data):
        return super().printTable(rows, columns, data)