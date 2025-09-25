# Array Qu?
# 1
import array
nums=array.array('i',[10,20,30,40,50])
print(nums[0])
print(nums[-1])

# 2
import array
arr=array.array('i',[10,20,30,40,50,60,70])
slice_arr=arr[2:5]
print("slice array:",slice_arr)
# 3
import array
arr=array.array('i',[10,20,30,40,50])
slice_arr=arr[-5:-2]
print("sliced array with negative indices:",slice_arr)

# 4
import array
arr=array.array('i',[1,2,3,4,5,7,8])
slice_arr=arr[1:2]
for i in range(1,8,2):
    print(i)

# 5
import array
num=array.array('i',[5,10,15,20,25,30])
print(num[:4])
count=0
for i in num [:4]:
    count+=1
print(count)    

# 6
import array
num=array.array('i',[10,20,30,40,50])
print(num[::-1])


import array
num=array.array('i',[1,2,3,4,5,6,7])
print(len(num))
print(sum(num))
print(max(num))
print(min(num))
