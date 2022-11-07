"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""





def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while m>0 and n>0: #looping till m and n have some value
            if nums1[m-1]>nums2[n-1]: #comparing the last value of both the list by their index
                nums1[m+n-1]= nums1[m-1] #updating the last index of list1 
                m -= 1 #decrementing the value of m by 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        while n > 0: # if m < n  then remaining elements of list 2 are stored in list 1 using this loop 
            nums1[m+n-1] = nums2[n-1]
            n-=1

