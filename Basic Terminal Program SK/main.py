import time
import datetime
import threading

class Item():
    def __init__(self, name, human, mode, category, studentprice, duration, amount, stock, info):
        print("New Item created")
        self.name = name
        self.category = category
        self.studentprice = studentprice
        self.duration = duration
        self.amount = amount
        self.stock = stock
        self.info = info
        self.mode = mode
        self.human = human
        self.thread = threading.Thread(target=self.countdown)
        self.thread.start
    def countdown(self):
        while self.duration>0:
            time.sleep(1)
            self.duration -=1
        

#while Inventory["Pizza"].duration >0:
#    print(Inventory["Pizza"].duration)
 
class Operation:
    Inventory = {"Pizza" : Item("Pizza", "Shloimy", 1, "food", "$2", 500, 1, 9, "Tel Aviv"),}
    def __init__(self, mode):
        self.mode = int(mode)
    def modedlistofstuff(self):
        self.modedinventory = {}
        for key, value in Operation.Inventory.items():
            if value.mode == self.mode:
                self.modedinventory[key] = value
        return self.modedinventory
    def printavailableinventory(self):
        inventory = self.modedlistofstuff()
        for key, value in inventory.items():  
            print(f"item: {key}, organizer: {value.human}, price you pay: {value.studentprice}, Expires in {value.duration} secs, contributions needed: {value.amount}, quantity of bulk: {value.stock}", "\n")
    def inventoryactions(self):
        choice = input("1. Join Order\n2. Create Order")
        if choice == 1:
            self.joinorder()
    def info(self, choice):
        print(self.listofstuff()[choice].info)
    def joinorder(self, choice):
                self.confirmorder()
    def confirmorder(self):
        print("Ordered")
    def addtoinventory(self):
        name, human, mode, category, studentprice, duration, amount, stock, info =input("").split(", ")
        Operation.Inventory[name] = Item(name, human, mode, category, studentprice, duration, amount, stock, info)
    def cancelorder(self):
        print("ordercanceled")
        
 
    

Mode = input("Please select the following options \n 1. Group Order \n 2. Buy/Sell\n")
program = Operation(Mode)
program.printavailableinventory()
program.inventoryactions()
             

