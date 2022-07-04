# Python CRUD Generator for Postgre Databases

This Python application requires the PostgreSQL database adapter, Psycopg2, which can be downloaded [here](https://pypi.org/project/psycopg2/), or through the following python terminal command:
```
pip install psycopg2
```

It does also needs the Faker library, to generate fake data for the example files, which can be installed using the following terminal command:
```
pip install faker
```

To run the application all you have to do is run the main.py file:
```
py main.py
```

The application takes input of your postgre *host*, *database*, *username* and *password*, then you get to choose the respective *table* from the database which you want to generate the CRUD, the program then generates a DAO (Data Acess Object) file, an Entity file and an usage example file.
