#ARRAY

#Integer Arrayinport
import array
numbers=array.array('i',[1,2,3,4,5])
print(numbers)

#Float array
import array
floats=array.array('f',[1,2,3,4,5])
print(floats)

#OPERATION ON ARRAYS:-

#Accessing elements
import array
nums=array.array('i',[10,20,30,40,50])
print(nums[0])
print(nums[3])

#Slicing Array:-
import array
num=array.array('i',[10,20,30,40,50])
print(num[1:4])
print(num[::-1])
print(num[1::])
print(num[2:])
print(num[:3])

#Adding elements:-
import array
nums=array.array('i',[1,2,3,5])
nums.append(4)
print(nums) 

#Insert at specific index
nums.insert(1,10)
print(nums)

# Removing eiements
nums.remove(10)
print(nums)

# Remove element by index
del nums[0]
print(nums)
