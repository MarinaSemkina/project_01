import sqlite3

def get_connection():
  connection = sqlite3.connect('Students.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = sqlite3.connect("School.db")
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
    
    
  except (Exception, sqlite3.Error) as erorr:
    print ("Ошибка в получении данных", erorr)

def get_students(school_id):
  try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = """SELECT * FROM Students WHERE School_Id = ?"""
    cursor.execute(sql_select_query, (school_id,))
    records = cursor.fetchall()
    
    for row in records:
      print ("ID Студента ", row[0])
      print ("Имя Студента: ", row[1])
      print ("ID Школы ", row[2])
      print ("Название школы: " , school_name)
      
      
  except (Exception, sqlite3.Error) as erorr:
    print ("Ошибка в получении данных", erorr)

print ("Написать программу, с помощью которой по ID студента можно получать информацию о школе и студенте. \n")

get_students(1)
