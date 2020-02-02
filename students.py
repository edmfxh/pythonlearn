n = int(input("Enter the number of students:"))
data = {}#the dictionary varity of storing data
subjects = ('physics','maths','history')
for i in range(0,n):
    name = input('Enter the name of the students {}:'.format(i+1))#obtaining names
#can it explain that adding a pair?
    marks = []#list
    for x in subjects:
        marks.append(int(input('Enter marks of {}:'.format(x))))#obtaining the scores of every subject
    data[name] = marks
for x,y in data.items():#listing all elements in data
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failef :(")
    else:
        print(x,"passed :)")


