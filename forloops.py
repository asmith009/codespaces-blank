fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        fruits.remove('banana')
        print(x)


grades = [80, 90, 70, 100, 60]

for x in grades:
    if x <=  70:
        grades.remove(x)
    print(x)