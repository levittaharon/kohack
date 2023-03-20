class new_market:
    def __init__(self,market_name):
        #this protects against someone trying to delete the directory with everyone's login
        if market_name != "directory":
            self.market_name = market_name
        else:
            self.market_name = False

    def create(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        #use try and except to make sure that value isn't false
        try:
            #this creates a table for the new market that the admin wants to add
            cur.execute(f"CREATE TABLE IF NOT EXISTS {self.market_name}(mode,item_name,seller_name,price,time_expire,amount_left,info,student_list);")
        except:
            print("issue with the table name please choose a different one")
        con.close()
    
    #when calling this function please send a warning first it can really mess things up if unintentional
    def delete(self): #this will delete an added market but for an original market all that his will do is reset it
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        try:
            #this creates a table for the new market that the admin wants to add
            cur.execute(f"DROP TABLE {self.market_name};")
        except:
            print("bad table name")
        con.close()
