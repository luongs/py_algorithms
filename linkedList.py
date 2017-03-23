class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "{}".format(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp != None:
            print str(temp)+" ,",
            temp = temp.next

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def pop(self):
        res = None
        if self.head == None:
            raise KeyError('Cannot pop empty stack')
        else:
            res = self.head
            self.head = self.head.next
        return res

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    ll.push(2)
    ll.push(3)

    print str(ll.pop())
    #second = Node(2)
    #third = Node(3)
    #ll.head.next = second
    #second.next = third


    ll.traverse()
