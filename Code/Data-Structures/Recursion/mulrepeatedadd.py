""" multiply with repeated additions """

def multi(multiplier, multiplicand):
    if multiplier == 1:
        return multiplicand
    return multiplicand + multi(multiplier-1, multiplicand)


assert multi(4, 5) == 20
assert multi(4, -5) == -20
