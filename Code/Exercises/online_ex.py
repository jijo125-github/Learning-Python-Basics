""" ----------exercises online attempted------------ """


""" Write a Python program to display the current date and time """
def date_time():
	import datetime
	x = datetime.datetime.now()
	return x.strftime("%Y-%m-%d %H:%M:%S")
# print(date_time())


""" Write a Python program which accepts the radius of a circle from the user and compute the area. """
def circle_area():
	from math import pi
	rad = float(input("Enter the radius of the circle: "))
	area = pi*rad*rad
	return area	
# print(circle_area())


""" Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them """
def rev(fname,lname):
	return f"{lname} {fname}"
# print(rev('Jijo','Johns'))


""" Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. """
def conv():
	val = input("Enter the values in comma seperated format: ")
	lval = list(val.split(","))
	tval = tuple(val.split(","))
	return f"List:{lval}\nTuple:{tval}"	
# print(conv())


""" Write a Python program to accept a filename from the user and print the extension of that. """
def exten():
	val = input("Enter the file: ")
	return val.split(".")[-1]	
# print(exten())


""" Write a Python program to display the first and last colors from the following list. """
def colorlist():
	color_list = ["Red","Green","White" ,"Black"]
	firstcolor = color_list[0]
	lastcolor = color_list[-1]
	return firstcolor,lastcolor
# print(colorlist())


""" Write a Python program to display the examination schedule. """
def sch():
	exam_st_date = (11, 12, 2014)
	#return f"{exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}"
	return "The examination will start from : %i / %i / %i"%exam_st_date
# print(sch())


""" Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. """
def mt(num1):
	i,sum=0,0
	temp_num=''
	while i<3:
		temp_num+=str(num1)	
		sum+=int(temp_num)
		i+=1
	return sum
# print(mt(5))


""" Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). """
def syn(fun):
	return fun.__doc__
# print(syn('abs'))


""" Write a Python program to print the calendar of a given month and year. """
def calendarr():
	import calendar
	y = int(input("Input the year : "))
	m = int(input("Input the month : "))
	return calendar.month(y,m)
# print(calendarr())


""" Write a Python program to calculate number of days between two dates. """
def datediffer():
	from datetime import date
	fd=date(2014,7,2)
	ld=date(2014,7,11)
	delta=ld-fd
	return delta.days
# print(datediffer())


""" Volume of a sphere. """
def vsphere(r):
	from math import pi
	return (4/3)*pi*r*r*r
#print(vsphere(6))


""" Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. """
def diff(numm):
	ans = 17-numm
	if numm>17:
		return abs(ans*2)
	return ans
#print(diff(20))


""" Write a Python program to test whether a number is within 100 of 1000 or 2000. """
def nearby(numm):
	if abs(1000-numm)<=100:
		return f"{numm} nearby to 1000"
	elif abs(2000-numm)<=100:
		return f"{numm} nearby to 2000"
	else:
		return "not nearby to any of them"
#print(nearby(1500))


""" Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. """ 
def summm(num1,num2,num3):
	if num1==num2==num3:
		return num1*(num1*3)
	else:
		return num1+num2+num3
#print(summm(3,3,3))


"""Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged """
def addstr():
	inp = input("Enter the string: ")
	if inp[:2]=='ls':
		return inp
	return 'ls'+inp
#print(addstr())


""" Write a Python program to get a string which is n (non-negative integer) copies of a given string. """
def nstring():
	strr = input("give any string: ")
	times = int(input("how many times: "))
	res = ''
	for i in range(times):
		res+=strr
	return res		
#print(nstring())


""" Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. """
def oddeven():
	inp = int(input("Enter a number: "))
	if inp % 2 == 0:
		return f"{inp} is an even number"
	return f"{inp} is an odd number"
#print(oddeven())


""" Write a Python program to count the number 4 in a given list. """
def countnum(list1,num):
	return f"the count of {num} in the given {list1} is {list1.count(num)}"
#print(countnum([1,1,1,2,3],1))	


""" Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. """
def prog():
	string1 = input("Enter the string: ")
	numtimes = int(input("No of copies: "))
	temp_str = ''
	for i in range(numtimes): 
		if len(string1)<2:
			temp_str+=string1
		else:
			temp_str+=string1[:2]
	return temp_str
#print(prog())


""" Write a Python program to test whether a passed letter is a vowel or not. """
def vowel(ch1):
	if ch1 in 'aeiou':
		return f"{ch1} is a vowel"
	return f"{ch1} is not a vowel"
#print(vowel('ae'))


""" Write a Python program to check whether a specified value is contained in a group of values. """
def numpresent(list1,num1):
	if num1 in list1:
		return f"{num1} is there in {list1}"
	return f"{num1} is not in {list1}"
#print(numpresent([1,2,3],5))


""" Write a Python program to create a histogram from a given list of integers. """
def histogram(list1,ch1):
	temp_str = ''
	for s in list1:
		for i in range(s):
			temp_str += ch1
		print(temp_str)
		temp_str = ''
#histogram([2,3,1,5],'@')


""" Write a Python program to concatenate all elements in a list into a string and return it. """
def conc(list1):
	temp_str = ''
	i=0
	while i<len(list1):
		temp_str += str(list1[i])
		i+=1
	return temp_str
#print(conc([11,22,33]))


""" Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. """
def eve():
	numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
	for num in numbers:
			if num%2==0:
				print(num)
			if num==237:
				break
#eve()


""" Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. """ 
def colorpre():
	color_list_1 = set(["White", "Black", "Red"])
	color_list_2 = set(["Red", "Green"])
	#return {color for color in color_list_1 if color not in color_list_2}	
	return color_list_1.difference(color_list_2)
#print(colorpre())


""" Write a Python program that will accept the base and height of a triangle and compute the area. """
def triarea(base,height):
	area = 0.5 * base *  height
	return area
#print(triarea(10,10))

 
""" Check whether a number is prime number or not """
def prime(num1):
	count=0
	i=1
	while i<=num1:
		if num1%i==0:
			count+=1
		i+=1
	if count==2:
		return f"{num1} is prime"
	return f"{num1} is not prime"
#print(prime(10))


""" Write a Python program to compute the greatest common divisor (GCD) of two positive integers. (simplified version) """
def gcd(x,y):
	gcd=1
	for i in range(1,x+1):
		if x % i == 0 and y % i == 0:
			gcd=i
	print(gcd)
#gcd(336,360)


""" Write a Python program to get the least common multiple (LCM) of two positive integers. """
def lcm(x,y):
	if x>y:
		z=x
	if y>x:
		z=y
		
	lcm=1
	while True:
		if z%x==0 and z%y==0:
			lcm=z
			break
		z+=1
	return lcm
#print(lcm(336,360))


""" Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. """
def sumprog(a,b,c):
	sum=0
	if a==b or a==c or b==c:
		return "sum is 0"
	else:
		return a+b+c
#print(sumprog(2,2,2))


""" Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. """
def suum(a,b):
	if a+b in range(15,20):
		return 20
	return a+b
#print(suum(7,5))


""" Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. """
def difpro(x,y):
	if x==y or x+y==5 or x-y==5:
		return True
	return False
#print(difpro(5,5))


""" Write a Python program to add two objects if both objects are an integer type. """
def addtype(a,b):
	if isinstance(a,int) and isinstance(b,int):
		return a+b
	raise TypeError("type must be same")	
#print(addtype(11,22))


""" Write a Python program to solve (x + y) * (x + y). """
def sol(x,y):
	s = x + y
	return f"{x}+{y}^2={s*s}" 
#print(sol(11,2))


""" To check if a year is leap year or not """
def is_leap(year):
	leap = False
	if year%4==0:
		if year%100==0 and year%400!=0:
			leap=False
		else:
			leap=True
	else:
		leap=False
	return leap
#print(is_leap(2100))


""" Print num in a line """
def trr(num):
	str_num=''
	for i in range(1,num+1):
		str_num=str_num+str(i)
	print(str_num)
# trr(3)


""" Triangle quest """
def triii(n):
	for i in range(1,n):
		print((10**(i)//9)*i)
# triii(5)