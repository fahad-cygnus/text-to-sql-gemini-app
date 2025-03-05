import sqlite3

## Connect to sqlite
## Following code will go ahead and create a new DB
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve records, can do anything
cursor=connection.cursor()

## Create the table, write the query - in this table we are going to create four important fields/colums
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Fahad','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Haider','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Haseeb','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Danish','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Rafay','Devops','A',35)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * From STUDENT''')
for row in data:
  print(row)

## Close the connection
connection.commit()
connection.close()