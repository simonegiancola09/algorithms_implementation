from turtle import right
from node_stack_and_queue import Node, Queue_Linked_List
class BinaryHeap:
    '''
    Binary Heap class implemented with a list. Heapsort function in sorting.py script. 
    '''
    def __init__(self):
        self.tree = []
        # parent of node k at k // 2
        # children of node k at 2k, 2k + 1
        # parent bigger than children
    def __len__(self):
        return len(self.tree)
    def parent(self, k):
        return k // 2
    def children(self, k):
        if k > len(self) // 2:
            raise Exception('Value of index is too high, no children detected')
        return 2 * k, 2 * k + 1
    def insert(self, el):
        # append to end
        self.tree.append(el)
        # swim up
        self.swim_up()
    def swim_up(self):
        n = len(self) - 1
        # get last_info
        last = self.tree[n]
        last_ind = n
        while last > self.tree[self.parent(last_ind)]:
            # swim up until it is possible
            # get parent
            parent_ind = self.parent(last_ind)
            # exchange
            self.tree[last_ind], self.tree[parent_ind] = self.tree[parent_ind], self.tree[last_ind]
            # substitute
            last_ind = self.parent(last_ind)
            last = self.tree[last_ind]
    def remove_max(self):
        # exchange
        self.tree[0], self.tree[-1] = self.tree[-1], self.tree[0]
        # save max_val
        max_val = self.tree[-1]
        # remove max_val from tree
        self.tree = self.tree[: -1]
        self.sink_down()
        return max_val
    def sink_down(self):
        first = self.tree[0]
        first_ind = 0

        while (first <= self.tree[self.children(first_ind)[0]] or first <= self.tree[self.children(first_ind)[1]]):
            right = self.tree[self.children(first_ind)[0]]
            left = self.tree[self.children(first_ind)[0]]
            # exchange with larger children
            if left > right:
                # exchange
                self.tree[first], self.tree[self.children(first_ind)][1] = self.tree[self.children(first_ind)][1], self.tree[first_ind]
                # substitute
                first = left
                first_ind = self.children(first_ind)[1]
            if left > right:
                # exchange
                self.tree[first], self.tree[self.children(first_ind)][0] = self.tree[self.children(first_ind)][0], self.tree[first_ind]
                # substitute
                first = right
                first_ind = self.children(first_ind)[0]

