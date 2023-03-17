import sqlite3
class student:
  #take in name and password because all functions require it
  def __init__(self,name,password):
    self.name = name
    if len(password) >7:
      self.password = password
    else:
      return("invalid password")
  #this function takes in additional info about the student and adds it to the db
  def new_student(self,email,phone):
    #this is the db that will contain everything it's just simpler that way
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    #create a table for basic information of a student
    cur.execute("CREATE TABLE IF NOT EXISTS directory(name TEXT NOT NULL PRIMARY KEY,password,email,phone);")
    #this is in a try except statement because if the data isn't correct then we need to send the user an error message
    Try:
      cur.execute("INSERT INTO directory(?,?,?,?)",self.name,self.password,email,phone)
    Except:
      return("invalid username")
    
