"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""
height = [1,8,6,2,5,4,8,3,7]

def maxArea(list): #function to find the maximum area
        res = 0 #initialising the variable
        l,r =0,len(list)-1 #initialising the variable
        while l<r: #looping until l and r are equal
            area = (r-l) * min(list[l], list[r]) #computing the area of rectangle where width is equal to r - l length and height is equal to min of l and r
            res = max(res, area) #staring the max value in the res
            if list[l]<list[r]: #if height of l is less than r then incrementing the l
                l += 1
            else: #else decrementing r
                r -= 1
        return res

solution = maxArea(height)
print(solution)