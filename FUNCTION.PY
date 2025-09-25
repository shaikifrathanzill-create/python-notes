#Functions
def greet():
    print("Welcome to python function!")
greet()

# passing parameters and argunents
def greet_user (name):
    print("Hello,",name)
#Calling function with argument
greet_user("Ram")

#Function ARGUMENTS TYPES:
#a:-positional arguments
def add(a,b):
    print("sum is:",a+b)
add(5,10)

#KEY WORD ARGUMENTS
def introduce(name,age):
    print(f"My name is {name}, and I am {age} years old")
introduce(age=20,name="Thanzill")

#Default Arguments
def greet(name="guest"):
    print("Hello,",name)
greet("Sita")