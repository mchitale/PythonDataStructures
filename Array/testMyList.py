from myList import myList
import random
import unittest

def testSize():
    
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


def testPushback():
    
    arr = myList(float)

    for i in range(5):
        num = random.uniform(0.0,100.0)
        arr.push_back(num)
        assert arr[-1] == num, "push_back must append at the end"
    
    assert arr.size() == 5


def testAt():
    arr = myList(int)
    for i in range(10):
        num = random.randint(0,20)
        arr.push_back(num)
        assert arr.at(i) == num, "Wrong number found at index {}".format(i)


def testInsert():
    arr = myList(int)
    
    for i in range(10):
        arr.push_back(i+1)

    arr.insert(4,74)
    assert arr[4] == 74, "insert failed"

    
def testPop():
    arr = myList(int)
    
    for i in range(10):
        arr.push_back(i+1)

    elem = arr.pop()
    assert elem == 1, "Popped element must be equal to 1"
    assert arr.size() == 9, "Array size after popping must be 9"

def testDelete():
    
    arr = myList(int)
    
    for i in range(10):
        arr.push_back(i+1)

    numToDelete = arr[random.randint(1,10)]
    del arr[numToDelete]
    assert arr.size() == 9, "New array size must be 9"


def testFind():
    arr = myList(int)
    
    for i in range(10):
        arr.push_back(i+1)

    assert arr.find(7) == 6, "Find failed"
    




if __name__ == '__main__':
    testSize()
    testPushback()
    testFind()
    testPop()
    testDelete()
    testInsert()

    print("Everything passed!")