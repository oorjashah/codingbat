def front3(str):
    if len(str) <= 3:
        return str+str+str
    return str[0:3]+str[0:3]+str[0:3]

print(front3('abc'))
print(front3('Java'))
print(front3('Chocolate'))

#for this you can also make the first three characters a variable
    