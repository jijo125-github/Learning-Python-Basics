""" Stack DS to reverse a string. """

from stack_ds import Stack

def rev_string(s,word):
    for ch in word:
        s.push(ch)
    rev_word = ''
    while not s.is_stack_empty():
        rev_word += s.pop()
    return rev_word

s = Stack()
string = input('Enter some word: ')
print('The rev of the string is ',rev_string(s,string))





