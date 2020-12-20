""" Decorator Example: Return double times """

def double_return(fn):
	def wrapper(*args,**kwargs):
		val=fn(*args,**kwargs)
		return [val,val]
	return wrapper
	
@double_return
def add(num1,num2):
	return num1+num2
	
@double_return
def greet(name):
	return f"Hi I'm {name}"


print(add(1,2))
print(greet('Jijo'))