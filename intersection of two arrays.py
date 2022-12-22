"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order."""

num1 = [4,9,5]
num2 = [9,4,9,8,4]

def intersection(nums1, nums2): #better in speed
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return (set(nums1) & set(nums2))#returning the set of two sets

# print(intersection(num1,num2))

def intersect(nums1, nums2): #better in space management
    result = []#initialising the variable
    for i in nums1: #looping
        if i in nums2 and i not in result: #if element does exist in second list and not in result variable then append that element in result
            result.append(i)
    return result

print(intersect(num1,num2))