# TWO SUM QUESTION OF SORTED ARRAY 
'''
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
Find two numbers such that they add up to a specific target number. Let these two numbers be
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length. Return the indices 
of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''


# APPROACH 1
'''
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(0,len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [numbers[i],numbers[j]]


array = [1,2,3,4,5,6,7]
target = 12
result = twoSum(array,target)
print(result)

'''

# APPROACH 2 (Finding indexes)
'''
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    have_seen = {}
    for index , num in enumerate(numbers):
        find_number = target- num
        if(find_number in have_seen ):
            return [have_seen[find_number],index]
        else:
            have_seen[num] = index


array = [1,2,3,4,5,6,7]
target = 3
result = twoSum(array,target)
print(result)

'''

# APPROACH 2 (Finding Values(hashmap))
'''
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    have_seen = {}
    for index , num in enumerate(numbers):
        find_number = target- num
        if(find_number in have_seen ):
            return [find_number,num]
        else:
            have_seen[num] = index


array = [1,2,3,4,5,6,7]
target = 8
result = twoSum(array,target)
print(result)

'''

# APPROACH 3 (optimized two-pointer)
'''
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    left = 0
    right = len(numbers)-1
    while left < right:
        matching_total = numbers[left] + numbers[right]
        if matching_total == target:
            return [numbers[left],numbers[right]]
        elif matching_total < target:
            left +=1
        else:
            right-=1


array = [1,2,3,4,5,6,7]
target = 5
result = twoSum(array,target)
print(result)

'''
