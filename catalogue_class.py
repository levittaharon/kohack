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
            cur.execute(f"SELECT * FROM {category} WHERE mode IS ?;",(mode))
            check = cur.fetchall()
            if len(check) == 0:
                return(False)
            else:
                return(check)
        except:
            #this return statement would equate to a no inventory found message
            return(False)
