""" Determine if parenthesis are balanced using Stack Data Structure """

from stack_ds import Stack

def is_match(top,paren):
	if top == '{' and paren == '}':
		return True
	elif top == '[' and paren == ']':
		return True
	elif top == '(' and paren == ')':
		return True
	return False
	
def is_paren_balanced(paren_string):
	s = Stack()
	is_balanced = True
	index = 0
	while index < len(paren_string) and is_balanced:
		paren = paren_string[index]
		if paren in '{[(':
			s.push(paren)
		else:
			if s.is_stack_empty():
				is_balanced = False
			else:
				top = s.pop()
				if not is_match(top,paren):
					is_balanced = False
		index += 1
		
	if s.is_stack_empty() and is_balanced:
		return True
	return False
	
print(is_paren_balanced('([[]'))



	
