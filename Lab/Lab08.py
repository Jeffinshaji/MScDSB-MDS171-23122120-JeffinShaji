class stack:
    def __init__(self):
        self.stlist=[]

    def push_item(self):
        value=input("enter the value to be added")
        self.stlist.append(value)
        return self.stlist
        
    def pop_item(self):
        self.stlist.pop()
        print("item removed")
        
    def stackitem(self):
        print("items are")
        print(self.stlist)
     
    def size(self):
        print("Size is:",len(self.stlist))

    def topitem(self):
        print("top element is",self.stlist[len(self.stlist)-1])

    def empty(self):
        if len(self.stlist)==0:
            print("the stack is empty")
        else:
            print("the stack is not empyt")
new_stack=stack()
while True:
    print("1 for push item")
    print("2 for pop item")
    print("3 for print item")
    print("4 for check size of stack")
    print("5 for view top item ")
    print("6 check stack is empty")
    print("7 exit")
    choice=int(input("enter your choice"))
    if choice==1:
        new_stack.push_item()
    elif choice==2:
        new_stack.pop_item()
    elif choice==3:
        new_stack.stackitem()
    elif choice==4:
        new_stack.size()
    elif choice==5:
        new_stack.topitem()
    elif choice==6:
        new_stack.empty()
    elif choice==7:
        exit()
    else:
        print("correct option")

