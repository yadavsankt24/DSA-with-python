# TWO SUM QUESTION OF SORTED ARRAY 

# APPROACH 1
'''
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0 
    right = len(numbers) -1
    
    while left < right:
        for i in range(0,len(numbers)):
            for j in range(i,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [numbers[i],numbers[j]]

array = [1,2,3,4,5,6,7]
target = 13
result = twoSum(array,target)
print(result)

'''

