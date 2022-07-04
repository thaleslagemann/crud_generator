import psycopg2
from DbConnection import DbConnection
from DbConnectionData import DbConnectionData
from DbMetadata import DbMetadata

class ClassWriter():

    def __init__(self, c, tableName):
        self.c = c
        self.tableName = tableName

    def writeDAOFile(self):
        mdt = DbMetadata.getTableMetadata(self.c, self.tableName)

        mdt_len = len(mdt)

        newFileName = self.tableName.capitalize()

        try:
            f = open(f'{newFileName}DAO.py', 'w')
            if(f):
                print("File opened successfully.\n")
            else:
                print("File opening failed.\n")

            m = open('DAOModel.txt', 'r')
            text = []
            text = m.readlines()
            identation = '    '
            
            for line in text:   
                if '__classDeclaration' in line:
                    sent = str()
                    sent += f"class {newFileName}DAO(Model):\n"
                    print('Found class declaration.')
                    print(f'Replacing __classDeclaration with:\n {sent}')
                    f.write(sent)
                elif '__tableNameDeclaration' in line:
                    sent = str()
                    for i in range(2):
                        sent += f'{identation}'
                    sent += f'self.tableName = \'{self.tableName}\'\n'
                    print('Found tablename declaration.')
                    print(f'Replacing __tableNameDeclaration with:\n {sent}')
                    f.write(sent)
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
                    for i in range(3):
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
                    for i in range(3):
                        sent += f'{identation}'
                    sent += 'cur.execute(f"DELETE FROM {self.tablename} WHERE '
                    sent += f'{mdt[0][0]}'
                    sent += ' = \'{data[0]}\'")\n'
                    print(f"Replacing __deleteStandardDeclaration with:\n {sent}")
                    f.write(sent)
                elif '__researchStandardDeclaration' in line and mdt_len != 0:
                    sent = str()
                    for i in range(3):
                        sent += f'{identation}'
                    sent += 'cur.execute(f"SELECT * FROM {self.tablename} WHERE '
                    sent += f'{mdt[0][0]}'
                    sent += ' = \'{data[0]}\'")\n'
                    print(f"Replacing __researchStandardDeclaration with:\n {sent}")
                    f.write(sent)
                else:
                    f.write(line)

        except (Exception) as error:
            print(error)

        finally:
            f.close()

    def writeEntityFile(self):

        mdt = DbMetadata.getTableMetadata(self.c, self.tableName)

        newFileName = self.tableName.capitalize()

        try:
            f = open(f'{newFileName}.py', 'w')

            if(f):
                print("File opened successfully.\n")
            else:
                print("File opening failed.\n")

            m = open('EntityModel.txt', 'r')
            text = []
            text = m.readlines()
            identation = '    '

            for line in text:
                if '__classDeclaration' in line:
                    sent = str()
                    sent += f"class {newFileName}:\n"
                    print('Found class declaration.')
                    print(f'Replacing __classDeclaration with:\n {sent}')
                    f.write(sent)
                elif '__initDeclaration' in line:
                    sent = str()
                    for i in range(1):
                        sent += f'{identation}'
                    sent += f"def __init__(self, c"
                    for data in mdt:
                        sent += f", {data[0]}"
                    sent += "):\n"
                    f.write(sent)
                elif '__tableNameDeclaration' in line:
                    sent = str()
                    for i in range(2):
                        sent += f'{identation}'
                    sent += f'self.tableName = \'{self.tableName}\'\n'
                    print('Found tablename declaration.')
                    print(f'Replacing __tableNameDeclaration with:\n {sent}')
                    f.write(sent)
                elif '__rowsDeclarationLoop' in line:
                    sent = str()
                    for data in mdt:
                        for i in range(2):
                            sent += f'{identation}'
                        sent += f'self.{data[0]} = {data[0]}\n'
                    f.write(sent)
                elif '__gettersDeclaration' in line:
                    sent = str()        
                    for data in mdt:
                        for i in range(1):
                            sent += f'{identation}'
                        sent += f'def get{data[0].capitalize()}({data[0]}):\n'
                        for i in range(2):
                            sent += f'{identation}'
                        sent += f'return {data[0]}\n\n'
                    f.write(sent)
                elif '__settersDeclaration' in line:
                    sent = str()        
                    for data in mdt:
                        for i in range(1):
                            sent += f'{identation}'
                        sent += f'def set{data[0].capitalize()}(self, {data[0]}):\n'
                        for i in range(2):
                            sent += f'{identation}'
                        sent += f'self.{data[0]} = {data[0]}\n\n'
                    f.write(sent)
                else:
                    f.write(line)

        except (Exception) as error:
            print(error)

        finally:
            f.close()