""" use of requests, pyfiglet module with one API example """


import requests
from random import choice
from pyfiglet import figlet_format

header=figlet_format("Search joke!")
print(header)

url="https://icanhazdadjoke.com/search"
term_input=input("Let me tell u a joke! Give me a topic: ")

response=requests.get(
		url,
		headers={"Accept":"application/json"},
		params={"term":term_input}
		).json()
		 
total_jokes=response['total_jokes']
jokes=[data['joke'] for data in response['results']]

if total_jokes>1:
	print(f"I have got {total_jokes} jokes about {term_input}. Here's one:\n")
	rand_joke=choice(jokes)
	print(rand_joke)
	
elif total_jokes==1:
	print(f"I have got {total_jokes} joke about {term_input}. Here it is: \n")
	print(jokes)
	
else:
	print(f"Sorry, I don't have any jokes about {term_input}. Please try again")