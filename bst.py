class Node:
    """
    Single node for BST
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        return "{}, ".format(self.key)

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.key < node.key:     # eg: root=> 1, node=>10
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:   # eg: root => 10, node => 1
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root),
        inorder(root.right)

def search(root, val):
    if root is None:
        print "{} NOT in BST".format(val)
    elif root.key == val:
        print "{} in BST".format(val)
    else:
        if root.key > val:
            search(root.left, val)
        else:   # root.key < val
            search(root.right, val)

if __name__ == '__main__':
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(70))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(60))
    insert(r, Node(80))

    print "In order traversal"
    inorder(r)
    print "\nSearching for 60 (exists)"
    search(r, 60)
    print "\nSearching for 100 (missing)"
    search(r, 100)
