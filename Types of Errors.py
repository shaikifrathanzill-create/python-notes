import array
num= array.array("i",[1,2,3,4,5])
print(sum(num))
print((sum(num))/len(num))

#
num= int(input("Enter your num:"))
list=[1,2,3,4,5,6,7,8,9,10]
if num in list:
    print("present")
else:
    print("absent")

#
marks=int(input("Enyer your marks:"))
if marks<35:
   print("Fail")
elif marks<=60:
   print("Pass")
elif marks<=84:
    marks>=100
    print("Distinction")
else:
    print("Error")        