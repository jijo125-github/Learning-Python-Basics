""" Decorator to check the execution speed """

from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		start_time=time()
		fun_result=fn(*args,**kwargs)
		end_time=time()
		print(f"Elapsed time is {end_time-start_time}")
		return fun_result
	return wrapper
	

@speed_test
def sum_nums():
		return sum(x for x in range(80000000))
print(sum_nums())

@speed_test
def sum_listnum():
		return sum([x for x in range(80000000)])
print(sum_listnum())