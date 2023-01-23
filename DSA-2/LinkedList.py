class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)

#linking

linked_list.head.next = second
second.next = third

#printing list

while linked_list.head!=None:
    print(linked_list.head.data)
    linked_list.head = linked_list.head.next