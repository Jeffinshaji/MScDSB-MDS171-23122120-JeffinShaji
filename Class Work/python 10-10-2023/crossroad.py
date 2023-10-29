# """def hey(name):
#     print("my name is "+name)
# def hello():
#     print("hello")
# value="jeffin shaji"
# hey(value )"""
# #argument passing to function
# #find number is odd or even
# number = input ("enter a number:")
# x=int(number)%2
# if x==0:
#     print("the number is even")
# else:
#     print("the number is odd")
# num1=(float(input("Enter Number 1:-")))
# num2=(float(input("Enter Number 2:-")))
# sum=num1+num2
# print(sum)
# num = int(input("enter a value:-"))
# sqrt= num **.5
# print(sqrt)
# import math
# num=int(input("enter a value:-"))
# num_sqrt=math.sqrt(num)
# print(num_sqrt)
# a=5
# b=6
# c=7
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**.5
# print(area)
# class student:
#     def __init__(self,sid,name,rollno):
#         self.studentID=sid,
#         self.studentName=name,
#         self.rollNo=rollno
# def student(name,mark1,mark2,mark3,total):
#     file=open("student.txt","w+")
#     file.write("name:"+str(name))
#     file.write("mark1:"+int(mark1))
#     file.write("mark2:"+int(mark2))
#     file.write("mark3:"+int(mark3))
#     file.close()
#     return True
# name=input("enter the name")
# mark1=input("enter the mark1")
# mark2=input("enter the mark2")
# mark3=input("enter the mark3")
# student(name,mark1,mark2,mark3)
n= int(input("enter a number"))
value = False
for i in range(2,(n//2)+1):
    if n%i==0:
        value = True
if value == True:
    print("not a prime")
else:
    print("prime")
    

            
