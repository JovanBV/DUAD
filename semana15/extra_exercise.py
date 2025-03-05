class Node:
    data: int
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


def swap_nodes(node_1, node_2):
    first_data = node_1.data
    node_1.data = node_2.data
    node_2.data = first_data


def sort_linked_list(node):
    current_node = node
    next_node = current_node.next
    
    while current_node.next is not None:
        print(current_node.data)
        if current_node.data > next_node.data:
            swap_nodes(current_node, next_node)
        current_node = current_node.next
        sort_linked_list(node.next)


second_node = Node(2)
firts_node = Node(1)
third_node = Node(3)
fourth_node = Node(4)

structure = Queue(second_node)
structure.queue(firts_node)
structure.queue(fourth_node)
structure.queue(third_node)


structure.print_structure()
print('------------------------')
sort_linked_list(second_node)
print('------------------------')
structure.print_structure()

