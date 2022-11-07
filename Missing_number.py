# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4


import array
l=[]
size=int(input("Enter the size of array: "))
for i in range(size-1):
    data=int(input())
    l.append(data)
arr=array.array('i',l)
# print(arr)
def MissingNumber(arr,size):
    all_sum=0
    for k in range(0,size+1):
        all_sum=all_sum+k

    arr_sum=0
    for i in range(0,size-1):
        arr_sum=arr_sum+arr[i]

# print(all_sum)
# print(arr_sum)
    return all_sum-arr_sum

print(MissingNumber(arr,size))


