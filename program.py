val1=10
val2=30
a=int(input("enter val1:"))
b=int(input("enter val2:"))

#Arithemetical Operators

print("val1+val2=",val1+val2)
print("val1-val2=",val1-val2)
print("val1*val2=",val1*val2)
print("val1/val2=",val1/val2)
print("val1//val2=",val1//val2)
print("val1%val2=",val1%val2)
print("val1**val2=",val1**val1)

# For grading system

marks=float(input("enter the marks"))
if marks>=90:
    grade="A"

elif marks>=80:
    grade="B"

elif marks>=70:
    grade="C"

elif marks>=60:
    grade="D"

else:
    print("your grade is:",grade)

#Even are Odd

num=int(input("enter a number"))
if num%2==0:
    print("Even")
else:
    print("Odd")

#Calculator
num=float (input("Enter first number:"))
operation= input("enter operation(+,_,*,/):")
num2=float (input("enter secound number:"))


