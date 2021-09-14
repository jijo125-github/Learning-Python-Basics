""" Use stack data structure to convert integer values to binary. """

from stack_ds import Stack

def int_to_bin(number):
	num_list = []
	bin_num = ''
	while number > 0:
		temp = number % 2
		num_list.append(temp)
		number = number // 2
	for num in num_list[::-1]:
		bin_num += str(num)
	return int(bin_num)


def int_to_bin_stack(number):
	st = Stack()
	ans = ''
	while number > 0:
		temp = number % 2
		st.push(temp)
		number = number // 2
	while not st.is_stack_empty():
		temp = st.pop()
		ans += str(temp)
	return ans	
	
print(int_to_bin_stack(217))
	