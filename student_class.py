import sqlite3
class student:
  #take in name and password because all functions require it
  def __init__(self,name,password):
    self.name = name
    if len(password) >7:
      self.password = password
    else:
      self.password = ""
  #this function takes in additional info about the student and adds it to the db
  def new_student(self,email,phone):
    #this is the db that will contain everything it's just simpler that way
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    #create a table for basic information of a student
    cur.execute("CREATE TABLE IF NOT EXISTS directory(name TEXT NOT NULL PRIMARY KEY,password,email,phone);")
    #check for invalid password to display correct error message
    if self.password != "":
    #this is in a try except statement because if the data isn't correct then we need to send the user an error message
      try:
        cur.execute("INSERT INTO directory(name,password,email,phone) VALUES(?,?,?,?);",(self.name,self.password,email,phone))
        conn.commit()
      except:
      #the only reason to get an error is if it is an invalid username since that is the specified data type
        print("invalid username")
    else:
      #if the password is "" then it is invalid this is from the init statement
      print("invalid password")
    #close the cursor because it is good practice if it is unnecessary to have it open
    cur.close()
  
  #this will check if it is a valid login and return all of the information for now
  def login(self):
    #this is necessary to access the cursor
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM directory WHERE name IS ? AND password IS ?;",(self.name,self.password))
    #check if the previous statement found a login matching the one submitted
    result = cur.fetchall()
    if len(result)== 0: #if it doesn't find anything then len is 0
      print("bad login")
    else:
      
      print(result)

