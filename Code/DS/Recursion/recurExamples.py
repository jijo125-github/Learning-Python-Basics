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


def factiter(num):
    """ this one is iterative way to find factorial"""
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num -= 1
    print(factorial)

# factiter(5)


def fiboiter(num):
    """ calculate fibonacci using iterative way """
    a,b,i = 0,1,0
    print(a)
    print(b)
    while i < num:
        a,b = b,a+b
        print(b)
        i += 1

# fiboiter(1)


def fibo(num):
    """ calculate fibonacii series using recursion """
    if num in [1,0]:
        return num
    else:
        return fibo(num-2) + fibo(num-1)

print(fibo(10))


    




