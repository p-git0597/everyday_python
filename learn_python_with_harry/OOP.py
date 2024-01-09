# class Enployee:
#     name = 'Harry'
#     marks = 34
    
# harry =Enployee()
# print(harry.name) # Output : Harry

class Employee:
    center = "NotKnown" # class attributes
    def __init__(self, name, marks,center):
        self.name = name        # instance arrtibute
        self.marks = marks      # instance arrtibute
        self.center = center    # instance arrtibute
    
    def printObj(self):
        print(f"The name is {self.name}")
        print(f"The marks is {self.marks}")
        print(f"The center is {self.center}")
        
harry = Employee("Puttar", 45, "Delhi")
rohan = Employee("Ram", 34, "Punjab")
harry.printObj()
rohan.printObj()