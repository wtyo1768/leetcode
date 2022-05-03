class MaxStack:
    # two lists have the same length, pop&push operations have to update both lists
    # For popmax, starting from end of stack list, saving all the poped items in tmp list, 
       # then reverse tmp, add the items back to stack one by one to update the max list.
    
    def __init__(self):
        self.stack = []
        self.max = []
    
    def push(self, x):
        self.stack.append(x)
        if self.max:
            curMax = max(x, self.max[-1])
            self.max.append(curMax)
        else:
            self.max.append(x)

    def pop(self):
        if self.stack:
            self.max.pop()
            return self.stack.pop()

    def top(self):
        if self.stack: return self.stack[-1]

    def peekMax(self):
        if self.max: return self.max[-1]


    def popMax(self):
        curMax = self.max[-1]
        tmp = []

        while True:
            if self.stack[-1] != curMax:
                tmp.append(self.stack.pop())
                self.max.pop()
            else:
                self.stack.pop()
                self.max.pop()
                break
        while tmp: self.push(tmp.pop())
        return curMax

s = MaxStack()
s.push(5)
s.push(1)
s.push(5)

print(s.top(), s.max, s.stack)
print(s.popMax(), s.max, s.stack)
print(s.top(), s.max, s.stack)
print(s.popMax(), s.max, s.stack)
print(s.pop(), s.max, s.stack)
print(s.top(), s.max, s.stack)