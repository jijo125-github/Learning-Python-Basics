def power(base, exp):
    """ to calculate power of a number using recursion """
    assert (exp >= 0) and int(exp) == exp, 'exponent should be a positive number'
    if exp == 0:
        return 1
    return base * power(base, exp-1)


print(power(2, -1))
