def ordNumber(self):
        ordCount += 1
        self.number = ordCount

class MyOrder:
    ordCount = 0
    
    def __init__(self, type, amount, number):
        self.type = input()
        self.amount = input()
        self.number = ordNumber()

    def __str__(self):
        return f"{self.name}  {self.age}"