#Breaks
for number in range(1,10):
    if number==5:
        print("braking the loop at number 5")
        break
    print("number:",number)


# 
numbers=[1,2,4,5,7,8,10]
for num in numbers:
        if num % 2==0:
             print("First even number found:",num)
        break
else:
     print["No even number found"]

#
while True:
     user_input=input("enter 'Thanzill' to stop:")
     if user_input=='Thanzill':
        print("logined")
        break
     else:
          print("try again")