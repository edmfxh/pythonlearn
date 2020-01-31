i = 1
print("-"*50)
while i < 3:
    n = 1
    while n <= 3:
        print("{:5d}".format(i*n))#, end = ' '))
        n += 1
    print()
    i += 1
print("-"*50)
#没打end
#1
#2
#3

#2
#4
#6
#打end
#1 2
#2 4
#3 6
