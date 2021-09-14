def recursiveMethod(n):
    """ to recursively call number and print """
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

# recursiveMethod(5)


def fact(num):
    """ Implement factorial of a number via recursion """
    assert num >= 0 and int(num) == num, 'the number must be positive integer only'
    if num == 1:
        return 1
    else:
        answer = num * fact(num - 1)
        return answer
        
# print(fact(5))


def fibo(num):
    """ calculate fibonacii series using recursion """
    if num in [1,0]:
        return num
    else:
        return fibo(num-2) + fibo(num-1)

# print(fibo(10))


def productOfArray(arr):
    """ calculate product of digits in array using recursion """
    if arr == []:
        return 1
    return arr[-1] * productOfArray(arr[:-1])

# print(productOfArray([3,2,4]))


def reverse(strng):
    """ recursive func which accepts a string and returns new string in reverse """
    if len(strng) == 1:
        return strng
    return strng[-1] + reverse(strng[:-1])

# print(reverse('Jijo'))


def isPalindrome(strng):
    """ check string is palindrome using recursion way"""
    if len(strng) == 1:
        return True
    if strng[-1] == strng[0]:
        return isPalindrome(strng[1:-1])
    return False

print(isPalindrome('malayalam'))
