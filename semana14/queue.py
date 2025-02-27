class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self, front):
        self.front = front

    def print_structure(self):
        current_node = self.front
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def dequeue(self):
        if (self.front):
            self.front = self.front.next

    def queue(self, node):
        current_node = self.front
        while(current_node.next is not None):
            current_node = current_node.next
        current_node.next = node

firts_node = Node('1')
second_node = Node('2')
third_node = Node('3')



firts_node.next = second_node
second_node.next = third_node



structure = Queue(firts_node)

structure.print_structure()

structure.dequeue()

structure.print_structure()