def menu_driven():
    while True:
        print("1. Addition")
        print("2. Substraction")
        print("3. Division")
        print("4. mulip;ication")
        print("5. Exit")
        opt= int(input("enter your choice\t"))
        if opt ==1:
            n1=int(input("enter value1:"))
            n2=int(input("enter value2:"))
            res= n1+n2
            print("The result is:\t",res)
        elif opt==2:
            n1=int(input("enter value1:"))
            n2=int(input("enter value2:"))
            res= n1-n2
            print("The result is:\t",res)
        elif opt==3:
            n1=int(input("enter value1:"))
            n2=int(input("enter value2:"))
            res= n1/n2
            print("The result is:\t",res)
        elif opt==4:
            n1=int(input("enter value1:"))
            n2=int(input("enter value2:"))
            res= n1*n2
            print("The result is:\t",res)
        elif opt ==5:
            exit()
        else:
            print("\nWrong Selection\n")        
menu_driven()
    