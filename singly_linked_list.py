class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def append(self, val):
        new_node = Node(val)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def prepend(self, val):
        new_node = Node(val)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove(self, val):
        cur = self.head
        if cur.val == val:
            self.head = self.head.next
            # Python GC will take care of it
            return

        cur_prev = cur
        cur = cur.next

        while cur != None:
            if cur.val == val:
                cur_prev.next = cur.next
                # Python GC will take care of it
                return

            cur_prev = cur
            cur = cur.next

    def display(self):
        current = self.head
        while current != None:
            print(f"{current.val} ", end="")
            current = current.next
        print()


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.prepend(4)
    sll.display()
    sll.remove(3)
    sll.display()
    sll.remove(1)
    sll.display()
    sll.remove(4)
    sll.display()
