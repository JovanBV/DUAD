class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if not self.data:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def in_order_print(root):
    if root is None:
        return
    else:
        in_order_print(root.left)
        print(root.data, end=' -> ')
        in_order_print(root.right)

def pre_order_print(root):
    if root is None:
        return
    else:
        print(root.data, end=' -> ')
        pre_order_print(root.left)
        pre_order_print(root.right)
        

def post_order_print(root):
    if root is None:
        return
    else:
        print(root.data, end=' -> ')
        post_order_print(root.right)
        post_order_print(root.left)

if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    print('In order print:')
    in_order_print(root)
    print('\nPre order print:')
    pre_order_print(root)
    print('\nPost order print:')
    post_order_print(root)