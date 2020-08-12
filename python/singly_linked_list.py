class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        str_res = ""
        while node:
            str_res += node.data + " -> "
            node = node.next
        str_res += "NULL"
        print(str_res)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, data):
        cur_node = self.head
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
        else:
            prev = None
            while cur_node and cur_node.data != data:
                prev = cur_node
                cur_node = cur_node.next
            if cur_node:
                prev.next = cur_node.next
                cur_node = None

    def delete_at(self, pos):
        cur_node = self.head

        if self.head and pos == 0:
            self.head = cur_node.next
            cur_node = None
        else:
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node:
                prev.next = cur_node.next
                cur_node = None

    def swap(self, data1, data2):
        if data1 == data2:
            return
        # Search for data1
        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != data1:
            prev1 = cur1
            cur1 = cur1.next
        # Search for data2
        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != data2:
            prev2 = cur2
            cur2 = cur2.next

        if cur1 and cur2:
            if prev1:
                prev1.next = cur2
            else:
                self.head = cur2

            if prev2:
                prev2.next = cur1
            else:
                self.head = cur1

            cur1.next, cur2.next = cur2.next, cur1.next

    def reverse_iterative(self):
        # A -> B -> C -> D -> null
        # to
        # D -> C -> B -> A -> null
        # or
        # null <- A <- B <- C <- D
        prev = None
        cur_node = self.head
        while cur_node:
            old_next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = old_next
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if cur is None:
                return prev
            old_next = cur.next
            cur.next = prev
            prev = cur
            cur = old_next
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(self.head, None)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()

# llist.reverse_iterative()
llist.reverse_recursive()
llist.print_list()

# llist.swap("B", "D")

# llist.prepend("E")
# llist.insert_after(llist.head.next, "D")
# llist.print_list()
# llist.delete_at(2)


