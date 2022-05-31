import psycopg2
from DbConnectionData import DbConnectionData

class DbConnection():

    def openConnection(c):
        try:
            con = psycopg2.connect(
                host = c.host,
                dbname = c.dbname,
                user = c.user,
                password = c.pwd
            )
            return con
        except (Exception, psycopg2.errors.ConnectionFailure) as error:
            print(error)