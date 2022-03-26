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




        

