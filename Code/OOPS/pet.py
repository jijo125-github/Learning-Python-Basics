""" OOPS example """

class Pet:
	allowed=['dog','cat','fish','horse']
	def __init__(self,name,species):
		if species not in Pet.allowed:
			raise ValueError(f"u can't have {species} as pet")
		self.name=name
		self.species=species
		
cat=Pet("John","cat")
dog=Pet("Bolt","dog")
tiger=Pet("Amit","tiger") # it will raise ValueError here
print(cat.name)