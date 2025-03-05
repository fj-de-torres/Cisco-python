class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        self.count = 0
        Stack.__init__(self)    #

    def get_counter(self):
        return self.count
    

    def pop(self):
        val = Stack.pop(self)
        self.count += 1
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
