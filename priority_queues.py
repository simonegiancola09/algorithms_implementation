from node_stack_and_queue import Node
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
    


            


