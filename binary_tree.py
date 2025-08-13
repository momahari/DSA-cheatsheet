
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    """
    Warning : Binary Tree is like a set so it wouldn't have a dublicate elements
    """

    def insert(self, data):
        if self.data == data:
            raise Exception("this value is already inserted in the tree")

        if self.data < data:
            if self.left :
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right :
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        ...

    def pre_order_traversal(self):
        ...

    def post_order_traversal(self):
        ...


if __name__ == "__main__":