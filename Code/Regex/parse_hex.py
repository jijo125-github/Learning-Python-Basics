import re

def extract_hexcode(line):
    line_regex = re.compile(r'\b#([0-9(A-F|a-f)]{6}|[0-9(A-F|a-f)]{3})\b')
    match = line_regex.findall(line)
    return match
	
print(extract_hexcode('#BED'))