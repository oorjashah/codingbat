def love6(a,b):
    """The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. """
    sum = a + b
    difference = a - b 

    return a == 6 or b ==6 or sum == 6 or difference == 6

print(love6(6,4))
print(love6(4,5))
print(love6(1,5))