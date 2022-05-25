import getpass


class dbData():

    def __init__(self) -> None:
        self.host = str(None)
        self.dbname = str(None)
        self.user = str(None)
        self.pwd = str(None)

    def getHost(self):
        host = input("Host: ")
        return host

    def setHost(self, host):
        self.host = host

    def getDbname(self):
        dbname = input("DB Name: ")
        return dbname

    def setDbname(self, dbname):
        self.dbname = dbname

    def getUser(self):
        user = input("User: ")
        return user

    def setUser(self, user):
        self.user = user

    def getPwd(self):
        pwd = input("Password: ")
        return pwd

    def setPwd(self, pwd):
        self.pwd = pwd

#    host = "localhost"
#    dbname = "testDB"
#    user = "testUsr"
#    pwd = "tstusr"