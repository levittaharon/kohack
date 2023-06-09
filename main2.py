import time
import datetime
import threading
import student_class
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import socket    
        


#The function needs 3 parameters, all for integer values. 
#First value: 1 for USD, 2 for CAD, 3 for GBP, and 4 for EUR.
#Second parameter is a 1 or 2-- A 1 lets us know that the final output should be in the foreign currency, a 2 for shekels
#Last parameter specifies the actual value you wish to convert. If a 1 is specified in the second parameter, this parameter 
#will be in shekels. If the second parameter is a 2, this will be in the specified foreign currency."""
def convert(orig, to_or_from, value_orig):
    cur=["EMPTY", 4500]
    my_url='https://google.com'
    spec_class='hello'
    match orig:
        case 1:
            cur[0]="USD"
            my_url='https://www.google.com/finance/quote/USD-ILS?sa=X&ved=2ahUKEwiDjLiU--b9AhXkmokEHdNqCEgQmY0JegQIBhAd'
            spec_class="YMlKec fxKbKc"
        case 2:
            cur[0]="CAD"
            my_url='https://www.google.com/finance/quote/CAD-ILS?sa=X&ved=2ahUKEwjq3cGLq-j9AhXGFFkFHbg7CDwQmY0JegQIBhAd'
            spec_class="YMlKec fxKbKc"
        #case 4:
        #    cur[0]="EUR"
        #    url='https://www.google.com/finance/quote/EUR-ILS?sa=X&ved=2ahUKEwjuyvisq-j9AhVBFFkFHfO2D68QmY0JegQIBhAd'
        #    spec_class="YMlKec fxKbKc"
        case 3:
            cur[0]="GBP"
            my_url='https://www.google.com/finance/quote/GBP-ILS?sa=X&ved=2ahUKEwjBiaHNq-j9AhUzVTUKHYb6Cj8QmY0JegQIBhAd'
            spec_class="YMlKec fxKbKc"
        case _:
            print("ERROR: Please try again")
    res= requests.get(my_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    get_value = soup.find_all(class_=spec_class)[0].text
    conversion_factor=float(get_value)
    match to_or_from:
        case 2:
            cur[0]="SHKL"
            cur[1]=(conversion_factor*value_orig)
        case 1:
            cur[1]=(value_orig/conversion_factor)
        case _:
            print("ERROR")
    return(cur)




# Class to create instance of inventroy item. Respectively, the parameters are as follows:
# 1. NAME: The name of the item, 2. HUMAN: the name of the organizer, 3. MODE: the mode (1 for bulk orders, 2 for used items), 
# 4. CATEGORY: the category of the item (food, books, amenities), 5. STUDENTPRICE: the price per piece in bulk order, 6. DURATION: the duration until expiry of the offer in seconds, 
# 7. AMOUNT: the amount of individual pieces remaining to be pruchased in order, 8. STOCK: In the case of used items, the amount of the item in stock, 9. INFO: More info on the object
# 10. HUMANLIST: list of participating students
class Item():
    def __init__(self, name, human, mode, category, studentprice, duration, amount, stock, info, humanlist):
        print(f"New {name} Item created\n")
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
        self.thread.start()
    def countdown(self):
        for i in range(self.duration):
            time.sleep(1)
            self.duration-=1
        print(f"{self.name} expired\n")
        send(f"{self.name} expired\n")
        

#while Inventory["Pizza"].duration >0:
#    print(Inventory["Pizza"].duration)
 
class Operation():
    
    ##IMPORTANT: Both the Studens Dictionary and the Items Dictionary are Static, meaning they do not differ based on the instance of a class and remain the same. 
    # All instances access the same dictionary and a change will affect all instances
    
    #Student Repository. The name of the student is the dictionary key, and the value is a list in the following format: 
    # [password, email, phone-number, [EMPTY LIST IN WHICH STUDENTS ORDERS WILL BE STORED]]
    
    def createStudents():
        
    Students = {"John": ["613770", "j@F.com", "-8544-58-9234452", ["Hotdogs"]], "Johannes": ["hi", "hi@F.com", "-8544-58-9234452", []]}
    #{Name: List of:  password, email, phone number, list of orders joined}
    def createInventory():
    #Inventory of items contains keys which are the names of the item, and an isntance of an item class as their value
    Inventory = {"Pizza" : Item("Pizza", "Shloimy", 1, "Food", "$2", 500, 9, 1, "Tel Aviv Pizza Shop", ["Shloimy"]), 
                 "Hotdogs" : Item("Hotdogs", "John", 1, "Food", "$1", 500, 12, 1, "Walmart", ["John"])}
    
    
    #The constructor takes in the mode, digit 1 for bulk orders, and the digit 2 for buing/selling
    def __init__(self, mode, category):
        self.mode = int(mode)
        self.category = category
    
    #Function validates the user and only proceeds once successful. 
    def uservalidation(self):
        self.name = input("Please enter Name: ")
        self.password = input("Please enter your password: ")
        self.templist = self.modedlistofstuff()
        for key, value in Operation.Students.items():
            if self.name == key:
                if self.password==value[0]:
                    return True
                    #Will terminate the rest of the code and return True, allowing the user to proceed with the rest of the program
                else:
                    retry = int(input("Incorrect Password\nTry Again? \n1.Yes, 2.No\n"))
                    if retry==2:
                        return False
                    else:
                        self.uservalidation()
        # Will prompt the user to create a new id and passowrd if none exists
        newchoice = int(input("No such user, would you like to create one?\n1. Yes, 2. No\n"))
        if newchoice==1:
            email = input("Please enter Email: ")
            phone = input("Please enter Phone: ")
            #Adds the student to the Students dictionary with the value being a list, as noted above.
            Operation.Students[self.name]=[self.password, phone, email, []]
            return True
        else:
            return False
                    
    
    #Creates a list of stuff specific to the mode with which the class is instantiated.
    def modedlistofstuff(self):
        self.modedinventory = {}
        for key, value in Operation.Inventory.items():
            #for every Item class instance in the inventory, if its mode is equal to this class mode, the Items are added to a Dictionary with their names as the key.
            #The function returns a dictionary
            if value.mode == self.mode and value.category==self.category:
                self.modedinventory[key] = value
        return self.modedinventory
    
    #This function prints each item in the inventory
    def printavailableinventory(self):
        inventory = self.modedlistofstuff()
        for key, value in inventory.items():  
            print(f"item: {key}, organizer: {value.human}, price you pay: {value.studentprice}, Expires in {value.duration} secs, contributions needed: {value.amount}, quantity of bulk: {value.stock}, participants: {value.humanlist}", "\n")
    
    #This function prints the additional info of the selected Item (choice)
    def info(self, choice):
        print(self.modedlistofstuff()[choice].info)
    
    #Allows the person to join the order, taking in as parameters the exact item he is joining and the amount of it he is purchasing
    def joinorder(self):
        self.choice = input("Please enter item name: ")
        print(Operation.Inventory[self.choice].duration)
        self.amount = input("Please enter item amount: ")
        if self.choice not in Operation.Inventory:
            self.newchoice = int(input("Item not found\nWould you like to create an order?\n1. Yes, 2.No\n"))
            if self.newchoice==1:
                self.addtoinventory(self.mode, self.category)
        else:    
            if self.uservalidation() and self.name not in Operation.Inventory[self.choice].humanlist:
                print("Order Joined\n")
                #Subrtacts the amount the man ordered from the item amount
                Operation.Inventory[self.choice].amount-=int(self.amount)
                #Appends the name of the orderee to the list of people involved in the order
                Operation.Inventory[self.choice].humanlist.append(self.name)
                #Adds the order to the list of orders the Student is involved in
                Operation.Students[self.name][-1].append(self.choice) 
                #If the amount needed to complete the order is at 0, the item is ordered
                if self.templist[self.choice].amount==0:
                    self.order(self.choice, self.name)
                    return True
            else:
                n = int(input("Order already joined\nWould You like to update the Order? \n1.Yes, 2.No\n"))
                if n==1:
                    Operation.Inventory[self.choice].amount-=int(self.amount)
                    if self.templist[self.choice].amount==0:
                        self.order(self.choice, self.name)
                        return True
                    
    
    def addtoinventory(self, Mode, category):
        self.choice = input("Please enter item name: ")
        self.category =category
        self.mode = Mode
        if self.uservalidation():
            self.studentprice, self.duration, self.amount, self.stock, self.info =input("").split(", ")
            Operation.Inventory[self.choice] = Item(self.choice,self.name, self.mode, self.category, self.studentprice, self.duration, self.amount, self.stock, self.info, [self.name])
            return True     
    def cancelorder(self, choice):
        print("ordercanceled\n")
        del self.modedlistofstuff()[choice]
    def order(self, choice, name):
        print(f"{choice} ordered!\n")
        history = open("history.txt", "a")
        history.write(f"Item: {choice}, Posted by {Operation.Inventory[choice].human}, Bought By {Operation.Inventory[choice].humanlist}\n")
        history.close
        del Operation.Inventory[choice]
        Operation.Students[name][-1].remove(choice)
    def buy(self):
        self.choice = input("Please enter item name: ")
        if self.uservalidation():
            if self.choice in Operation.Inventory:
                with open("history.txt", "a") as history:
                    history.write(f"Item: {self.choice}, Posted by {Operation.Inventory[self.choice].human}, Bought By {self.name}\n")
                del Operation.Inventory[self.choice]  
                #Operation.Students[self.name][-1].remove(self.choice)
                print(f"{self.choice} purchased!\n")
    def categories():
        categors = []
        for key, value in Operation.Inventory.items():
            if value.category not in categors:
                categors.append(value.category)
        return categors
            
while True:
    Mode = int(input("Welcome to the Yeshiva Marketplace\nPlease select the following options: \n 1. Group Order \n 2. Buy/Sell\n 3.Currency Converter\n"))
    if Mode==1 or Mode==2:    
        category=  input(f"Please enter one of the following categories: {Operation.categories()}")
        program = Operation(Mode, category)
        program.printavailableinventory()
    if Mode==1:    
        choice = int(input("1. Join Order\n2. Create Order\n"))
        if choice == 1:
            program.joinorder()
            print(Operation.Inventory)
            program.printavailableinventory()
            print(Operation.Students)
        elif choice == 2:
            program.addtoinventory(Mode, category)
    elif Mode==2:
        choice = int(input("1. Post Item\n2.Buy Item\n"))
        if choice == 1:
            program.addtoinventory(Mode, category)
            print(Operation.Inventory)
            program.printavailableinventory()
            print(Operation.Students)
        elif choice == 2:
            program.buy()
    elif Mode ==3:
        currency=float(input("Please select one: 1.USD 2.CAD 3.GBP\n"))
        convert_dir=float(input("Select original currency: 1.SHKL 2.Other\n"))
        my_value=float(input("Value of original currency: "))
        print(str(round(convert(currency, convert_dir, my_value)[1], 2)))
        print(convert(currency, convert_dir, my_value)[0])
    for key, value in Operation.Inventory.items():
        if value.duration == 0:
            del Operation.Inventory[key]
        
             

