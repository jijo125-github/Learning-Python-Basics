""" using BeautifulSoup and DictWriter from csv """

import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
	all_quotes=[]
	url = "/page/1"
	while url:
		response = requests.get(f"{BASE_URL}{url}")
		soup = BeautifulSoup(response.text,"html.parser")
		quotes=soup.find_all(class_="quote")
		
		for quote in quotes:
			name = quote.find("small").get_text()
			text = quote.find(class_="text").get_text()
			link = quote.find("a")["href"]
			all_quotes.append({'author':name,'text':text,'bio-link':link})
			
		next_btn = soup.find(class_="next")
		url = next_btn.find("a")["href"] if next_btn else None
		sleep(1)
	return all_quotes

def write_quotes(quotess):	
	with open("quotes.csv","w") as file:
		headers = ['author','text','bio-link']
		csv_writer = DictWriter(file,fieldnames=headers)
		csv_writer.writeheader()
		for quote in quotess:
			csv_writer.writerow(quote)
		
quotess = scrape_quotes()
write_quotes(quotess)