"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

l1 = [1,2,4,5,6,7,9]
val = 8





#binary search function
def binarySearch(list, value):
    low = 0 # initialising low value
    high = len(list) - 1 #initialising high value
    while(low <= high):
        mid = (low + high) // 2 #initialising mid value
        if (list[mid] == value):
            return mid
        elif (list[mid] > value):
            high = mid - 1 #updating mid value
        else:
            low = mid + 1 #updating mid value
    return low

solution = binarySearch(l1, val)
print(solution)