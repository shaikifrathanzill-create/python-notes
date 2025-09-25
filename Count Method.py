#Count Method
numbers=(1,2,3,2,1,2)
count_2=numbers.count(2)
print(count_2)

#Index Method
fruits=('apple','banana','mango','apple')
index_apple=fruits.index('apple')
print(index_apple) 

#SET (unique elements)
unique_numbers={1,2,3,2,1,4,5,4,6}
print(unique_numbers)

#Adding elements
unique_numbers.add(7)
print(unique_numbers)

#rEMOVING ELEMENTS
unique_numbers.remove(2)
print(unique_numbers) 

#DICITIONARY
student={
    'Name':'Thanzill',
    'Age' : '18',
    'Grade': 'A'
}
print(student)

print(student['Name'])

student['Course']= 'CS'
print(student)