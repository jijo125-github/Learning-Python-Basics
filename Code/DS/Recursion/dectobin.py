def decimaltobinary(num):
    """ to convert decimal number to binary using recursion """
    assert int(num) == num, 'number should be integer only'
    if num == 0:
        return 0
    quot = num // 2
    rem = num % 2
    return rem + 10 * decimaltobinary(quot)


print(decimaltobinary(10))
