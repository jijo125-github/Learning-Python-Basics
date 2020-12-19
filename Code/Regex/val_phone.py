import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')   ##returns a regex object
	match = phone_regex.search(input)  ## here it returns a object
	if match:
		return match.group()
	return None
	
def extract_all_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')   ##returns a regex object
	match = phone_regex.findall(input)   ## here it returns a list
	return match
	#if match:
	#	return match.group()
	#return None
	
def val_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')    #first and last boundary ^ and $
	match = phone_regex.search(input)
	if match:
		return True
	return False
	
def vall_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')		
	match = phone_regex.fullmatch(input)			 #if we use fullmatch no need to use the first and the last boundary
	if match:
		return True
	return False
	
#print(extract_phone('My number is 456 345-1234'))
print(extract_all_phone('my number is 234 111-1122 or call me at 233 232-1213'))

#print(vall_phone('234 999-5678'))
#print(vall_phone('234 999-56789'))
#print(vall_phone('234 9999-5678'))