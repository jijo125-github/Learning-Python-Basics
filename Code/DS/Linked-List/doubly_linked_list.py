# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.prev = None
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    def print_list(self):
        cur = self.head
        if not self.head:
            return
        while cur:
            # print('Current node Value: ', cur.data)
            print(cur.data)
            # prev = cur.prev
            cur = cur.next
            # if prev:
            #     print('Previous node value: ', prev.data)
            # if cur:
            #     print('Next node value: ', cur.data)

    def add_node_after(self,key,data):
        new_node = Node(data)
        cur = self.head

        # if the key is not tail
        while cur.next:
            if cur.data == key:
                new_node.next = cur.next
                new_node.prev = cur
                cur.next.prev = new_node
                cur.next = new_node
                return
            cur = cur.next

        # if the key is tail or it's not a valid key
        if cur.data == key:
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
        else:
            print('Not a valid key..')
            return

    def add_node_before(self,key,data):
        new_node = Node(data)

        # if key is head node
        if self.head.data == key:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
            return

        # if key is after head or not a valid key
        cur = self.head.next
        while cur:
            if cur.data == key:
                new_node.prev = cur.prev
                new_node.next = cur
                cur.prev.next = new_node
                cur.prev = new_node
                return
            cur = cur.next
        if not cur:
            print('Not a valid key')
            return

    def delete_node(self,key):
        if not self.head:
            return

        # if head is the key to be deleted
        if self.head.data == key:
            next_node = self.head.next
            next_node.prev = None
            self.head.next = None
            self.head = next_node
            return

        # any node between head and tail
        cur = self.head
        while cur.next:
            if cur.data == key:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = None
                return
            cur = cur.next

        # tail node or there are no valid nodes:
        if cur.data == key:
            cur.prev.next = None
            cur.next = None
            cur.prev = None
            cur = None
            return
        elif not cur:
            print('no valid key to delete')
            return

    # this method we directly print
    def reverse_list(self):
        if not self.head:
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        tail = cur
        while tail:
            print(tail.data)
            tail = tail.prev

    # this method we reverse the links to the nodes
    def reverse(self):
        if not self.head:
            return
        cur = self.head
        temp = None
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        if not self.head:
            return

        dict_values = dict()
        cur = self.head
        while cur:
            if cur.data in dict_values:
                nxt = cur.next
                self.delete_node(cur.data)
                cur = nxt
            else:
                dict_values[cur.data] = 1
                cur = cur.next

    def pairs_with_sum(self,sum_val):
        pairs = []
        cur = self.head
        while cur:
            new_cur = cur.next
            while new_cur:
                if cur.data + new_cur.data == sum_val:
                    pairs.append([cur.data,new_cur.data])
                new_cur = new_cur.next
            cur = cur.next
        print(pairs)


lin1 = DoublyLinkedList()
# lin1.prepend('A')
# lin1.append('C')
# lin1.add_node_after('C','D')
# lin1.add_node_before('C','B')
# lin1.add_node_after('D','F')
# lin1.add_node_before('A','Z')
# lin1.add_node_before('F','E')
lin1.append(1)
lin1.append(2)
lin1.append(3)
lin1.append(4)
lin1.append(5)
# lin1.print_list()
# print('REmoving duplicates')
# lin1.remove_duplicates()
lin1.print_list()
# print('After reversal')
# lin1.reverse()
print('Pairs')
lin1.pairs_with_sum(7)
# lin1.reverse_list()
# lin1.delete_node('F')
# print('After deletion')
# lin1.print_list()
