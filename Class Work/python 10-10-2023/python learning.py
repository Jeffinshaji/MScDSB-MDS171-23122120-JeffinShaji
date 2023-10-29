# create a sport mart class where you will have inventory /shelf of item and order of coustmers.
# create a csv file which will there inventory details and order details with the help of file handling technique in python. 
# read the file and create  an object for trinity store and populate the inventory item and orders for the trinity object.
# to make sure that you have add the item from your file used the display method to show your inventory and oredr history.
class sportmart:
    def __init__(self):
        self.inventory={} # list of item
        self.order={} # customer order
    def addorder(self,OrderID,ProductName,Quantity,Price,Total):
        temp={"orderID":OrderID,"productname":ProductName,"quantity":Quantity,"price":Price,"total":Total}
        self.order[OrderID]=temp
    def inventory(self,ProductID ,ProductName ,Quantity,Price,Total):
        tempe={"ProductID":ProductID,"productname":ProductName,"quantity":Quantity,"price":Price,"total":Total}
        self.inventory[ProductID]=tempe
    def displayorder(self):
        print(self.order)
    def displayinventory(self):
        print(self.inventory)
trinity = sportmart()
# Read orders from a CSV file
orders=open("smorder .csv","r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp=item.strip().split(',')
    trinity.addorder(temp[0],temp[1],temp[2],temp[3],temp[4])
inventory=open("smproductID.csv","r")
inventory_header = inventory.readline()
inventory_inventory= inventory.readlines()
for item in inventory_inventory:
    tempe=item.strip().split(',')
    trinity.addorder(tempe[0],tempe[1],tempe[2],tempe[3],tempe[4])

while True:
    print("\n Select the option")
    print("1.New Order")
    print("2.Update Inventory")
    print("3.Exit")
    choice = int(input("\nEnter your choice"))
    
    if choice==1:
        OrderID=input("Enter the order id:-")
        ProductName=input("Enter the product name:-")
        Quantity=input("Enter the quantity:-")
        Price=input("Enter the price:-")
        Total=Quantity*Price
        trinity.addorder(OrderID,ProductName,Quantity,Price,Total)
    elif choice==2:
        ProductID=input("Enter the product ID:-")
        productname=input("Enter the product name:-")
        quantity=input("Enter the quantity:-")
        price=input("Enter the price:-")
        total=quantity*price
        trinity.inventory(ProductID,productname,quantity,price,total)
    elif choice==3:
        exit()
    else:
        print("Enter the correct option")


    