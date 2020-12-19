import re

def parse_bytes(input_byte):
	byte_regex = re.compile(r'\b[01]{8}\b')
	match = byte_regex.findall(input_byte)
	return match
	
print(parse_bytes("11011100"))
print(parse_bytes("my data is: 10101111 11110000"))
print(parse_bytes("asdfg"))