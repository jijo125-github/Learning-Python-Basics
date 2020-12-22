""" using BeautifulSoup module to scrape and csv module to write details in CSV format. """

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")
#print(articles)

with open("blog_data.csv","w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["title","link","date"])
	for article in articles:
		a_tag = article.find("a")
		title = a_tag.get_text()
		#href = a_tag.attrs
		url = a_tag["href"]
		date_tag = article.find("time")
		date = date_tag["datetime"].split(" ")[0]
		#print(title,url,date)
		csv_writer.writerow([title,url,date])
		