import re
text="Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

sub_regex = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+',re.IGNORECASE)
res = sub_regex.sub("sub",text)  #so here we are substituting the word subed with those words which are matching in the pattern
result = sub_regex.sub("\g<1> \g<2>",text)
print(result)


def censor(input_text):
	pattern = re.compile(r'frack[a-z]*',re.I)
	result = pattern.sub('CENSORED',input_text)
	print(result)
	
censor("frack you")
censor("fracking you")
censor("you fracker")
censor("i hope u fracking die")