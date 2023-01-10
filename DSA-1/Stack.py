#LAST IN FIRST OUT (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.check_empty():
            return "Stack is Empty Cannot do POP Operation"
        else:
            self.stack.pop()

    def Show(self):
        print(self.stack)




