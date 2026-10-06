# Amazon | OA 2019 | Two Sum - Unique Pairs

# If the input is [1, 1, 2, 45, 46, 46] and the target is 47, the unique pairs are [1, 46] and [2, 45]
'''
# solution 1
def two_sum_unique(arr,target):
    left = 0
    right = len(arr)-1
    store=[]
    while left < right:
        sum = arr[left]+arr[right]
        if(sum==target): #check if the values are equal we simply store this in the store and chck further for duplicacy
            store.append([arr[left],arr[right]])
            left+=1
            right -=1
            while arr[left]==arr[left-1]:
                left+=1
            while arr[right]==arr[right+1]:
                right -=1
        elif(sum < target):
            left+=1
        else:
            right -=1
    return store
'''

# def two_sum_unique( arr, target):
#     arr.sort()
#     i, j = 0, len(arr) - 1
#     res = 0
#     while i < j:
#         if arr[i] + arr[j] < target:
#             i += 1
#         elif arr[i] + arr[j] > target:
#             j -= 1
#         else:
#             res += 1
#             vi, vj = arr[i], arr[j]
#             while i < j and arr[i] == vi:
#                 i += 1
#             while i < j and arr[j] == vj:
#                 j -= 1
#     return res #returns no of pair that are eligible
        
# arr= [1, 1, 2, 45, 46, 46]
# target = 47
# print(two_sum_unique(arr,target))




threshold = int(input("threshold: "))


def count(chunks):
    return len(chunks.split())


length = count("Hi from python i am working here as a full stack developer")

if length > threshold:
    print("chunk too large")
else:
    print("chunk within limit")