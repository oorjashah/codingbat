def front_back(str):
    """Given a string, return a new string where the first and last chars have been exchanged."""
    
    if len(str) <= 1: 
        return str
  
    mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
    return str[len(str)-1] + mid + str[0]

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))