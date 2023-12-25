class Queue:
    def __init__(self) -> None:
        self.store = []

    def empty(self):
        return len(self.store) == 0

    # I know the following code could err if empty :)
    def peek(self):
        return self.store[0]

    def pop(self):
        v = self.store[0]
        del self.store[0]
        return v

    def push(self, val):
        self.store.append(val)

    def display(self):
        for i in self.store:
            print(f"{i} ", end="")
        print()


if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())
    queue.pop()
    queue.display()
    queue.pop()
    queue.display()
    queue.pop()
    queue.display()
