import sqlite3
conn = sqlite3.connect("myData.db")
sql = '''Create table students(
         id int,
         name text)'''
conn.execute(sql)
conn.close()