"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."""

l1 = [1,2,2,3,4,5,6,6,7,8,9,9,9]
val = 9




def removeElements(list, val): #total number of elements after removing val from the list
   
    while val in list: #iterating through the list
        
        list.remove(val) #if val in list then remove that element from the list
            
            
    return len(list) #return number of element in the list

solution = removeElements(l1, val)
print(solution)