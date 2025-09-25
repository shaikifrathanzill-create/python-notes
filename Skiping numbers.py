#skip negative numbers
numbers=[1,2,4,5,-3,-6,-9,0]
for num in numbers:
    if num <0:
        continue
    print(num)

#Skip multiple of 3
numbers=[3,2,6,5,9,10,4,6]
for num in numbers:
    if num%3==0:
        continue
    print(num) 