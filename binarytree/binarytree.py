class BinaryTree:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    class BinaryTree:

        def __init__(self):
            self.root = None

    def add(self, value):
        if self.key is None:
            self.key = value
            return
        if self.key == value:
            return
        if value < self.key:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryTree(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryTree(value)

    def check(self, value):
        if self.key is None:
            self.key = value

    def search(self, value):
        if self.key == value:
            print("The node is present")
            return
        if value < self.key:
            if self.left:
                self.left.search(value)
            else:
                print("The node is empty in the tree!")
        else:
            if self.right:
                self.right.search(value)
            else:
                print ("The node is empty in the tree!")
