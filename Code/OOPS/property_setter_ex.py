""" use of property decorator and setter """

class Human:
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
	
	"""  @property is a decorator """
	@property         
	def age(self):
		return self._age

	""" @age.setter is a setter """	
	@age.setter
	def age(self,value):
		if value>=0:
			self._age=value
		else:
			raise ValueError("age can't be negative")


jijo=Human("jijo","johns",23)
print(jijo.age)	
jijo.age=100
print(jijo.age)
# jijo.age = -23
# print(jijo.age)