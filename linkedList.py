class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp != None:
            print str(temp.data)+" ,",
            temp = temp.next

    def insert(self, data):
        if self.head == None:
            self.head = Node(data, self.head)
        else:
            node = Node(data)
            node.next = self.head

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.traverse()
