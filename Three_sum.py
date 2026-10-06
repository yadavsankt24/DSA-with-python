# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# for example Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


def three_sum(arr,target):
    res = []
    arr.sort()
    for i in range(len(arr)-2):
        if i > 0 and (arr[i]==arr[i-1]): # humne left aur right ka to duplicate check kar liya par i baaki tha use bhi karo aur taki -ve index na uthaye isliye i>0 ka check lagao
            continue
        left = i+1
        right = len(arr)-1
        while left < right:
            sum = arr[left]+arr[right]+arr[i]
            if(sum==target): # equal hua to 
                res.append([arr[i],arr[left],arr[right]]) # agar mil gya to append kar do aur bakio ko aage badha do left aur right 
                left+=1
                right-=1
                while  (arr[left]==arr[left-1]): #yha pe ek baar ye bhi check kar lo ki left value same to nahi piche wali se aur h to left wale ko ek ek badhate rhe jitna duplicate aaye
                    left+=1
                while arr[right] == arr[right+1]:#yha pe ek baar ye bhi check kar lo ki right value same to nahi piche wali se aur h to right wale ko ek ek badhate rhe jitna duplicate aaye
                    right-=1
            elif (sum<target): #chota hua to
                left+=1
            else: # bada hua to
                right-=1
    return res

print(three_sum([-1,0,1,2,-1,-4],0))