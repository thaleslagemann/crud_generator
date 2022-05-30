import psycopg2
from dbConnection import dbConnection
from dbConnectionData import dbConnectionData

class classWriter():

    def __init__(self, c, tableName):
        self.c = c
        self.tableName = tableName

    def createFile(self):
        try:
            f = open(f'{self.tableName}.py', 'x')

            if(f):
                print("File created.")
            else:
                print("File not created.")
        except (Exception, FileExistsError) as error:
            print(error)

    def writeInFile(self):
        try:
            f = open(f'{self.tableName}.py', 'w')
            if(f):
                print("File opened successfully.")
            else:
                print("File opening failed.")
        except (Exception) as error:
            print(error)

        m = open('modeloWrites.txt', 'r')
        text = []
        text = m.readlines()

        for line in text:   
            print("Line reads:", line)
            if line == '__classDeclaration\n':
                f.write(f'class {self.tableName}DAO(model):\n')
                print('Found class declaration.')
                print(f'Replacing with "class {self.tableName}DAO(model):\\n"')
            else:
                f.write(line)
                