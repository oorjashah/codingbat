def lone_sum(a,b,c):
    """Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum."""

    sum = a + b + c

    if a!=b and b!=c and a!=c:
        return sum 

print(lone_sum(1,2,3))
print(lone_sum(3,2,3))