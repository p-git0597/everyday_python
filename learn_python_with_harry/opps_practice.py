# class Programmer:
    
#     def __init__(self, name, language):
#         self.name = name
#         self.language = language
        

# harry = Programmer("rohan", "hindi")
# rohan = Programmer("sham", "marathi")

# print(rohan.name)
# print(harry.name)


# import math
# class Calculator:
#     def __init__(self, number):
#         self.number = number
    
#     def sqrt(self):
#         return math.sqrt(self.number)
    
#     def square(self):
#         return self.number * self.number
    
#     def cube(self):
#         return self.number * self.number * self.number
    
# cal = Calculator(5)
# print(cal.square())
# print(cal.cube())


# class Myclass:
#     a = 9
    
# obj = Myclass()
# print(obj.a)
# obj.a = 0 # I am setting instance attribute
# print(obj.a)
# print(Myclass.a)


class Train:
    
    def __init__(self) -> None:
        self.seats = 100
        self.fare = 300
    
    def bookTicket(self):
        self.seats -= 1
    
    def getStatus(self):
        print(self.seats)
    
    def getFare(self):
        print(self.fare)
        
        
tr = Train()
tr.getFare()
tr.getStatus()
tr.bookTicket()
tr.getStatus()

