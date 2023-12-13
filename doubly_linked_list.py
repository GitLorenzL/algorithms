class Node:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def init(self, new_node: Node):
        self.head = new_node
        self.tail = new_node
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

    def append(self, val):
        new_node = Node(val)
        if self.empty():
            self.init(new_node)
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = self.tail.next

    def prepend(self, val):
        # In doubly linked list, prepend == append because it's a circle
        self.append(val)

    def insert(self, val, index):
        behind_this = self.head
        for i in range(index):
            behind_this = behind_this.next

        new_node = Node(val, behind_this.next, behind_this)
        behind_this.next = new_node
        behind_this.next.next.prev = new_node

    def search(self, val) -> bool:
        cur = self.head
        if cur.val == val:
            return True
        cur = cur.next

        while cur != self.head:
            if cur.val == val:
                return True

        return False

    def display(self):
        if self.empty():
            print("Empty!")
            return

        current = self.head
        print(f"{current.val} ", end="")
        current = current.next

        while current != self.head:
            print(f"{current.val} ", end="")
            current = current.next
        print()


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(4)
    dll.insert(10, 2)
    dll.display()

    cur = dll.head
    while True:
        print(f"1. Forward; 2. Backward.", end="")
        cmd = int(input())
        if cmd == 1:
            cur = cur.next
            print(cur.val)
        elif cmd == 2:
            cur = cur.prev
            print(cur.val)
        else:
            print("")
