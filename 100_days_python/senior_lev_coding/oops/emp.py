from typing import Any


class Employee:
    
    def __init__(self, name):
        self.name = name
    c = 0
    def __len__(self):
        for c in self.name:
            c = c+1
        return c

    def __str__(self):
        return f"The Employee name is {self.name} str"
    
    def __repr__(self):
        return f"Employee ('{self.name}') repr"

    def __call__(self):
        print("hello how are you python")