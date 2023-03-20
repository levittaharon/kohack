import sqlite3
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
            check = cur.fetchall()
            if len(check) == 0:
                print("nothing at this moment")
                return(False)
                
            else:
                print("success")
                print(check)
                return(check)
        except:
            #this return statement would equate to a no inventory found message
            print("error")
            return(False)
    def send_notification(self,info_list): #this function takes in a list with the item name as the 0 index and seller name as 1 index and amount left as 2 index
        user = info_list[1]
        item = info_list[0]
        stock = info_list[2]
        student_list = info_list[3]
        msg = f"dear {user} your {item} item has been ordered by {student_list} and has {stock} left in stock."
#for testing purposes only
#instance = catalogue()
#print("testing")
#instance.send_catalogue("books",True)
#print("done")
