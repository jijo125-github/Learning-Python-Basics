""" Method Resolution Order (MRO) """

class A:
	def do_something(self):
		print("Method defined in A")
		
class B(A):
	def do_something(self):
		print("Method defined in B")
		super().do_something()
		
class C(A):
	def do_something(self):
		print("Method defined in C")
		super().do_something()
		
class D(B,C):
	""" we have used multiple inheritance here """                               
	def do_something(self):
		print("Method defined in D")
		super().do_something()
		
		
thing=D()
thing.do_something()
print(D.__mro__)   #==>   D,B,C,A,object
print(D.mro()) #above is dunder way and here it is function way
# help(D)