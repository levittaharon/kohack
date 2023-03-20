import sqlite3
from student_class import student
class catalogue:
    def __init__(self):
        pass
    def send_catalogue(self, category,mode):
        #use try except in case for whatever reason the table is empty
        try:
                #get all of the values from the desired category and mode
            con = sqlite3.connect("students.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM {category} WHERE mode IS True;")
            check = list(cur.fetchall())
            final = []
            con.close()
            for i in check:
                i =list(i)
                final.append(i)
            if len(check) == 0:
                #print("nothing at this moment")
                #false means means nothing in db
                return(False)
                
            else:
                #print("success")
                #print(final)
                return(final)
        except:
            #this return statement would equate to a no inventory found message
            print("error")
            return(False)
    
    def fetch_directory(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        #fetch the entire directory in a way which can be read as a dictionary
        cur.execute(f"SELECT * FROM directory;")
        dictionary = {}
        check = cur.fetchall()
        con.close()
        #each row needs to be adictionary value so iterate through each one
        for i in check:
            i = list(i)
            #this if statement turns the orders part of into a list
            if i[5] == '':
                i[5] = []
            else:
                i[5] = list(i[5])
            dictionary[i[0]] = [i[1],i[2],i[3],i[5]] #this coresponds to name = [password,email,phone,orders_part_of]

        print(dictionary)
        return(dictionary)

      #this will take in a dictionary and update the db
    #the dictionary is {name:[password,email,phone,orders_by_user]}
    def update_student(self,dictionary):
        
        #use a for loop to iterate through each row
        for key,value in dictionary.items():
            #initialize the db this is done in the for loop to check if there is a new student
            con = sqlite3.connect("students.db")
            cur = con.cursor()
            
            password = value[0]
            email = value[1]
            phone = value[2]
            orders = str(value[3])
            cur.execute("SELECT * FROM directory WHERE name IS ?;",(key,)) #key is the name
            check = cur.fetchall()
            if len(check) != 0: #if student exists
                cur.execute("UPDATE directory SET orders_part_of = ? WHERE name is ?",(orders,key)) #key is the name
            else:
                #create new instance of student do it this way to validate the password
                student(key,password).new_student(email,phone)
                cur.execute("UPDATE directory SET orders_part_of = ? WHERE name is ?;",(orders,key)) #key is the name
            con.commit()
            con.close()



            



    def send_tabs(self): #this function sends the correct tabs to the gui
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM tab_list;")
        check = cur.fetchall()
        return(check)

    def send_notification(self,info_list): #this function takes in a list with the item name as the 0 index and seller name as 1 index and amount left as 2 index
        user = info_list[1]
        item = info_list[0]
        stock = info_list[2]
        student_list = info_list[3]
        #make sure that it's one big notification statement
        if msg == "":
            msg = f"dear {user} your {item} item has been ordered by {student_list} and has {stock} left in stock. \n"
            
        else:
            msg += f"dear {user} your {item} item has been ordered by {student_list} and has {stock} left in stock. \n"
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("UPDATE directory SET notification = ? WHERE name IS ?;",(msg,user))
#for testing purposes only
#instance = catalogue()
#print("testing")
#instance.send_catalogue("books",True)
#print("done")
#catalogue().update_student({"john":["goodpass","email","773",["new_order"]]})
