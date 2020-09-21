def diff21(n):
    """Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21."""

    difference = n - 21 #store difference as local varaible

    if n <= 21:
        return abs(difference)
    else: 
        return difference * 2
    
print(diff21(19))
print(diff21(10))
print(diff21(21))
