from myList import myList
import random
import unittest


class testMyList(unittest.TestCase):
    
    def testSize(self):
        
        # size function of the array should return the correct size
        arr = myList(int)

        for i in range(3):
            num = random.randint(0,100)
            arr.push_back(num)

        assert arr.size() == 3, "Int array size must be 3"

        arr = myList(float)
        for i in range(5):
            num = random.uniform(0.0,100.0)
            arr.push_back(num)

        assert arr.size() == 5, "Float array size must be 5"


    def testPushback(self):
        
        arr = myList(float)

        for i in range(5):
            num = random.uniform(0.0,100.0)
            arr.push_back(num)
            assert arr[-1] == num, "push_back must append at the end"
        
        assert arr.size() == 5


    def testAt(self):
        arr = myList(int)
        for i in range(10):
            num = random.randint(0,20)
            arr.push_back(num)
            assert arr.at(i) == num, "Wrong number found at index {}".format(i)

        with self.assertRaises(IndexError):
            arr.at(20)

    def testInsert(self):
        arr = myList(int)
        
        for i in range(10):
            arr.push_back(i+1)

        arr.insert(4,74)
        assert arr[4] == 74, "insert failed"

        with self.assertRaises(IndexError):
            arr.insert(33,100)

        
    def testPop(self):
        arr = myList(int)

        with self.assertRaises(RuntimeError):
            elem = arr.pop()
        
        for i in range(10):
            arr.push_back(i+1)

        elem = arr.pop()
        assert elem == 1, "Popped element must be equal to 1"
        assert arr.size() == 9, "Array size after popping must be 9"

    def testDelete(self):
        
        arr = myList(int)
        
        for i in range(10):
            arr.push_back(i+1)

        numToDelete = arr[random.randint(1,10)]
        del arr[numToDelete]
        assert arr.size() == 9, "New array size must be 9"


    def testFind(self):
        arr = myList(int)
        
        with self.assertRaises(RuntimeError):
            arr.find(1)

        for i in range(10):
            arr.push_back(i+1)

        assert arr.find(7) == 6, "Find failed"

        assert arr.find(12) == "Item Not Found"
        

if __name__ == '__main__':
    
    t = testMyList()
    t.testSize()
    t.testPushback()
    t.testFind()
    t.testPop()
    t.testDelete()
    t.testInsert()

    print("Everything passed!")