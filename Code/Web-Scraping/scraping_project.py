""" Using BeautifulSoup to scrape quotes website and create a game """

import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep

BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
	all_quotes=[]
	links = []
	url = "/page/1"
	while url:
		response = requests.get(f"{BASE_URL}{url}")
		print(f"Now Scraping {BASE_URL}{url}...")
		soup = BeautifulSoup(response.text,"html.parser")
		quotes=soup.find_all(class_="quote")
		for quote in quotes:
			name = quote.find("small").get_text()
			text = quote.find(class_="text").get_text()
			link = quote.find("a")["href"]
			all_quotes.append({'author':name,'text':text,'bio-link':link})	
		next_btn = soup.find(class_="next")
		url = next_btn.find("a")["href"] if next_btn else None
		sleep(0.5)
	return all_quotes

def start_game(quotes): 	
	rand_quote_info = choice(quotes)
	rand_quote_text = rand_quote_info['text']
	rand_quote_author = rand_quote_info['author']
	rand_quote_link = rand_quote_info['bio-link']
	remaining_guesses = 4
	user_ans = ''

	print(f"\n{rand_quote_text}\n")
		
	while user_ans.lower() != rand_quote_author.lower() and remaining_guesses>0:
		user_ans = input(f"Who said it? Guesses remaining:{remaining_guesses}: ")
		remaining_guesses -= 1
		
		if remaining_guesses == 3 and user_ans.lower() != rand_quote_author.lower() :
			bio_response = requests.get(f"{BASE_URL}{rand_quote_link}")
			bio_soup = BeautifulSoup(bio_response.text,"html.parser")
			author_born_date = bio_soup.find(class_="author-born-date").get_text()
			author_born_location = bio_soup.find(class_="author-born-location").get_text()
			print("\nLet me give u one hint:")
			print(f"That person was born on {author_born_date} {author_born_location}\n")
			
		elif remaining_guesses == 2 and user_ans.lower() != rand_quote_author.lower():
			print("\nOne hint wasted.. No worries. One more hint")
			print(f"Name starts with {rand_quote_author[0]}\n")
			
		elif remaining_guesses == 1 and user_ans.lower() != rand_quote_author.lower():
			print("\nOh no this is the last hint. Answer or ur life is finished..")
			last_name_initial = rand_quote_author.split(" ")[1][0]
			print(f"Name ends with {last_name_initial}\n")
			
		elif user_ans.lower() == rand_quote_author.lower():
			print("\nCorrect Answer.. Lucky guy.. hehe\n")
			
		else:
			print(f"U lost the game. The correct answer is {rand_quote_author}\n")

	again = ''
	while again.lower() not in ('y','yes','n','no'):
		again = input("Want to play again? (y/n): ")
	if again.lower() in ('y','yes'):
		return start_game(quotes)
	else:
		print("Good Bye..")
		
		
quotes = scrape_quotes()
start_game(quotes)