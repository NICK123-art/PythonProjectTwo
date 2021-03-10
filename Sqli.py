import sqlite3

conn = sqlite3.connect("myData.db")
cursor = conn.cursor()
sql = '''Create table students(
         id int,
         name text
         gender text)'''
cursor.execute(sql)
cursor.close()
conn.close()