def sum_double(a,b):
    """Given two int values, return their sum. Unless the two values are the same, then return double their sum."""

    sum = a + b #store sum as local variable
    if a == b:
        return sum * 2 #double sum if a and b are the same
    else:
        return sum

print(sum_double(1,2))
print(sum_double(3,2))
print(sum_double(2,2))