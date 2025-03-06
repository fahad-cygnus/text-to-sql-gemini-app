import sqlite3

def read_sql_query(sql, db):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute(sql)
  rows = cur.fetchall()
  conn.commit()
  conn.close()
  for row in rows:
    print(row)
  return rows

def get_all_students(db):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute("SELECT * FROM STUDENT")  # Query to select all students
  rows = cur.fetchall()
  conn.close()
  return rows