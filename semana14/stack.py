class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, top):
        self.top = top
        

    def push(self, node):
        if not self.top:
            self.top = node
            return
        
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise IndexError("Empty stack. ")
        else:
            self.top = self.top.next

    def print_stack(self):
        if not self.top:
            raise IndexError("Empty stack")
        
        current_node = self.top
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

first_node = Node(1)
second_node = Node(2)


structure = Stack(first_node)
structure.print_stack()
print('---------')
structure.push(second_node)
structure.print_stack()
print('---------')
structure.pop()
structure.print_stack()
print('---------')

