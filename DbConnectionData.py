class DbConnectionData():

    def __init__(self) -> None:
        self.host = str(None)
        self.dbname = str(None)
        self.user = str(None)
        self.pwd = str(None)

    def getHost(self):
        return self.host

    def setHost(self, host):
        self.host = host

    def getDbname(self):
        return self.dbname

    def setDbname(self, dbname):
        self.dbname = dbname

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user

    def getPwd(self):
        return self.pwd

    def setPwd(self, pwd):
        self.pwd = pwd
