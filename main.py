from dbConnection import dbConnection
from crud_generator import crud_generator
from dbData import dbData
from dbMetadata import dbMetadata

c = dbData()
   
c.setHost(c.getHost())
        
c.setDbname(c.getDbname())
        
c.setUser(c.getUser())
        
c.setPwd(c.getPwd())

dbmdt = dbMetadata(c)
dbmdt.getMetadata()
#a = client()
#a._set_sql_insertion("INSERT test IN test")
#a.print_value()