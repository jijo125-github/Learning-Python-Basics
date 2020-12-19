#validate time

import re

def is_valid_time(timee):
	time_regex = re.compile(r'^\d{1,2}:\d{1,2}$')
	match = time_regex.search(timee)
	if match:
		return True
	return False
	
print(is_valid_time("10.30"))
print(is_valid_time("1.21"))
print(is_valid_time("time is 10:30"))
print(is_valid_time("10:30"))