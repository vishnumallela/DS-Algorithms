class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertNodeAfter(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            print("Node should not be null")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        iterator = self.head
        while (iterator.next):
            iterator = iterator.next
        iterator.next = new_node

    def search(self, key):
        iterator = self.head
        while iterator is not None:
            if iterator.data == key:
                return True
            iterator = iterator.next

        return False

    def DeleteNode(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def sortList(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next

        values = sorted(values)

        current = self.head
        for val in values:
            current.data = val
            current = current.next




        



        
            





        