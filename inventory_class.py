from catalogue_class import catalogue
import sqlite3
class inventory:
    # parameters are as follows:
    # 1. NAME: The name of the item, 2. HUMAN: the name of the organizer, 3. MODE: the mode (1 for bulk orders, 2 for used items or food), 
    # 4. CATEGORY: the category of the item (food, books, amenities), 5. STUDENTPRICE: the price per piece in bulk order, 6. DURATION: the duration until expiry of the offer in seconds, 
    # 7. AMOUNT: the amount of individual pieces remaining to be pruchased in order, 8. STOCK: In the case of used items, the amount of the item in stock, 9. INFO: More info on the object
    # 10. HUMANLIST: list of participating students
    
    #for anything that is not necessary put in false as param
    def __init__(self,item_name,seller_name,mode,category,price,time_left,amount_left, info,student_list):

        self.item_name = item_name #only necessary if specific item
        self.seller_name = seller_name
        self.mode = mode #bulk or individual
        
        self.category = category #this shoud be a string containing "food", "ammenities" or "books"
        self.price = price
        self.time_left = time_left
        self.amount_left = amount_left
        self.info = info
        self.student_list = str(student_list)

        #create a table in the student database that keeps track of the orders for each category
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books(mode,item_name,seller_name,price,time_expire,amount_left INTEGERL,info,student_list);")
        cur.execute("CREATE TABLE IF NOT EXISTS food(mode,item_name,seller_name,price,time_expire,amount_left INTEGER,info,student_list);")
        cur.execute("CREATE TABLE IF NOT EXISTS ammenities(mode,item_name,seller_name,price,time_expire,amount_left INTEGER,info,student_list);")
        cur.execute("CREATE TABLE IF NOT EXISTS luggage(mode,item_name,seller_name,price,time_expire,amount_left INTEGER,info,student_list);")
        cur.execute("CREATE TABLE IF NOT EXISTS transport(mode,item_name,seller_name,price,time_expire,amount_left INTEGER,info,student_list);")
        #make a 1 column db to keep track of which tabs are being used to send to gui
        cur.execute("CREATE TABLE IF NOT EXISTS tab_list(tab_name);")
        cur.execute("INSERT INTO tab_list (tab_name) VALUES ('books'), ('food'), ('ammenities'), ('luggage'), ('transport');")#insert all of the defauslt values
        con.close()
    def add_item(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        #check if item is already in the db in which case we don't allow it
        cur.execute(f"SELECT * FROM {self.category} WHERE item_name IS ? AND seller_name IS ?;",(self.item_name,self.seller_name))
        check = cur.fetchall()
        if len(check) == 0:
            cur.execute(f"INSERT INTO {self.category} (mode,item_name,seller_name,price,time_expire,amount_left,info,student_list) VALUES (?,?,?,?,?,?,?,?);",(self.mode,self.item_name,self.seller_name,self.price,self.time_left,self.amount_left,self.info,self.student_list))
            

        else:
            return(False)
        con.commit()
        con.close
    
    def delete(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute(f"DELETE FROM {self.category} WHERE item_name IS ? AND seller_name IS ?;",(self.item_name,self.seller_name))
        con.commit()
        con.close

    def order(self,amount):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute(f"SELECT item_name,amount_left,student_list FROM {self.category} WHERE item_name IS ? and seller_name IS ?;",(item_name,seller_name))
        info_list = cur.fetchall()
        info_list = list(info_list)
        new_stock = info_list[1] -amount #get rid of ordered item from stock
        cur.execute(f"UPDATE {self.category} SET amount_left = ? WHERE item_name IS ? and seller_name IS ?;",(new_stock,item_name,seller_name))
        catalogue.send_notification(info_list)

        
        

    

    



"""        
#these 2 lines are for testing only
instance = inventory("book","harry",True,"books","price","time_expire","0","info","student_list")
instance.add_item()

instance = inventory("item_name","seller_name",True,"books","price","time_expire","0","info","student_list")
instance.delete()
"""
