class Deque:
    def __init__(self):
        self.arr =[]
    def is_empty(self):
        return len(self.arr)==0
    def addFront(self,item):
         self.arr.append(item)
         return self.arr
    def addRear(self,item):
        self.arr.insert(0,item)
        return self.arr
    def removeFront(self):
        self.arr.pop()
        return self.arr
    def removeRear(self):
        self.arr.pop(0)
        return self.arr

x = Deque()
print(x.is_empty())
print(x.addFront(2))
print(x.addRear(1))
print(x.addRear(3))
print(x.removeFront())
print(x.removeRear())

