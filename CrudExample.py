import psycopg2
from Model import Model
from DbConnection import DbConnection
from DbMetadata import DbMetadata

class CrudExample(Model):
    
    def __init__(self, c, tableName):
        self.c = c
        self.tableName = tableName

    # Método substituto da viewTable dos exemplos, pega uma table do banco e printa ela na tela
    def viewTable(self):
        lineCount = DbMetadata.getTableLineCount(self.c, self.tableName)
        columnCount = DbMetadata.getTableColumnCount(self.c, self.tableName)
        print("Column count:", columnCount)
        print("Line count:", lineCount)
        s = f"DATA FROM TABLE <{self.tableName}>:"
        print(s.upper())
        table = DbMetadata.getTable(self.c, self.tableName)
        self.printTable(lineCount, columnCount, table)

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
    def insertItem(self, con, data):
        con = DbConnection.openConnection(self.c)
        cur = con.cursor()

        try:
            print(type(data[0]), type(data[1]), type(data[2]))
            cur.execute(f"INSERT INTO {self.tableName} VALUES ({data[0]}, {data[1]}, '{data[2]}')")
            cur.execute(f"SELECT * FROM {self.tableName} WHERE id = {id}")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()
        con.close()

    # Método utilizado para deletar um item escolhido da tabela informada
    def deleteItem(self, con):
        cur = con.cursor()

        try:
            cur.execute(f'SELECT * FROM public.{self.tableName} ORDER BY id')
            print(f"Table <{self.tableName}> found.")
            data = cur.fetchall()
            size = len(data)
            print(f"{self.tableName}")
            for x in range(size):
                print(f"{data[x]};")
            id = int(input("ID: "))
            cur.execute(f"select data from {self.tableName} where id = {id}")
            attribute1 = cur.fetchone()[1]
            print(f"You are about to delete {attribute1}, do you wish to proceed?\n(Y\\N)")
            if(input("") == 'Y' or 'y'):
                cur.execute(f"delete from {self.tableName} where id = {id}")
                print("Deletion successful.")
            else:
                print("Cancelled.")
        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(f"Table <{self.tableName}> not found.")
            print(error)

        con.commit()
        con.close()

    # Método utilizado para visualizar um item específico da tabela informada
    def viewItem(self, con):
        cur = con.cursor()

        if(cur.execute("select * from information_schema.tables where table_name = %s", (self.tableName,))):
            print("Table name does not exist.")
        else:
            print(f"Table <{self.tableName}> found.")
            id = input("ID: ")
            cur.execute(f"SELECT * FROM {self.tableName} WHERE id = {id};")
            row = cur.fetchone()
            print("Current item values:")
            print(row)

        con.close()

    def updateItem(self, con, data):
        cur = con.cursor()

        try:
            print(type(data[0]), type(data[1]), type(data[2]))
            cur.execute(f"UPDATE {data[0]} WHERE table = '{self.tableName}' VALUES ({data[1]}, '{data[2]}')")
            cur.execute(f"SELECT * FROM {self.tableName} WHERE id = {data[0]}")
            row = cur.fetchone()
            print(row)

        except(Exception, psycopg2.errors.DatabaseError) as error:
            print(error)
        
        con.commit()

    def printTable(self, lines, columns, data):
        return super().printTable(lines, columns, data)