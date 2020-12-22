""" basic use of BeautifulSoup module """

from bs4 import BeautifulSoup

html_str="""
<html>
	<head>
		<title>Beautiful Soup</title>
		
		<style type="text/css">
		#first 
		{color:blue;}
		
		.green 
		{color:green;}
		
		li 
		{color:red;}
		</style>
		
	</head>
<body>
	<h1>Recipe</h1>
	<em>By Jijo</em>
	<ul>
		<li>soup</li>
		<li class="green super-green">eggs</li>
		<li class="green">water</li>
	</ul>
	<h2 id="first">color testing</h2>
	<h3 data-example="yes">hi</h3>
</body>
</html>
"""

soup=BeautifulSoup(html_str,"html.parser")
print(soup.body.ul)
print(soup.find("li"))    # it returns the first one only whichever we get
print(soup.find(id="first"))
print(soup.find_all(class_="green")[0])
print(soup.find(attrs={"data-example":"yes"}))
d=soup.select("#first")
d=soup.select(".green")
d2=soup.select("[data-example]")
print(d)
print(d2)
print(soup.find_all("li"))   # it returns all of them
print(soup.li)
print(type(soup))

attr=soup.find("h3")["data-example"]
print(attr)
attr1=soup.find("h2")["id"]
print(attr1)

for el in soup.select(".green"):
	print(el.attrs)
	print(el.name)
	print(el.get_text())