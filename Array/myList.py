""" Create your own implementation of an automatically resizing vector """


class myList(object):
        """

        I/O: 
            >> a = myList(int)
            >> a.push_back(4)
            a =
            [4]
            >> a.push_back(32)
            a = 
            [4, 32]
            >> a.push_back("This will generate an error")
            Expected input to be type <class 'int'>, found <class 'str'>.

        Public Methods:
            a.push_back(num)
            a.append(num)
            a.pop()
            a.empty()
            a.size()
            a.at(idx)
            a.find(item)


        Private Methods:
            a.__checkType()

        """
        def __init__(self, argType):
            
            self.Type = argType # Data type for the list
            self.array = []

        def __getitem__(self,idx):
            return self.array[idx]

        def __setitem__(self,idx, item):
            self.array[idx] = item

        def __delitem__(self, item):
            self.array = [elem for elem in self.array if elem != item]
        
        def push_back(self, num):
            if self.__checkType(num):
                self.array.append(num)
            else:
                print("Expected input to be type {}, found {}.".format(self.Type,type(num)))

        def pop(self):
            if self.empty():
                return "Array Is Empty"
            ans = self.array[0]
            self.array = self.array[1:]
            return ans

        def empty(self):
            return len(self.array) == 0

        def size(self):
            return len(self.array)

        def at(self,idx):
            if idx >= len(self.array):
                print("Index out of bounds")
            return self.array(idx)

        def find(self,num):
            if self.empty():
                return "Array Is Empty"
            for i,elem in enumerate(self.array):
                if num == elem:
                    return i

            return "Item Not Found"

        def insert(self,idx,item):
            if not self.__checkIndex(idx):
                raise IndexError("Index Out of Bounds")
            
            list_before_idx = self.array[:idx]
            list_after_idx = self.array[idx:]
            list_before_idx.append(item)
            self.array = list_before_idx + list_after_idx

        def __checkType(self, num):
            return type(num) == self.Type

        def __checkIndex(self, idx):
            return idx >= 0 and idx <= self.size()


                
