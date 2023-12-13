class Node:
    def __init__(self, val=None, father=None, l_child=None, r_child=None):
        self.val = val
        self.father = father
        self.l_child = l_child
        self.r_child = r_child

    def __str__(self):
        return f"Val: {self.val} - L_Child: {self.l_child} - R_Child: {self.r_child} - Father: {self.father}"


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def empty(self):
        return self.root == None

    def _recur_search(self, node, val):
        if node.val == val:
            return node
        elif node.val > val:
            return (
                node if node.l_child == None else self._recur_search(node.l_child, val)
            )
        else:
            return (
                node if node.r_child == None else self._recur_search(node.r_child, val)
            )

    def search(self, val):
        found = self._recur_search(root, val)
        print("Found!" if found.val == val else "Not Found!")

    def attach(self, val):
        if self.empty():
            self.root = Node(val)
            print("Root Created!")
            return

        node = self._recur_search(self.root, val)
        if node.val == val:
            new_node = Node(val, node, node.l_child, node.r_child)
            if node.l_child != None:
                node.l_child.father = new_node
            if node.r_child != None:
                node.r_child.father = new_node
            node.l_child = new_node
            node.r_child = None
        elif node.val > val:
            node.l_child = Node(val, node)
        else:
            node.r_child = Node(val, node)

    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)
        print()

    def _display_aux(self, node):
        if node.r_child is None and node.l_child is None:
            line = "%s" % node.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.r_child is None:
            lines, n, p, x = self._display_aux(node.l_child)
            s = "%s" % node.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.l_child is None:
            lines, n, p, x = self._display_aux(node.r_child)
            s = "%s" % node.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        l_child, n, p, x = self._display_aux(node.l_child)
        r_child, m, q, y = self._display_aux(node.r_child)
        s = "%s" % node.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            l_child += [n * " "] * (q - p)
        elif q < p:
            r_child += [m * " "] * (p - q)
        zipped_lines = zip(l_child, r_child)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == "__main__":
    bt = BinaryTree()
    bt.attach(5)
    bt.display()
    bt.attach(8)
    bt.display()
    bt.attach(3)
    print(bt.root)
    bt.display()
    bt.attach(5)
    bt.display()
    bt.attach(7)
    bt.display()
    bt.attach(9)
    bt.display()
    bt.attach(8)
    bt.display()
    bt.attach(10)
    bt.display()
    bt.attach(9)
    bt.display()
