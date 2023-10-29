#create a petstore class where you have the details off pets available and their details.
#the class will have methods 
#-store a new pet details
#-search for a pet 
#-sell a pet
#-list all pet

#importing your petstore class, create a petstoremain file, where you will implement a menu 
# driven program for admin who will manage the store & user who will see the pets and buy pets.

class petstore:
    def __init__(self):
        self.pet=[]
    def petdetails(self):
        details={}
        type=input("Enter the species of pet:")
        age= str(input("Enter the age of pet:"))
        price=int(input("Enter the price of pet:"))
        details["Species"]=type
        details["Age"]=age
        details["Price"]=price
        print(details)
        self.pet.append(details)
        file=open("Petstore.csv","w+")
        file.write("\n"+str(details))
        file.close()
    def search(self):
        

petdet=petstore()
petdet.petdetails()




