'''
You are given an integer array nums of length n and an integer target.
Find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

def three_sum_closest(nums,target):
    nums.sort() # pehle sort karo
    closest = 0 # ek variable define karo jo sabse pass wala no dhoondega
    diff = float('inf') #ek define karo jo imaginarily sabse door aur bada h 
    for i in range(len(nums)-2): #kyuki 3 sum hai to 3 no chahiye hi
        left = i+1
        right = len(nums) -1
        while left < right:
            total = nums[i] + nums[left] + nums[right] # sabko  add kar do taki total malum pad sake jo target se pass hoga 
            absolute_diff = abs(target-total) # target se total km karne pe malum padega ki kitna difference h dono k beech
            if diff> absolute_diff: # agar bada h diffrence se to chote wale no ko bade ki jagah dalo kyuki minimum find karna h ( closest)
                diff = absolute_diff
                closest = total #jo total h usko usko hame dhoondna h jo target ke pass ho sakta h isliye jitni baad total chota hoga uthni baar ye closest chota hoga
            if(total==target): # sabse behetar case agar target ke barabar ho jaye to return karo
                return closest
            if total<target: # aur nai h to jese two sum me karte the wese hi karte rho
                left+=1
            else:
                right-=1
    return closest

print(three_sum_closest([-1,2,1,-4],1))
