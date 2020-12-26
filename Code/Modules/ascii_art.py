""" use of pyfiglet and termcolor module """


import pyfiglet
from termcolor import colored

msg=input("What would u like to print: ")
color=input("What color u want? ").lower()

ascii_art=pyfiglet.figlet_format(msg)
colored_ascii=colored(ascii_art,color=color)
print(colored_ascii)