class BTNode:
    def __init__(self, key, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node):
        if not isinstance(node, BTNode):
            raise Exception('Insert a valid element of Node instance')
        parent = None
        to_compare = self.root
        while to_compare != None:
            parent = to_compare
            if to_compare.key < node.key:
                to_compare = to_compare.left
            elif to_compare.key > node.key:
                to_compare = to_compare.right
            else:
                raise Exception('Node key already present')
        node.parent = parent

        if parent == None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        self.size += 1        
                
    def get(self, key):
        node = self.root
        while node != None:
            if key < node.key:
                # go left
                node = node.left
            elif key > node.key:
                # go right
                node = node.right
            else:
                # hit search
                return node.val
        # nothing found
        return None

    def get_min(self):
        node = self.root
        while node.left != None:
            node = node.left
        return node.key
    def get_max(self):
        node = self.root
        while node.right != None:
            node = node.right
    
    def get_floor(self, key):
        # call inside function which finds the floor iteratively
        node = self.root

        def inside_floor(key, node):
            # find key starting from node recursively
            if node is None:
                # base case
                return None
            if node.key > key:
                # go left as node is bigger
                return inside_floor(key, node.left)
            if node.key == key:
                # search hit
                return node
            if node.key < key:
                # smaller, so go right and compare rightmost value with current
                floor_right = inside_floor(key, node.right)
                if (floor_right is None or floor_right.key < node.key):
                    # not a floor found or too small floor
                    return node
                else:
                    # rightmost floor is the correct one
                    return floor_right
        floor = inside_floor(key, node)
        return floor


    def get_ceil(self, key):
        # call inside function which finds the floor iteratively
        node = self.root

        def inside_ceil(key, node):
            # find key starting from node recursively
            if node is None:
                # base case
                return None
            if node.key < key:
                # go right as node is smaller
                return inside_ceil(key, node.right)
            if node.key == key:
                # search hit
                return node
            if node.key > key:
                # bigger, so go left and compare leftmost value with current
                ceil_left = inside_ceil(key, node.left)
                if (ceil_left is None or ceil_left.key > node.key):
                    # not a ceil found or too big ceil
                    return node
                else:
                    # leftmost floor is the correct one
                    return ceil_left
        ceil = inside_ceil(key, node)
        return ceil
    def size(self):
        node = self.root
        # base case is when left and right are none
        if node is None:
            return 0
        # other case is sum of children + 1
        return 1 + node.left.size() + node.right.size()

    def rank(self, key):
        ''' Counts number of keys less than the key presented'''
        node = self.root

        def inside_rank(key, node):
            # recursvive
            # base case
            if node == None:
                return 0
            if key < node.key:
                # evaluate left rank
                return inside_rank(key, node.left)
            elif key > node.key:
                # evaluate all directinos rank
                return 1 + node.left.size() + inside_rank(key, node.right)
            else:
                # evaluate only size of all that is to the left as hit search
                return node.left.size()
        # never gets here
        return inside_rank(key, node)
    def select_node(self, rank):
        if rank < 0:
            return None
        elif rank > self.size():
            return None
        def inside_select_node(node, rank):
            if node == None:
                return None
            s = node.left.size()
            if s > rank:
                # go left
                inside_select_node(node.left, rank)
            elif s < rank:
                # go right
                inside_select_node(node.right, rank - s - 1)
            else:
                return node
        node = self.root

        node = inside_select_node(node, rank)
        return node.key
    def inorder_traversal(self):
        queue = Queue_Linked_List()
        def inner_inorder_traversal(node, queue):
            if node == None:
                return None
            queue.enqueue(inner_inorder_traversal(node.left, queue))
            queue.enqueue(node.key)
            queue.enqueue(inner_inorder_traversal(node.right, queue))
            return queue
        queue = inner_inorder_traversal(self.root, queue)
        return queue
    
    def delete(self):
        pass
    # missing

class RedBlackNode:
    def __init__(self, key, color, value=None,
                left=None, parent=None, right=None):
        self.key = key
        # color is the color of the link parent - node
        self.color = color
        self.value = value
        self.left = left
        self.parent = parent
        self.right = right
    def is_red(self):
        return self.color.upper() == 'R'

class RedBlackTree:
    # assume left leaning red black tree
    # this is just a convention used in class
    def __init__(self):
        self.root = None
        self.size = 0
    
    # elementary operations

    def rotate_left(self, node):
        '''
        Orient right leaning red link to the left
        '''
        assert node.right.is_red()

        x = node.right
        node.right = x.left

        x.left = node

        x.color = node.color
        node.color = 'R'
        # need to return to make it operative in insert function
        return x
    def rotate_right(self, node):
        '''
        Orient double left leaning red tree to the right temporarily
        '''
        assert node.left.is_red()
        assert node.left.left.is_red()
        # the double red children
        child = node.left
        grandchild = node.left.left

        # now to the left of node we have the child material
        node.left = child.right
        # exchange parenthood
        child.parent = node.parent
        node.parent = child
        # update colors, now double red link at the top
        child.color = 'B'
        node.color = 'R'
        # return the head
        return child

    def color_split(self, node):
        '''
        Change a double red node into a parent red and children black structure
        '''
        assert node.is_red() == 0
        assert(node.left.is_red()) == 1
        assert(node.right.is_red()) == 1
        node.color = 'R'
        node.left.color = 'B'
        node.right.color = 'B'

    def insert(self, key, val):
        def inner_insert(head, key, val):
            if head == None:
                return RedBlackNode(key, 'R', val)
            if key < head.key:
                head.left = inner_insert(head.left, key, val)
            elif key > head.key:
                head.right = inner_insert(head.right, key, val)
            else:
                head.val = val
            # now the three cases

            if (not head.left.is_red() and head.right.is_red()):
                head = self.rotate_left(head)
            if (head.left.is_red() and head.left.left.is_red()):
                head = self.rotate_right(head)
            if (head.left.is_red and head.right.is_red()):
                self.flipcolors(head)
            return head


        
        

        






    


            


