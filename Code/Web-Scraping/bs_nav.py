""" basic use of BeautifulSoup """

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
data=soup.body.contents[1].next_sibling.next_sibling
print(data)

par_data=soup.find(class_="super-green").parent.parent
print(par_data)

par_ddata=soup.find(id="first")
print(par_ddata)
