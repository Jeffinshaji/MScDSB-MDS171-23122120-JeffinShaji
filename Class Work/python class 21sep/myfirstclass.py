#class MSCDSB:
#     def __init__(self):
#         #data members /properties/attributes
#         self.name="MSC DS B"
#         self.students=["A","B","C"]
#     def printstudents(self):
#         for student in self.students:
#             print(student)
# obj = MSCDSB()
# print(obj.name,obj.students)
# obj.printstudents()


class car:
    def __init__(self,mfg,mdl,yer):
        self.manufacture=mfg
        self.model=mdl
        self.year=yer
    def __str__(self):
        return self.manufacture

bmw = car("BMW","F Series",2020)
print(bmw.manufacture)
ferrari=car("Ferarri","A Series",2020)
print(ferrari.model)

Manufacture=input("Enter manufacture")
Model=input("Enter the model")
Year=input("Enter the year")
audi=car(Manufacture,Model,Year)
print(audi.manufacture,audi.model,audi.year)
