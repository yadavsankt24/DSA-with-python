
# Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.


# Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].




def segregate0and1(arr):
    # code here
    left = 0
    right =len(arr)-1
    
    while left < right:
        while left < right and arr[left]==0: #if left =0 then move left
            left +=1
        
        while left < right and arr[right]==1: #if right =1 then move right
            right -=1
            
        if(left < right): # if anyone is not satisfied then swap the left and right so 1 comes last and 0 at first
            arr[left],arr[right]= arr[right],arr[left]
            left+=1
            right-=1
            
    return arr

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(segregate0and1(arr))