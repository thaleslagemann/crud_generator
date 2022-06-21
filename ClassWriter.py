import psycopg2
from DbConnection import DbConnection
from DbConnectionData import DbConnectionData
from DbMetadata import DbMetadata

class ClassWriter():

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
        mdt = DbMetadata.getTableMetadata(self.c, self.tableName)

        mdt_len = len(mdt)
        print(self.tableName)
        print(mdt_len)

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
        identation = '    '
        
        for line in text:   
            print("Line reads:", line)
            if '__classDeclaration' in line:
                f.write(f'class {self.tableName}DAO(Model):\n')
                print('Found class declaration.')
                print(f'Replacing with "class {self.tableName}DAO(Model):\\n"')
            elif '__tableNameDeclaration' in line:
                sent = str()
                for i in range (2):
                    sent += f'{identation}'
                sent += f'self.tableName = \'{self.tableName}\'\n'
                f.write(sent)
                print('Found tablename declaration.')
                print(f'Replacing with: {sent}')
            elif '__insertStandardDeclaration' in line and mdt_len != 0:
                sent = str()
                for i in range (3):
                    sent += f'{identation}'
                sent += 'cur.execute(f"INSERT INTO {self.tableName} VALUES ({data[0]}'
                for i in range(mdt_len - 1):
                    sent += ", {data["
                    sent += f"{i + 1}]"
                    sent += "}]"
                sent += ')")\n'
                print(f"Replacing __insertStandardDeclaration with:\n {sent}")
                f.write(sent)
            elif '__updateStandardDeclaration' in line and mdt_len != 0:
                sent = str()
                for i in range (3):
                    sent += f'{identation}'
                sent += 'cur.execute(f"UPDATE {data[0]} WHERE table = \'{self.tableName}\' VALUES ({data[0]}'
                for i in range(mdt_len - 1):
                    sent += ", {data["
                    sent += f"{i + 1}]"
                    sent += "}]"
                sent += ')")\n'
                print(f"Replacing __updateStandardDeclaration with:\n {sent}")
                f.write(sent)
            elif '__deleteStandardDeclaration' in line and mdt_len != 0:
                sent = str()
                for i in range (3):
                    sent += f'{identation}'
                sent += 'cur.execute(f"DELETE FROM {self.tablename} WHERE '
                sent += f'{mdt[0][0]}'
                sent += ' = \'{data[0]}\'")'
                sent += '\n'
                print(f"Replacing __deleteStandardDeclaration with:\n {sent}")
                f.write(sent)
            else:
                f.write(line)
