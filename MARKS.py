# Marks
marks=int(input("enter marks (0-100):"))
 
 #check conditions
if marks <35:
    print("fail")
elif marks<= 59:
    print("pass")
elif marks <=84:
    print("first class")
elif marks<=100:
    print ("distionction")
else:
    print("Invalid marks ! please enter between 0 and 100.")