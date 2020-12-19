import re

def parse_date(input_date):
	#date_regex = re.compile(r'^\d{2}/\d{2}/\d{4}$|^\d{2},\d{2},\d{4}$|^\d{2}\.\d{2}\.\d{4}$')
	date_regex = re.compile(r'^(?P<d>\d{2})[/.,](?P<m>\d{2})[/.,](?P<y>\d{4})$')
	match = date_regex.search(input_date)
	if match:
		return {
		'd':match.group('d'),
		'm':match.group('m'),
		'y':match.group('y')
		}
	return None
	
#^(?P<d>\d{2})/(?P<m>\d{2})/(?P<y>\d{4})$|^(\d{2}),(\d{2}),(\d{4})$|^(\d{2})\.(\d{2})\.(\d{4})$

print(parse_date('12,04,2003'))
print(parse_date('01/01/19999'))