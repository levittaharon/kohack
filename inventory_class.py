import sqlite3
class inventory:
    # parameters are as follows:
    # 1. NAME: The name of the item, 2. HUMAN: the name of the organizer, 3. MODE: the mode (1 for bulk orders, 2 for used items or food), 
    # 4. CATEGORY: the category of the item (food, books, amenities), 5. STUDENTPRICE: the price per piece in bulk order, 6. DURATION: the duration until expiry of the offer in seconds, 
    # 7. AMOUNT: the amount of individual pieces remaining to be pruchased in order, 8. STOCK: In the case of used items, the amount of the item in stock, 9. INFO: More info on the object
    # 10. HUMANLIST: list of participating students
    
    #for anything that is not necessary put in false as param
    def __init__(self,item_name,seller_name,mode,category,price,time_left,amount_left,info,student_list):
        self.item_name = item_name #only necessary if specific item
        self.seller_name = seller_name
        self.mode = mode #bulk or individual
        self.category = category 
        self.price = price
        self.time_left = time_left
        self.amount_left = amount_left
        self.info = info
        self.student_list = student_list

        #create a table in the student database that keeps track of the orders for each category
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books(mode,item_name,seller_name,price,time_expire,info,student_list);")
        cur.execute("CREATE TABLE IF NOT EXISTS food(mode,item_name,seller_name,price,time_expire,info,student_list);")
        cur.execute("CREATE TABLE IF NOT EXISTS ammenities(mode,item_name,seller_name,price,time_expire,info,student_list);")

     