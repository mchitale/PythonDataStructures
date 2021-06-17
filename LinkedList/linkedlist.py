""" Create your own Linked List """

class Node(object):
    """
    Base datatype for a linkedlist node
    containing the data and a pointer to the
    next node
    """
    def __init__(self, dataval = None):
        self.data = dataval
        self.next = None


class linkedlist(object):
    """
    Usage:
    >> import linkedlist
    
    >> l = linkedlist.linkedlist()
    >> l.addNode(93)
    >> l.addNode(39)
    >> l.addNode(30)
    >> l.size()
    
    3

    >> l.value_at(2)

    30

    >> l.push_front(27)
    >> l.value_at(0)

    27

    >> 
    """
    def __init__(self, data=None):
        self.root = Node(data)
        self.count = 1 if data else 0

    def __getitem__(self, idx):
        runner = self.root
        for i in range(idx):
            runner = runner.next

        return runner.data

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

    def empty(self):
        return self.count == 0

    def value_at(self,idx):
        if idx >= self.count:
            raise IndexError("Index exceeds number of items in list")

        runner = self.root
        for i in range(idx):
            runner = runner.next

        return runner.data

    def push_front(self,val):

        # Handle empty list edge case
        if self.empty():
            self.root = Node(val)
            self.count+=1
            return

        newRoot = Node(val)
        newRoot.next = self.root
        self.root = newRoot
        self.count+=1


    def pop_front(self):

        ans = self.root.data
        self.root = self.root.next
        self.count-=1
        return ans


    def front(self):
        return self.root.data

    def push_back(self, val):
        self.addNode(val)

    def pop_back(self):
        if self.count == 0:
            raise RuntimeError("List is empty")
        
        if self.count == 1:
            ans = self.root.data
            self.root = None
            self.count = 0
            return ans

        runner = self.root
        while runner.next != None:
            prevRunner = runner
            runner = runner.next
        ans = runner.data
        prevRunner.next = None
        self.count-=1
        return ans

    def erase(self, idx):
        runner = self.root

        for i in range(idx):
            prevRunner = runner
            runner = runner.next

        prevRunner.next = runner.next
        self.count -= 1
        return

    def removeValue(self,value):
        runner = self.root

        while runner.data != val:
            prevRunner = runner
            runner = runner.next

        prevRunner.next = runner.next
        self.count -= 1
        return

    def value_n_from_end(self,idx):
        if (self.size() - idx) < 0:
            raise IndexError("list isn't long enough to perform this operation")

        #runner_n_from_end = self.root
        runner = self.root
        for i in range((self.size()-idx)):
            prevRunner = runner
            runner = runner.next

        prevRunner.next = runner.next
        self.count -= 1
        return




