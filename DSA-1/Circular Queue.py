# Last element is conected to first element
# The circular queue solves the major limitation of the normal queue . In a normal queue,
# after a bit of insertion and deletion, there will be non-usable empty space


class Circular_Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*self.size
        # as initially queue is empty both head and tail will be same and that is equal to -1
        self.front = self.tail = -1

    def Enqueue(self, item):
        if ((self.tail+1) % self.size == self.front):
            print("Circular Queue is Full")
        elif self.front == -1:
            # empty queue case
            self.front = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail+1) % self.size
            self.queue[self.tail] = item

    def Dequeue(self):
        # empty queue case
        if self.front == -1:
            return "Circular queue is Empty"
        # condition where only one element is present i queue where tail and front is 0
        elif self.front == self.tail:
            temp = self.queue[self.front]
            self.tail = -1
            self.front = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return temp

    def Printqueue(self):
        if self.front == -1:
            return "Queue is Empty"
        if self.tail >= self.front:
            print("Printing Circular Queue : ")
            for i in range(self.front, self.tail+1):
                print(self.queue[i], end="")
            print()
        else:
            print("Printing Circular Queue : ")

            for i in range(self.front, self.size):
                print(self.queue[i], end="")
            for i in range(0, self.tail+1):
                print(self.queue[i], end="")
            print()


obj = Circular_Queue(4)
obj.Enqueue(2)
obj.Enqueue(3)
obj.Enqueue(4)
obj.Printqueue()
obj.Dequeue()
obj.Printqueue()







        

        




        


        





