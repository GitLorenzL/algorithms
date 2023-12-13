class Stack:
    def __init__(self) -> None:
        self.store = []

    def empty(self):
        return len(self.store) == 0

    # I know the following code could err if empty :)
    def peek(self):
        return self.store[-1]

    def pop(self):
        v = self.store[-1]
        del self.store[-1]
        return v

    def push(self, val):
        self.store.append(val)

    def display(self):
        for i in self.store:
            print(f"{i} ", end="")
        print()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    stack.pop()
    stack.display()
    stack.pop()
    stack.display()
    stack.pop()
    stack.display()
