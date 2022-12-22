"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order."""



def intersect(self, nums1, nums2):
    #sorting both the arrays
    nums1 = sorted(nums1) 
    nums2 = sorted(nums2)
    i,j = 0,0 #initialising the variables
    result = [] #initailising an empty array
    while i <len(nums1) and j < len(nums2): #looping both arrays using two pointers
        if nums1[i]> nums2[j]: 
            j += 1
        elif nums1[i]<nums2[j]:
            i += 1
        else:
            result.append(nums1[i]) # if values of i and j are equal then appending that value in our empty array and increment the variables
            j += 1
            i += 1
    return result