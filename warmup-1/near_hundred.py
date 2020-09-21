def near_hundred(n):
    """Given an int n, return True if it is within 10 of 100 or 200."""
    return (90 <= n <= 110) or (190 <= n <= 210)

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))