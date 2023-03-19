import time
import datetime
import threading
import student_class

# Class to create instance of inventroy item. Respectively, the parameters are as follows:
# 1. NAME: The name of the item, 2. HUMAN: the name of the organizer, 3. MODE: the mode (1 for bulk orders, 2 for used items), 
# 4. CATEGORY: the category of the item (food, books, amenities), 5. STUDENTPRICE: the price per piece in bulk order, 6. DURATION: the duration until expiry of the offer in seconds, 
# 7. AMOUNT: the amount of individual pieces remaining to be pruchased in order, 8. STOCK: In the case of used items, the amount of the item in stock, 9. INFO: More info on the object
# 10. HUMANLIST: list of participating students
class Item():
    def __init__(self, name, human, mode, category, studentprice, duration, amount, stock, info, humanlist):
        print(f"New {name} Item created")
        self.name = name
        self.category = category
        self.studentprice = studentprice
        self.duration = duration
        self.amount = amount
        self.stock = stock
        self.info = info
        self.mode = mode
        self.human = human
        self.humanlist = humanlist
        self.thread = threading.Thread(target=self.countdown)
        self.thread.start
    def countdown(self):
        self.timeleft = self.duration
        for i in range(self.duration):
            time.sleep(1)
            self.timeleft-=1
        print("Item expired")
        

#while Inventory["Pizza"].duration >0:
#    print(Inventory["Pizza"].duration)
 
class Operation:
    ##IMPORTANT: Both the Studens Dictionary and the Items Dictionary are Static, meaning they do not differ based on the instance of a class and remain the same. 
    # All instances access the same dictionary and a change will affect all instances
    
    #Student Repository. The name of the student is the dictionary key, and the value is a list in the following format: 
    # [password, email, phone-number, [EMPTY LIST IN WHICH STUDENTS ORDERS WILL BE STORED]]
    Students = {"John": ["613770", "j@F.com", "-8544-58-9234452", []], "Johannes": ["hi", "hi@F.com", "-8544-58-9234452", []]}
    
    #Inventory of items contains keys which are the names of the item, and an isntance of an item class as their value
    Inventory = {"Pizza" : Item("Pizza", "Shloimy", 1, "food", "$2", 500, 9, 1, "Tel Aviv Pizza Shop", ["Shloimy"]),}
    
    #The constructor takes in the mode, digit 1 for bulk orders, and the digit 2 for buing/selling
    def __init__(self, mode):
        self.mode = int(mode)
    
    #This function creates a new user
    def createnewuser(self, name, password):
        email = input("Please enter Email: ")
        phone = input("Please enter Phone: ")
        #Adds the student to the Students dictionary with the value being a list, as noted above.
        Operation.Students[name]=[password, phone, email, []]
        return True
    
    #Creates a list of stuff specific to the mode with which the class is instantiated.
    def modedlistofstuff(self):
        self.modedinventory = {}
        for key, value in Operation.Inventory.items():
            #for every Item class instance in the inventory, if its mode is equal to this class mode, the Items are added to a Dictionary with their names as the key.
            #The function returns a dictionary
            if value.mode == self.mode:
                self.modedinventory[key] = value
        return self.modedinventory
    
    #This function prints each item in the inventory
    def printavailableinventory(self):
        inventory = self.modedlistofstuff()
        for key, value in inventory.items():  
            print(f"item: {key}, organizer: {value.human}, price you pay: {value.studentprice}, Expires in {value.duration} secs, contributions needed: {value.amount}, quantity of bulk: {value.stock} participants: {value.humanlist}", "\n")
    
    #This function prints the additional info of the selected Item (choice)
    def info(self, choice):
        print(self.modedlistofstuff()[choice].info)
    
    #Allows the person to join the order, taking in as parameters the exact item he is joining and the amount of it he is purchasing
    def joinorder(self, amount, choice):
        if choice not in Operation.Inventory:
            print("Item not found")
        else:    
            #Validates the user
            self.name = input("Please enter Name: ")
            self.password = input("Please enter your password: ")
            self.templist = self.modedlistofstuff()
            for key, value in Operation.Students.items():
                if self.name == key:
                    if self.password==value[0]:
                        print("Order Joined")
                        #Subrtacts the amount the man ordered from the item amount
                        Operation.Inventory[choice].amount-=int(amount)
                        #Appends the name of the orderee to the list of people involved in the order
                        Operation.Inventory[choice].humanlist.append(self.name)
                        #Adds the order to the list of orders the Student is involved in
                        Operation.Students[self.name][-1].append(choice)
                        
                        #If the amount needed to complete the order is at 0, the item is ordered
                        if self.templist[choice].amount==0:
                            self.order(choice, self.name)
                        return True
                    else:
                        print("Incorrect Password")
                        return False
            #If invalid, prompts the user to create a new user
            print("No such user, would you like to create one?")
            newchoice = int(input("1. yes, 2. no"))
            if newchoice==1:
                if self.createnewuser(self.name, self.password):
                    #Repeats the same process described earlier in joining and order
                    print("Order Joined")
                    Operation.Inventory[choice].amount-=int(amount)
                    Operation.Inventory[choice].humanlist.append(self.name)
                    Operation.Students[self.name][-1].append(choice)
                    if self.templist[choice].amount==0:
                        self.order(choice, self.name)
    
    
    def addtoinventory(self, item, Mode):
        self.item = item
        self.mode = Mode
        self.human = input("Please enter your name:")
        self.password = input("Please enter your password:")
        for key, value in Operation.Students.items():
            if self.human == key:
                if self.password==value[0]:
                    self.category, self.studentprice, self.duration, self.amount, self.stock, self.info =input("").split(", ")
                    Operation.Inventory[self.item] = Item(self.item, self.human, self.mode, self.category, self.studentprice, self.duration, self.amount, self.stock, self.info, [self.human])

    def cancelorder(self, choice):
        print("ordercanceled")
        del self.modedlistofstuff()[choice]
    def order(self, choice, name):
        print(f"{choice} ordered")
        del Operation.Inventory[choice]
        Operation.Students[name][-1].remove(choice)
        
 
    

print("Welcome to the Yeshiva Marketplace")
Mode = int(input("Please select the following options \n 1. Group Order \n 2. Buy/Sell\n"))
program = Operation(Mode)
program.printavailableinventory()
if Mode==1:    
    choice = int(input("1. Join Order\n2. Create Order"))
    item = input("Please enter item name")
    if choice == 1:
        amount = input("Please enter item amount")
        program.joinorder(amount, item)
        print(Operation.Inventory)
        program.printavailableinventory()
        print(Operation.Students)
    elif choice == 2:
        program.addtoinventory(item, Mode)
elif Mode==2:
    choice = int(input("1. Post Item\n2.Buy Item"))
    item = input("Please enter item name")
    if choice == 1:
        program.addtoinventory(item, Mode)
        print(Operation.Inventory)
        program.printavailableinventory()
        print(Operation.Students)
             

