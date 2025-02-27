class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None


class Dequeue:
    def __init__(self, front):
        self.front = front

    def push_left(self, node):
        front_node = self.front
        node.next = front_node
        self.front = node

    def push_right(self, node):
        if not self.front:
            self.front = node
            return

        current_node = self.front
        while(current_node.next is not None):
            current_node = current_node.next
        current_node.next = node

    def pop_left(self):
        if self.front:
            self.front = self.front.next
        else:
            print('Empty dequeue.')

    def pop_right(self):
        if not self.front:
            raise IndexError('Dequeue is empty. ')

        if not self.front.next:
            self.front = None
            return
        
        current_node = self.front
        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def print_structure(self):
        if not self.front:
            raise IndexError('Dequeue is empty. ')

        current_node = self.front
        while(current_node is not None):
            print(current_node.data, end=' -> ')
            current_node = current_node.next    


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)

structure = Dequeue(first_node)
structure.push_right(second_node)
structure.pop_right()
structure.print_structure()
