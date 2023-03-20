from catalogue_class import catalogue
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
        #check if item is still in stock and if not it needs to be deleted and the owner must be notified
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        #if stock is 0 then it needs to go
        cur.execute(f"SELECT item_name,seller_name FROM {self.category} WHERE amount_left IS ? ;",(0))
        info = cur.fetchall()        
        cur.execute(f"DELETE FROM {self.category} WHERE amount_left IS ? ;",(0))
        con.commit()
        con.close()
        
        for i in info: #make a list for each data set to pass in 
            message = list(i)
            catalogue().send_notification(message)
            
"""
#thes are all for testing
instance = expire("books")
instance.check_stock()
"""

