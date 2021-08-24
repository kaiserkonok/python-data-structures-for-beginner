class Stack:
    def __init__(self, size):
        self.top = 0
        self.size = size
        self.data = [None] * self.size

    def push(self, item):
        self.data[self.top] = item
        self.top += 1

    def pop(self):
        self.top = self.top - 1
        return self.data[self.top]

    def print_stack(self):
        if self.top == 0:
            print("Stack is empty!!")
        else:
            for i in range(self.top):
                print(self.data[i], end=' ')
            print()


s = Stack(5)

s.push(5)

item = s.pop()

print("Removed item =>", item)

s.print_stack()
