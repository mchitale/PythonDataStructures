

class stack():

    def __init__(self):
        self.count = 0
        self._stack = []
        self._topOfStack = 0

    def __getitem__(self, idx):
        return self._stack[idx]

    def size(self):
        return self.count


    def push(self, num):
        self._stack.append(num)
        self.count += 1
        self._topOfStack = self.count - 1

    def pop(self):

        if self.count == 0:
            raise IndexError("Stack is empty!")

        ans = self._stack[self._topOfStack]
        del self._stack[self._topOfStack]
        self.count -= 1
        
        self._topOfStack -= 1
        return ans

    def peek(self):
        return self._stack[self._topOfStack]




