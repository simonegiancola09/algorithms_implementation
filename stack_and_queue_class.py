class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_Linked_List:
    '''
    Initiates with an empty stack
    basic operations in O(1)
    length and search in O(n)
    '''
    def __init__(self):
        self.head = None
    def push(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        node.next = self.head
        self.head = node
    def pop(self):
        if self.head is None:
            return None
        to_pop = self.head
        self.head = self.head.next
        return to_pop
    def is_empty(self):
        return self.head is None
    def __contains__(self, item):
        head = self.head
        while head != None:
            if head.data == item:
                return True
            head = head.next
        return False
    def __len__(self):
        counter = 0
        head = self.head
        while head != None:
            head = head.next
            counter += 1
        return counter


class Stack_Array_Resizing:
    '''
    Uses efficient array resizing
    double size when array is full, halve it when array is one quarter full to get O(1) amortized constant
    '''
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.items = 0
    def push(self, item):
        if self.items == self.capacity:
            self.change_size(2)
        self.array[self.items] = item
        self.items += 1
    def pop(self):
        if self.items == 0:
            return None
        if self.items - 1 == self.capacity // 4:
            self.change_size(0.5)
        element = self.array[self.items]
        self.array[self.items] = None
        self.i
        return element
    def change_size(self, factor):
        self.size *= factor
    def is_empty(self):
        return self.items == 0
    def __contains__(self, element):
        for i in range(self.items):
            if self.array[i] == element:
                return True
        return False
    def __len__(self):
        return self.items

class 

b = Node('ciao')
a = Stack()
a.push('second')
a.push(b)
a.pop()
a.pop()