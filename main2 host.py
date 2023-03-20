import time
import threading
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import socket
from inventory_class import inventory
from student_class import student
from catalogue_class import *


student("John", "61377000").new_student("gdsgf@dsf.com", "42352356423")
      
host = "192.168.60.90"
port = 55555

#Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET: internet socket, #SOCK_STREAM: TCP protocol
server.bind((host, port))
server.listen()

client, address = server.accept()

client.send("Connected to server!".encode("utf-8"))

def receive():
    return(client.recv(1024).decode("utf-8"))
def send(message):
    client.send(message.encode("utf-8"))
send("Connected with {}".format(str(address)))


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
            send("ERROR: Please try again")
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
            send("ERROR")
    return(cur)




# Class to create instance of inventroy item. Respectively, the parameters are as follows:
# 1. NAME: The name of the item, 2. HUMAN: the name of the organizer, 3. MODE: the mode (1 for bulk orders, 2 for used items), 
# 4. CATEGORY: the category of the item (food, books, amenities), 5. STUDENTPRICE: the price per piece in bulk order, 6. DURATION: the duration until expiry of the offer in seconds, 
# 7. AMOUNT: the amount of individual pieces remaining to be pruchased in order, 8. STOCK: In the case of used items, the amount of the item in stock, 9. INFO: More info on the object
# 10. HUMANLIST: list of participating students
class Item():
    def __init__(self, name, human, mode, category, studentprice, duration, amount, stock, info, humanlist):
        send(f"New {name} Item created\n")
        send(f"New {name} Item created\n")
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
        send(f"{self.name} expired\n")
        send(f"{self.name} expired\n")
        

#while Inventory["Pizza"].duration >0:
#    send(Inventory["Pizza"].duration)
 
class Operation():
    
    ##IMPORTANT: Both the Studens Dictionary and the Items Dictionary are Static, meaning they do not differ based on the instance of a class and remain the same. 
    # All instances access the same dictionary and a change will affect all instances
    
    #Student Repository. The name of the student is the dictionary key, and the value is a list in the following format: 
    # [password, email, phone-number, [EMPTY LIST IN WHICH STUDENTS ORDERS WILL BE STORED]]
    Students = catalogue().fetch_directory()
    #Students = {"John": ["613770", "j@F.com", "-8544-58-9234452", ["Hotdogs"]], "Johannes": ["hi", "hi@F.com", "-8544-58-9234452", []]}
    #{Name: List of:  password, email, phone number, list of orders joined}
    #Inventory of items contains keys which are the names of the item, and an isntance of an item class as their value
    Inventory = {"Pizza" : Item("Pizza", "Shloimy", 1, "Food", "$2", 500, 9, 1, "Tel Aviv Pizza Shop", ["Shloimy"]), 
                 "Hotdogs" : Item("Hotdogs", "John", 1, "Food", "$1", 500, 12, 1, "Walmart", ["John"])}
    
    
    
    #The constructor takes in the mode, digit 1 for bulk orders, and the digit 2 for buing/selling
    def __init__(self, mode, category):
        self.mode = int(mode)
        self.category = category
    
    #Function validates the user and only proceeds once successful. 
    def uservalidation(self):
        send("Please enter Name: ")
        self.name = receive()
        send("Please enter your password: ")
        self.password = receive()
        self.templist = self.modedlistofstuff()
        for key, value in Operation.Students.items():
            if self.name == key:
                if self.password==value[0]:
                    return True
                    #Will terminate the rest of the code and return True, allowing the user to proceed with the rest of the program
                else:
                    send("Incorrect Password\nTry Again? \n1.Yes, 2.No\n")
                    retry = int(receive())
                    if retry==2:
                        return False
                    else:
                        self.uservalidation()
        # Will prompt the user to create a new id and passowrd if none exists
        send("No such user, would you like to create one?\n1. Yes, 2. No\n")
        newchoice = int(receive())
        if newchoice==1:
            send("Please enter Email: ")
            email = receive()
            send("Please enter Phone: ")
            phone = receive()
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
            send(f"item: {key}, organizer: {value.human}, price you pay: {value.studentprice}, Expires in {value.duration} secs, contributions needed: {value.amount}, quantity of bulk: {value.stock}, participants: {value.humanlist}\n")
    
    #This function prints the additional info of the selected Item (choice)
    def info(self, choice):
        send(self.modedlistofstuff()[choice].info)
    
    #Allows the person to join the order, taking in as parameters the exact item he is joining and the amount of it he is purchasing
    def joinorder(self):
        send("Please enter item name: ")
        self.choice = receive()
        send(str(Operation.Inventory[self.choice].duration))
        send("Please enter item amount: ")
        self.amount = receive()
        if self.choice not in Operation.Inventory:
            send("Item not found\nWould you like to create an order?\n1. Yes, 2.No\n")
            self.newchoice = int(receive())
            if self.newchoice==1:
                self.addtoinventory(self.mode, self.category)
        else:    
            if self.uservalidation() and self.name not in Operation.Inventory[self.choice].humanlist:
                send("Order Joined\n")
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
                send("Order already joined\nWould You like to update the Order? \n1.Yes, 2.No\n")
                n = int(receive())
                if n==1:
                    Operation.Inventory[self.choice].amount-=int(self.amount)
                    if self.templist[self.choice].amount==0:
                        self.order(self.choice, self.name)
                        return True
                    
    #Adds new item to inventory after prompted for all the informations
    def addtoinventory(self, Mode, category):
        send("Please enter item name: ")
        self.choice = receive()
        self.category =category
        self.mode = Mode
        if self.uservalidation():
            send("Please enter price: ")
            self.studentprice = receive()
            send("Please enter duration until expiry: ")
            self.duration = receive()
            send("Please enter amount needed: ")
            self.amount = receive()
            send("Please enter stock: ")
            self.stock = receive()
            send("Please enter more information (if any): ")
            self.info = receive()
            Operation.Inventory[self.choice] = Item(self.choice,self.name, self.mode, self.category, self.studentprice, self.duration, self.amount, self.stock, self.info, [self.name])
            return True     
    def cancelorder(self, choice):
        send("ordercanceled\n")
        del self.modedlistofstuff()[choice]
    def order(self, choice, name):
        send(f"{choice} ordered!\n")
        history = open("history.txt", "a")
        history.write(f"Item: {choice}, Posted by {Operation.Inventory[choice].human}, Bought By {Operation.Inventory[choice].humanlist}\n")
        history.close
        del Operation.Inventory[choice]
        Operation.Students[name][-1].remove(choice)
    def buy(self):
        send("Please enter item name: ")
        self.choice = receive()
        if self.uservalidation():
            if self.choice in Operation.Inventory:
                with open("history.txt", "a") as history:
                    history.write(f"Item: {self.choice}, Posted by {Operation.Inventory[self.choice].human}, Bought By {self.name}\n")
                del Operation.Inventory[self.choice]  
                #Operation.Students[self.name][-1].remove(self.choice)
                send(f"{self.choice} purchased!\n")
    def categories():
        categors = []
        for key, value in Operation.Inventory.items():
            if value.category not in categors:
                categors.append(value.category)
        return categors
            
