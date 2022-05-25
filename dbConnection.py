import psycopg2
from dbData import dbData

class dbConnection():

    def openConnection(c):

        try:
            print(f"Trying connection to <{c.dbname}> at <{c.host}>...")
            con = psycopg2.connect(
                host = c.host,
                dbname = c.dbname,
                user = c.user,
                password = c.pwd
            )
            print("Connection was successful.\n")
            return con
        except (Exception, psycopg2.errors.ConnectionFailure) as error:
            print(error)