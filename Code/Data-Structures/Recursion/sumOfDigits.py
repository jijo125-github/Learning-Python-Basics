def sumofdigits(num):
    """ to calculate sum of digits using recursion """
    assert (num > 0) and int(num) == num, 'number should be positive digit'
    if num // 10 == 0:
        return num
    return (num % 10) + sumofdigits(num // 10)


print(sumofdigits(1395))
