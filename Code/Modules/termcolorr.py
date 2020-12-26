""" use of colorama module """


from colorama import init, Fore, Back, Style

init()
print(Back.LIGHTBLUE_EX)
print(Fore.RED + 'Red')
print(Back.LIGHTWHITE_EX)
print(Fore.GREEN + 'Green')
print(Back.LIGHTYELLOW_EX)
print(Fore.BLUE + 'Blue')
print(Style.RESET_ALL)