import mysql.connector 
class Data :
  def show_all_data():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Dunggttn1512.",
      database="WEBAPI_DB"
    )

    mycursor = mydb.cursor()
    sql = " SELECT * FROM Employee"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    f = '<div class="hidden">'
    for data in myresult:
      f += '<div class="data-student" attr-id="1">'
      f += f'<div id=ID>{data[0]}</div>'
      f += f'<div id=FirstName>{data[1]}</div>'
      f += f'<div id=LastName>{data[2]}</div>'
      f += f'<div id=Gender>{data[3]}</div>'
      f += f'<div id=Salary>{data[4]}</div>'
    print(f)

print(Data.show_all_data())