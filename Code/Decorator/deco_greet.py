""" Using Decorator when greeting """

def be_polite(fn):
	#def wrapper(name):   if single argument then
	def wrapper(*args,**kwargs):
		print("Nice to meet you")
		#fn(name)
		fn(*args,**kwargs)
		print("Have a great day")
	return wrapper

@be_polite
def greet(name):
	print(f"Hello, I'm {name}")

@be_polite	
def rage(name,food):
	print(f"{name} hate {food}")


#greet=be_polite(greet)   when we use decorator we don't need to call this
greet('Jijo')
rage('Jijo','paveka')
#rage=be_polite(rage)
#rage()