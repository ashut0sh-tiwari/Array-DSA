"""Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution."""

nums = [-1,2,1,-4]
target = 1

def threeSumClosest(list, target):
        res = float('inf') #initialising the variable with positive infinite number     
        list.sort() #sorting the list
        for i in range(0,len(nums)-2): #iterating till the second last element
            if list[i] == list[i-1] and i >0: #if i and i+1 is the same element the skip that element
                continue
            l = i + 1 #initialising the variable
            r = len(list) - 1 #initialising the variable
            while l<r: #iterating until l and r are not same
                s = list[i] + list[l] + list[r] # storing the sum of three values
                if s == target: #if sum is equal to the target then return s
                    return s
                
                if abs(target - s)<abs(target-res): #if sum is less than target than storing that in a res variable
                    res = s

                if s<target: # if s is smaller than target then incrementing the l variable
                    l += 1
                    while list[l] == list[l-1] and l<r: #checking if l and l+1 value is same if same then keep incrementing the l variable 
                        l+=1
                else: #else deccremneting the r variable
                    r -=1
        return res #return res

sol = threeSumClosest(nums, target)
print(sol)