import unittest
import linkedlist
import random

class testMyList(unittest.TestCase):

    def testSize(self):
        # add nodes, check size
        # remove nodes, check size
        l = linkedlist.linkedlist()
        assert l.size() == 0, "testSize(): linkedlist must be empty, it is {}".format(l.size())

        l.addNode(4)
        l.addNode(44)
        l.addNode(444)
        assert l.size() == 3, "testSize(): Size must be 3"
        

    def testEmpty(self):
        # make list, test if empty
        # add node, remove node, check if empty
        l = linkedlist.linkedlist()
        assert l.empty(), "testEmpty(): List.empty() returned false"
        l.addNode(23)
        assert not l.empty(), "testEmpty(): List is not empty"

    def testValueAt(self):
        # add values, push front, check value at
        l = linkedlist.linkedlist()
        l.addNode(48)
        l.addNode(83)
        l.addNode(29)
        assert l.value_at(0) == 48, "testValueAt(): value must be 48"

        l.push_front(99)
        assert l.value_at(0) == 99, "testValueAt(): new value must be 99"

    def testPushFront(self):
        # test push front and value at
        l = linkedlist.linkedlist()
        l.push_front(48)
        assert l.value_at(0) == 48, "testPushFront(): new value must be 48"

        l.push_front(83)
        assert l.value_at(0) == 83, "testPushFront(): new value must be 83"

        l.push_front(99)
        assert l.value_at(0) == 99, "testPushFront(): new value must be 99"

    def testPushBack(self):
        # check value at end
        # idx value == size - 1 
        l = linkedlist.linkedlist()
        for i in range(10):
            num = random.randint(1,10)
            l.push_back(num)
            assert l.value_at(i) == num, "testPushBack(): Push back working incorrectly"


    def testPopFront(self):
        # check value at root
        l = linkedlist.linkedlist()
        l.addNode(48)
        l.addNode(83)
        l.addNode(29)
        
        val = l.pop_front()
        assert val == 48 and l.size() == 2, "testPopFront(): Pop front failed"

    def testPopBack(self):
        l = linkedlist.linkedlist()
        l.addNode(48)
        l.addNode(83)
        l.addNode(29)
        
        val = l.pop_back()
        assert val == 29 and l.size() == 2, "testPopBack(): Pop front failed"



if __name__=="__main__":

    tester = testMyList()
    tester.testSize()
    tester.testEmpty()
    tester.testValueAt()
    tester.testPushFront()
    tester.testPushBack()
    tester.testPopFront()
    tester.testPopBack()

    print("Everything passed!")



