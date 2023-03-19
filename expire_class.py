import sqlite3
class expire:
    def __init__(self,category):
        self.category = category
    
    def check_expired(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute(f"DELETE FROM {self.category} WHERE time_expire <= datetime('now');")
        
        
        con.close()
    
    def check_stock(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute(f"SELECT item_name,seller_name FROM {self.category} WHERE amount_left IS '0';")
        info = cur.fetchall()  
        print(info)      
        cur.execute(f"DELETE FROM {self.category} WHERE amount_left IS '0';")
        con.commit()
        con.close()
        
        return(info)
"""
#thes are all for testing
instance = expire("books")
instance.check_stock()
"""
