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
        while head is not None:
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
        if not isinstance(item, Node):
            item = Node(item)
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
        self.items -= 1
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

class Queue_Linked_List:
    '''
    Linked List Queue Implementation
    '''
    def __init__(self):
        self.head = None
        self.back = self.head
    def enqueue(self, element):
        if not isinstance(element, Node):
            element = Node(element)
        if self.back is None:
            self.head = element
            self.back = self.head
        self.back.next = element
        self.back = self.back.next
    def dequeue(self):
        if self.head is None:
            return None
        to_dequeue = self.head
        self.head = self.head.next
        return to_dequeue
    def __contains__(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        head = self.head
        while head is not None:
            if head.data == item.data:
                return True
            head = head.next
        return False
    def is_empty(self):
        return self.head is None
    def __len__(self):
        counter = 0
        head = self.head
        while head is not None:
            head = head.next
            counter += 1
        return counter

class Queue_Circular_Buffer:
    '''
    Circular Buffer, not optimized for performance
    '''
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0
    def __len__(self):
        relative_length = self.tail - self.head
        if relative_length < 0:
            relative_length *= - 1
        return relative_length + 1
    def enqueue(self, item):
        if len(self) == self.size:
            raise Exception('Circular Buffer is going to Overwrite, aborted')
        self.array[(self.tail)% self.size] = item
        self.tail += 1
    def dequeue(self):
        to_dequeue = self.array[self.head % self.size]
        self.array[self.head % self.size] = None
        self.head += 1
        return to_dequeue
    def __contains__(self, item):
        l = len(self)
        for i in range(l):
            if self.array[(self.head + i) % self.size] == item:
                return True
        return False
    def is_empty(self):
        return self.array[self.head % self.size] is None
