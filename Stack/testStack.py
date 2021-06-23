import stack
import unittest
import random

class testStack(unittest.TestCase):
    
    def testPush(self):
        s = stack.stack()
        s.push(238)
        s.push(383)
        s.push(128)

        assert s.size() == 3, "Size of stack must be 3"

    def testPop(self):
        s = stack.stack()
        s.push(238)
        s.push(383)
        s.push(128)

        assert s.pop() == 128 and s.peek() == 383 and s.size() == 2, "Pop didn't work"

    def testSize(self):
        s = stack.stack()
        expectedSize = random.randint(0,100)

        for i in range(expectedSize):
            s.push(i)

        assert s.size() == expectedSize, "Size error"



if __name__ == '__main__':
    t = testStack()
    t.testPush()
    t.testPop()
    t.testSize()
    print("Everything passed!")
