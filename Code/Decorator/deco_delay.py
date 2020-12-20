""" Using Decorator to delay function execution """

from functools import wraps
from time import sleep

def delay(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args,**kwargs):
			print(f"Waiting {val} seconds before running say_hi to the console")
			sleep(val)
			return fn(*args,**kwargs)
		return wrapper
	return inner
	
@delay(5)
def say_hi():
	print("hi")

	
say_hi()