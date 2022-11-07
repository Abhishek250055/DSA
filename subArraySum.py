# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position
# is 12.

import array
l=[]
size=int(input("Enter the size of array: "))
for i in range(size):
    data=int(input())
    l.append(data)
arr=array.array('i',l)
print(arr)
target=int(input("Enter the target: "))
def ans(arr,size,target):
    for k in range(0,size):
        for k1 in range(k+1,size):
            for k2 in range(k1+1,size):
                if arr[k]+arr[k1]+arr[k2]==target:
                    return k,k2

print(ans(arr,size,target))