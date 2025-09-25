#divisible by 4,5
num=int(input("enter a number:"))
if num%4==0 and num%5==0:
    print(f"{num}is divisible by both 4 and 5")
else:
    print(f"{num}is not divisible by both 4 and 5")
    