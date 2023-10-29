#create a class rseturant, that accepts 
#item name & qty as input i
#inside your class you are having the item and its cost(unit price) as a dictionary
#create  afunction calculate total cost 
#that print the item name qty and total cost

class resturant:
    def __init__(self,itemname,qty):
        self.itemname=itemname
        self.qty=qty
        self.menuItems={
            "Rice":30,
            "Chicken":100,
            "Dal":40,
            "Chapathi":15
        }

    def total(self):
        print("Total cost of the oredr")
        print("Item\t:",self.itemname)
        print("Quantity\t:",self.qty)
        global total
        total = self.qty*self.menuItems[self.itemname]
        print("Total\t:",total)
tot=0    
for i in range(3):
    itemname=input("enter the item")
    qty=int(input("enter the quantity"))
    order=resturant(itemname,qty)
    order.total()
    tot=tot+total
    print("total price:",tot)
        
        

