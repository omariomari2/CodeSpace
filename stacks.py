#Create Stack Class
class ArrayStack:
    def __init__(self):
        self.stack = [] 
        
    def push(self, n):
        self.stack.append(n)
    
    def isEmpty(self):
        return not self.stack  
    
    def pop(self):
        if self.isEmpty():  
            raise IndexError("Pop from empty stack!")
        return self.stack.pop()
        
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def length(self):
        return len(self.stack)

#Reversing using Stacks
def reversing(arr, start, stop):
    meh = ArrayStack()
    for i in range(start, stop):
        meh.push(arr[i])
    
    for i in range(start, stop):
        arr[i] = meh.pop()
        
    return arr

S = [1,2,3,4,5,6]
print(reversing(S, 0, 4))

def reversing(S, start, stop):
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1
        
    return S
S = [1,2,3,4,5,6]
print(reversing(S, 0, 4))

    
#Matching Parantheses 
def check_parenthesis(S):
    S = S.strip()
    diction = {'(':')', '[':']', '{':'}'}
    meh = []
    for i in S:
        if i in diction.keys():
            meh.append(i)
        elif i in diction.values():
            if not meh:
                return False
            top = meh.pop()
            if diction[top] != i:
                return False
                
    return not meh
