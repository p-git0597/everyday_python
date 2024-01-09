# class Vector2d:
#     def __init__(self, i, j)-> None:
#         self.i = i
#         self.j = j
#     def printVector2d(self):
#         print(f"{self.i}i + {self.j}j")    
    
# class Vector3d(Vector2d):
#     def __init__(self, i, j, k):    
#         self.k = k
#         super().__init__(i, j)
    
#     def printVector3d(self):
#         print(f"{self.i}i + {self.j}j + {self.k}k")
        
# v2 = Vector2d(1, 5)
# v3 = Vector3d(11 ,5 , 7)

# v2.printVector2d()
# v3.printVector3d()

# class Employee:
#     def __init__(self, salary, increment) -> None:
#         self.salary = salary
#         self.increment = increment
        
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * (1 + self.increment)
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self):
#         self.salary = self.salary * (1 + self.increment)
        
# emp = Employee(12000, 0.1)
# print(emp.salaryAfterIncrement)
# emp.salaryAfterIncrement = 15000

class Vector:
    def __init__(self, l1) -> None:
        self.dim = len(l1)
        self.data = l1
        
    def __add__(self, obj):
        myList = []
        for i in range(len(obj.data)):
            myList.append(obj.data[i] + self.data[i])
        return Vector(myList)
    def __mul__(self, obj):
        dot = 0
        for i in range(len(obj.data)):
            dot +=(obj.data[i] * self.data[i])
        return dot

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])

v3 = v1 + v2
v4 = v1*v2
print(v3.data)
print(v4)     
        