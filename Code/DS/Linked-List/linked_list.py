# Linked List

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_listt():
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

	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print('Previous node is not in the list')
			return

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key):
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return

		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

			if cur_node is None:
				return

		prev.next = cur_node.next
		cur_node = None

	def delete_node_position(self, position):
		cur_node = self.head
		ind = 0

		if cur_node is None:
			print('There are no nodes to be deleted')
			return

		if ind == position:
			self.head = cur_node.next
			cur_node = None
			return

		prev_node = None
		while cur_node and ind != position:
			prev_node = cur_node
			cur_node = cur_node.next
			ind += 1

		if cur_node is None:
			print('There is no such node.. Input proper node..')
			return

		prev_node.next = cur_node.next
		cur_node = None
		return

	def linked_list_length_iterative(self):
		cur_node = self.head
		ind = 0
		while cur_node:
			cur_node = cur_node.next
			ind += 1
		return ind

	def linked_list_length_recursive(self,node):
		if node is None:
			return 0
		return 1 + self.linked_list_length_recursive(node.next)

	def node_swap(self, key1, key2):

		if key1 == key2:
			return

		prev1 = None
		cur_nodeA = self.head
		while cur_nodeA and cur_nodeA.data != key1:
			prev1 = cur_nodeA
			cur_nodeA = cur_nodeA.next

		prev2 = None
		cur_nodeB = self.head
		while cur_nodeB and cur_nodeB.data != key2:
			prev2 = cur_nodeB
			cur_nodeB = cur_nodeB.next

		if not cur_nodeA or not cur_nodeB:
			return

		if prev1:
			prev1.next = cur_nodeB
		else:
			self.head = cur_nodeB

		if prev2:
			prev2.next = cur_nodeA
		else:
			self.head = cur_nodeA

		cur_nodeA.next, cur_nodeB.next = cur_nodeB.next, cur_nodeA.next

	def linked_list_rev(self):
		cur_node = self.head
		prev = None
		while cur_node:
			nxt = cur_node.next
			cur_node.next = prev
			prev = cur_node
			cur_node = nxt
		self.head = prev

	def merge_sortedlist(self, llist):
		nodeA = self.head
		nodeB = llist.head
		nodeT = None

		if not nodeA:
			return nodeB
		if not nodeB:
			return nodeA

		if nodeA and nodeB:
			if nodeA.data <= nodeB.data:
				nodeT = nodeA
				nodeA = nodeT.next
			else:
				nodeT = nodeB
				nodeB = nodeT.next
			new_head = nodeT

		while nodeA and nodeB:
			if nodeA.data <= nodeB.data:
				nodeT.next = nodeA
				nodeT = nodeA
				nodeA = nodeT.next
			else:
				nodeT.next = nodeB
				nodeT = nodeB
				nodeB = nodeT.next

		if not nodeA:
			nodeT.next = nodeB
		if not nodeB:
			nodeT.next = nodeA
		return new_head

	def remove_duplicates(self):
		cur_node = self.head
		prev = None
		dict_values = dict()

		while cur_node:
			if cur_node.data in dict_values:
				prev.next = cur_node.next
				cur_node = None
			else:
				dict_values[cur_node.data] = 1
				prev = cur_node
			cur_node = prev.next

	def nth_to_lastnode(self,pos):
		length = self.linked_list_length_iterative()
		if pos >= length:
			print('Give proper position')
			return

		ind = 0
		cur_node = self.head
		while cur_node and ind != pos:
			cur_node = cur_node.next
			ind += 1
		self.head = cur_node

	def count_occurences_iterative(self,data):
		cur_node = self.head
		count = 0
		while cur_node:
			if cur_node.data == data:
				count += 1
			cur_node = cur_node.next

		if count:
			print(f'There are {count} occurences of ',data)
		else:
			print('There is no such data')

	def count_occurences_recursive(self,node,data):
		if not node:
			return 0
		if node.data == data:
			return 1 + self.count_occurences_recursive(node.next,data)
		else:
			return self.count_occurences_recursive(node.next,data)

	def rotate(self,key):
		p = None
		cur_node = self.head
		while cur_node:
			if key == cur_node.data:
				p = cur_node
			q = cur_node
			cur_node = cur_node.next
		if p is None:
			print("Invalid key")
		else:
			q.next = self.head
			self.head,p.next = p.next,None

	def move_tail_to_head(self):
		cur_node = self.head
		prev_node = self.head
		while cur_node.next:
			prev_node = cur_node
			cur_node = cur_node.next
		cur_node.next = self.head
		self.head = cur_node
		prev_node.next = None

	def sum_linked_list(self, llist): # one method to do it
		nodeA = self.head
		nodeB = llist.head
		summ, poww = 0,0
		while nodeA:
			summ += (nodeA.data * pow(10,poww))
			nodeA = nodeA.next
			poww += 1
		poww = 0
		while nodeB:
			summ += (nodeB.data * pow(10,poww))
			nodeB = nodeB.next
			poww += 1
		print('Sum of two linked list is: ', summ)

	def sum_link_list_carry(self,llist):
		pass



lin1 = Linked_listt()
lin1.append(1)
lin1.append(2)
lin1.append(3)
# lin1.print_list()
lin2 = Linked_listt()
lin2.append(5)
# lin2.print_list()
# lin1.sum_linked_list(lin2)
# lin1.count_occurences_iterative('A')
# print(lin1.count_occurences_recursive(lin1.head,'A'))
# lin1.rotate(2)
# print('tail to head: ')
# lin1.move_tail_to_head()
# lin1.print_list()
# lin1.nth_to_lastnode(3)
# lin1.print_list()
# print('Linked list elements with duplicates')
# lin1.print_list()
# lin1.remove_duplicates()
# print('Duplicates removed')
# lin1.print_list()
# lin2 = Linked_listt()
# lin2.append(2)
# lin2.append(3)
# lin2.append(4)
# lin2.append(6)
# lin2.append(8)
# print('Second Linked list')
# lin2.print_list()
# print('Merge both linked list:')
# lin1.merge_sortedlist(lin2)
# lin1.print_list()
# lin.node_swap('B','D')
# print('After swap')
# lin.linked_list_rev()
# print('REverseing the linked list')
# lin.print_list()
# lin.prep('E')
# lin.linked_list_length_iterative()
# lin.delete_node('C')
# lin.print_list()
# lin.linked_list_length_iterative()
# print('The length thru recursive mode is ',lin.linked_list_length_recursive(lin.head))
# print('head data',lin.head.data)
# print('next data after head',lin.head.next.data)
# print('Appending')
# lin.print_list()
# lin.prep('D')
# print('Prepending')
# lin.print_list()
# print('Insert node after')
# lin.insert_after_node(lin.head.next,'E')
# lin.print_list()
# lin.delete_node('B')
# print('Deleting B')
# print('head data',lin.head.data)
# lin.print_list()
# lin.delete_node('B')
# print('Before deleting')
# lin.print_list()
# lin.delete_node_position(2)
# print('After deleting')