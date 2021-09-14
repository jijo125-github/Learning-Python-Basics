# Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prep(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # If there is no head, then:
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        # If there is head, then:
        else:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)

        # If there is no head, then:
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        # If there is head, then:
        else:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        cur_node = self.head
        if cur_node is None:
            print('list is empty')
            return

        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break

    # testcase for remove invalid node left my logic
    def remove(self, key):
        cur = self.head
        prev = None
        is_key_there = False

        while cur:
            prev = cur
            cur = cur.next
            if cur.data == key and cur == self.head:
                prev.next = cur.next
                self.head = cur.next
                is_key_there = True
                cur = None
            elif cur.data == key:
                prev.next = cur.next
                is_key_there = True
                cur = None
        if not is_key_there:
            print('no such key to be deleted')
            return

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    # this is overwriting the inbuilt method
    def __len__(self):
        cur = self.head
        if cur is None:
            return 0

        nodes = 1
        while cur.next != self.head:
            cur = cur.next
            nodes += 1
        return nodes

    def split(self):
        cur = self.head
        prev = None
        length = len(self)
        if length == 0:
            return None
        if length == 1:
            print(self.head.data)
            return

        mid = length // 2
        pos = 0
        while cur and pos != mid:
            prev = cur
            cur = cur.next
            pos += 1
        prev.next = self.head

        new_list = CircularLinkedList()
        new_list.head = cur

        cur = new_list.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_list.head

        print('First list')
        self.print_list()
        print('Second list')
        new_list.print_list()

    def josephus_circle(self, step):
        cur = self.head
        count, total = 1, 1
        length = len(self)
        while cur and total < length:
            if count == step:
                print('Removed: ', cur.data)
                self.remove_node(cur)
                total += 1
                count = 0
            else:
                cur = cur.next
                count += 1
        self.print_list()

    def is_linked_list_circular(self, llist):
        cur = llist.head
        head = llist.head
        while cur:
            cur = cur.next
            if cur == head:
                return True
        return False


lin1 = CircularLinkedList()
lin1.append(1)
lin1.append(2)
lin1.append(3)
lin1.append(4)
lin2 = LinkedList()
lin2.append(1)
lin2.append(2)
lin2.append(3)
lin2.append(4)
print(lin1.is_linked_list_circular(lin2))

# lin1.prepend('C')
# lin1.prepend('B')
# lin1.prepend('A')
# lin1.append('E')
# lin1.append('F')
# lin1.josephus_circle(3)
# lin1.remove('C')
# lin1.remove('F')
# print('Before split')
# lin1.print_list()
# print('After split')
# lin1.split()
