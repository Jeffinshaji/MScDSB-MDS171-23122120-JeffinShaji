# def addition(x,y):
#     return x+y
# def multiplication(x,y):
#     return x*y
# def division(x,y):
#     return(x/y)
# def substraction(x,y):
#     return(x-y)
# while True:
#     print("1.Addition")
#     print("2.Multiplication")
#     print("3.Divistion")
#     print("4.Substraction")
#     print("5.Exit")
#     choice=int(input("Select your choice"))
#     if choice==1:
#         x=int(input("Enter First Number:-"))
#         y=int(input("Enter Second Number:-"))
#         sum = addition(x,y)
#         print(sum)
#     if choice==2:
#         x=int(input("Enter First Number:-"))
#         y=int(input("Enter Second Number:-"))
#         sum = multiplication(x,y)
#         print(sum)
#     if choice==3:
#         x=int(input("Enter First Number:-"))
#         y=int(input("Enter Second Number:-"))
#         sum = division(x,y)
#         print(sum)
#     if choice==4:
#         x=int(input("Enter First Number:-"))
#         y=int(input("Enter Second Number:-"))
#         sum = substraction(x,y)
#         print(sum)
#     if choice==5:
#        exit()
        
with open("data.csv" , "r+")as file:
    head = file.readline()
    data = file.readlines()
    for dataa in data:
        print(dataa)


        