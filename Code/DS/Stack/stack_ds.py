""" Stack Data Structure """

class Stack():
	def __init__(self):
		self.items = []
		
	def push(self,item):
		""" push some new item """ 
		self.items.append(item)
		
	def pop(self):
		""" pop the latest one which is only possible in stack """ 
		return self.items.pop()
		
	def is_stack_empty(self):
		""" to check if stack empty or not """
		return self.items == []
	
	def latest_entry(self):
		""" display the latest entry """
		if self.is_stack_empty():
			return 'Stack is empty.. input something'
		return self.items[-1]
	
	def stack_count(self):
		""" checks how many items in the stack """
		return len(self.items)
		
	def disp_cur_items(self):
		""" the current items list """
		return self.items
		
s = Stack()
print(s.is_stack_empty())
print(s.latest_entry())
print(s.disp_cur_items())
s.push('A')
s.push('B')
s.push('D')
print(s.latest_entry())
print(s.disp_cur_items())
s.pop()
print(s.disp_cur_items())
s.push('F')
print('how many items in the stack: ',s.stack_count())
		
	
		
	
		