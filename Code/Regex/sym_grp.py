import re

def sym_grp(input):
	str_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-za-z]+)$')
	matches = str_regex.search(input)
	print(matches.group())
	print(matches.group(1))
	print(matches.group("first"))
	print(matches.group("last"))
	
#sym_grp("Mr. Johns Jijo")

def comp_fg(input):
	str_regex = re.compile(r"""^(Mr\.|Mrs\.|Ms\.Mdme\.) (?P<first>[a-z]+) (?P<last>[a-z]+)$""",re.IGNORECASE)
	matches = str_regex.search(input)
	print(matches.groups())
	
comp_fg("Mr. Johns Jijo")	