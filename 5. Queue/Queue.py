class Queue(object)
    def __init__(self)
        self.items = []

    def __len__(self)
        return self.size()

    def enqueue(self, item)
        self.items.insert(0, item)

    def dequeue(self)
        if not self.is_empty()
            return self.items.pop()

    def size(self)
        return len(self.items)

    def is_empty(self)
        return len(self.items) == 0

    def peek(self)
        if not self.is_empty()
            return self.items[-1].value