while True:
    for key, value in Operation.Inventory.items():
        (inventory(value.name, value.human, value.mode, value.category, value.studentprice, str(value.duration), value.stock, value.info, value.humanlist)).order(value.amount) 
    send(str(Operation.Students))
    send(str(Operation.Inventory))
    send("Welcome to the Yeshiva Marketplace\nPlease select the following options: \n 1. Group Order \n 2. Buy/Sell\n 3.Currency Converter\n")
    Mode = int(receive())
    if Mode==1 or Mode==2:    
        send(f"Please enter one of the following categories: {Operation.categories()}")
        category=  receive()
        program = Operation(Mode, category)
        program.printavailableinventory()
    if Mode==1:    
        send(("1. Join Order\n2. Create Order\n"))
        choice = int(receive())
        if choice == 1:
            program.joinorder()
            send(str(Operation.Inventory))
            program.printavailableinventory()
            send(str(Operation.Students))
        elif choice == 2:
            program.addtoinventory(Mode, category)
    elif Mode==2:
        choice = int(input("1. Post Item\n2.Buy Item\n"))
        if choice == 1:
            program.addtoinventory(Mode, category)
            send(str(Operation.Inventory))
            program.printavailableinventory()
            send(str(Operation.Students))
        elif choice == 2:
            program.buy()
    elif Mode ==3:
        send("Please select one: 1.USD 2.CAD 3.GBP\n")
        currency=float(receive())
        send("Select original currency: 1.SHKL 2.Other\n")
        convert_dir=float(receive())
        send("Value of original currency: ")
        my_value=float(receive())
        send(str(round(convert(currency, convert_dir, my_value)[1], 2)))
        send(convert(currency, convert_dir, my_value)[0])
    for key, value in Operation.Inventory.items():
        if value.duration == 0:
            del Operation.Inventory[key]
    catalogue.update_student(Operation.Students)   
#    for key, value in Operation.Inventory:
#        (inventory(value.name, value.human, value.mode, value.category, value.studentprice, value.duration, value.amount_left, value.info, value.humanlist)).order(value.amount()) 
             

name, human, mode, category, studentprice, duration, amount, stock, info, humanlist