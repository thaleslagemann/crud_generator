# Python CRUD Generator for Postgre Databases

This Python application requires the PostgreSQL database adapter, Psycopg2, which can be downloaded [here](https://pypi.org/project/psycopg2/), or through the following python terminal command:
```
pip install psycopg2
```

The application takes input of your postgre *host*, *database*, *username* and *password*, then you get to choose the respective *table* from the database which you want to generate the CRUD, the program then generates a DAO (Data Acess Object) file, an Entity file and an usage example file.
