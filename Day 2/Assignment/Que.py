#Implementing Stack in python
class Stack:
    def __init__(self):
        self.container = []
        self.trackMax = []

    def push(self, data):
        self.container.append(data)

        if len(self.container) == 1:
            self.trackMax.append(data)
            return

        if data >= self.trackMax[-1]:
            self.trackMax.append(data)
        else :
            self.trackMax.append(self.trackMax[-1])

    def pop(self):
        self.container.pop()
        self.trackMax.pop()

    def getMax(self):
        return self.trackMax[-1]

#Driver code
if __name__ == '__main__':

    a = int(input())
    stack = Stack()
    
    for i in range(a):
        op = input().rstrip().split()
        if op[0] == "1":
            stack.push(op[1])
        elif op[0] == "2":
            stack.pop()
        else :
            print(stack.getMax())