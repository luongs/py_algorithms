from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

    def __str__(self):
        return '{}'.format(self.data)

def inorder(root):
    if root:
        inorder(root.left)
        print "{}, ".format(root) ,
        inorder(root.right)

def preorder(root):
    if root:
        print "{}, ".format(root) ,
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print "{}, ".format(root),

def bfs(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        temp = queue.popleft()
        print "{}, ".format(temp),
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print "In Order: "
    inorder(root)
    print "\nPreOrder: "
    preorder(root)
    print "\nPostOrder: "
    postorder(root)
    print "\nBFS: "
    bfs(root)
