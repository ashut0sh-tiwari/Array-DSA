"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""

nums = [-10,4,-5]


#function to get the maximum subarray from the list
def maxSubArray(list):
    #initialising the variables
    csum=0
    msum=nums[0]
    #iterating over the list
    for i in nums:
        #if the value of csum is less than 0 then we are initialising it with 0 again
        if csum < 0:
            csum = 0
        #else adding the value to the csum
        csum += i
        #storing the value of csum in msum and using the max function to store the maximum value
        msum = max(msum, csum)
    return msum

solution = maxSubArray(nums)

print(solution)



