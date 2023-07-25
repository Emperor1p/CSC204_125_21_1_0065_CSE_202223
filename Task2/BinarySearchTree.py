class BinarySearchTree:
    def __init__(self, key= None):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, key):
        if key == self.key:  # if the particular has existed before then we need to return it, no need of adding again
            return
        if key < self.key:
            if self.lchild:
                self.lchild.insert(key)  # when node < parent node it will go to left of the parent node
            else:
                self.lchild = BinarySearchTree(key)
        else:
            if self.rchild:
                self.rchild.insert(key)  # when node > parent node it will go to right of the parent node
            else:
                self.rchild = BinarySearchTree(key)

    def in_order(self):  # this is the mode of checking the element
        elements = []

        # visit lchild mode
        if self.lchild:  # go to leaf, traverse from the left first
            elements += self.lchild.in_order()

        # visit base node
        elements.append(self.key)  # add the element to the previous set of the node visited

        # visit rchild tree
        if self.rchild:  # go to leaf, traverse from the left first
            elements += self.rchild.in_order()  # add the element to the previous set of the node visited

        return elements

    def search(self, val):
        if self.key == val:
            return True

        if val < self.key:
            if self.lchild:
                return self.lchild.search(val)
            else:
                return False

        if val > self.key:
            if self.rchild:
                return self.rchild.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTree(elements[0])  # the root element should be the first element in the list i.e. zero index

    for i in range(1, len(elements)):
        root.insert(elements[i])
    return root


if __name__ == '__main__':
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    numbers = build_tree(data_list)
    print(numbers.in_order())
    print(numbers.search(1))  # this is to check if a particular number exists
