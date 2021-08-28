class Queue:
    def __init__(self, size):
        self.size = size
        self.head = 0
        self.tail = 0
        self.data = [None] * (self.size + 1)

    def en_queue(self, item):
        if (self.tail + 1) % (self.size + 1) == self.head:
            print("Queue is full!")
        else:
            self.data[self.tail] = item
            self.tail = (self.tail + 1) % (self.size + 1)

    def de_queue(self):
        new_item = self.data[self.head]
        self.head = (self.head + 1) % (self.size + 1)
        print("Deleted item =>", new_item)
        return new_item


q = Queue(5)

q.en_queue(8)
q.en_queue(9)
q.en_queue(10)
q.en_queue(11)
q.en_queue(12)
q.de_queue()
q.en_queue("latest")
q.de_queue()
q.en_queue("new latest")

print("head =>", q.head)
print("tail =>", q.tail)

print(q.data)
