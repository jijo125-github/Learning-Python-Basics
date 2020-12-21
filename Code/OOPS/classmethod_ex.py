""" Example how to use classmethod decorator """

class User:
	active_users=0
	
	@classmethod   #to recognise its a class method
	def display_active_users(cls):   #cls for classmethod and self for instance method as per rules
		print(f"there are currently {cls.active_users} active users")
		
	@classmethod
	def from_string(cls,data_str):
		first,last,age=data_str.split(",")
		return cls(first,last,int(age))    #here cls will run the init method
		
	def __init__(self,first,last,age):
		self.first=first
		self.last=last
		self.age=age
		User.active_users+=1
		
	def __repr__(self):
		return f"{self.first} is {self.age}"
	
	def logout(self):
		User.active_users-=1
		return f"{self.first} has logged out"
		
	def full_name(self):                 # instance method...  Self needs to be there for every instance method we define
		return f"{self.first} {self.last}"
		
	def likes(self,item):
		return f"{self.first} likes {item}"   # no need to write self to access argument
		
	
class Moderator(User):
	total_mods=0
	def __init__(self,first,last,age,community):
		super().__init__(first,last,age)
		self.community=community
		Moderator.total_mods+=1
		
	@classmethod   #to recognise its a class method
	def display_active_mods(cls):   #cls for classmethod and self for instance method as per rules
		print(f"there are currently {cls.total_mods} active mods")	
	
	def remove_post(self):
		return f"{self.full_name()} removed a post from {self.community} community"


user1=User("Jijo","Johns",23)  #init method works on the instance being created
user2=User("Snehal","Sinha",24)	
user3=User("Jijo","Johns",23)  #init method works on the instance being created
user4=User("Snehal","Sinha",24)	
jijo=Moderator("Jijo","Johns",23,"football")
jijo2=Moderator("Jijo","Johns",23,"football")
#print(jijo.remove_post())

#jijo=User.from_string("Jijo,Johns,23")
#print(jijo.last)
#print(jijo.full_name())	
		
#print(User.active_users)
# User.display_active_users()	
# User.display_active_users()
# user3=User("Jijo","Johns",23)  #init method works on the instance being created
# user4=User("Snehal","Sinha",24)
User.display_active_users()
Moderator.display_active_mods()

#print(User.active_users)
#print(user1.logout())
#print(User.active_users)
# print(user1.first,user1.last)
# print(user2.first,user2.last)
# print(user1.full_name())  #calling instance method
# print(user2.likes("Chocolate"))