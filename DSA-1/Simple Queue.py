#FIRST IN FIRST OUT
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def Enqueue(self, item):
        self.queue.append(item)

    def Dequeue(self):
        if self.is_empty:
            return "Cannot Dequeue Empty Queue"
        else:
            # popping first element
            self.queue.pop(0)

    def Show(self):
        print(self.queue)

        