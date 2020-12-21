""" Example how to use super to access parent"""

class Animal:
	def __init__(self,name,species):
		self.name=name
		self.species=species
		
	def __repr__(self):
		return f"{self.name} is a {self.species}"
		
	def make_sound(self,sound):
		print(f"this animal says {sound}")
		
			
class Cat(Animal):
	def __init__(self,name,species,breed,toy):
		super().__init__(name,species)     #here we don't need to declare self
		#Animal.__init__(self,name,species)   #one way of accesing the base class properties
		#self.name=name
		#self.species=species
		self.breed=breed
		self.toy=toy


maaya=Cat("maaya","tiger","a","b")
print(maaya.species)
print(maaya.breed)