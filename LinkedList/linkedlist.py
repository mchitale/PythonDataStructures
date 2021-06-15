""" Create your own Linked List """

class Node(object):
    """docstring for Node"""
    def __init__(self, dataval = None):
        self.data = dataval
        self.next = None


class linkedlist(object):
    """docstring for linkedlist"""
    def __init__(self, data=None):
        self.root = Node(data)
        self.count = 1 if data else 0

    def addNode(self,val):
        
        if self.count == 0:
            self.root.data = val
            self.count+=1
            return
        
        if self.count == 1:
            newNode = Node(val)
            self.root.next = newNode
            self.count+=1
            return

        runner = self.root
        while runner.next != None:
            runner = runner.next
        newNode = Node(val)
        runner.next = newNode
        self.count+=1
        return

    def size(self):
        return self.count

    








