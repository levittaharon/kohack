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

#for testing purposes only
#instance = catalogue()
#print("testing")
#instance.send_catalogue("books",True)
#print("done")
